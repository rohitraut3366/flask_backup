import datetime

from werkzeug.exceptions import InternalServerError, BadRequest

from app.main.services.client import os_client
from app.main.services.utilities import sftp_, cloud_selection


def mysql_backup(data):
    ssh = os_client(data["os"])
    bucket_file_name = data['database']["backup_file_prefix"] + str(datetime.datetime.utcnow()).replace(" ",
                                                                                                        "-") + ".gz"
    date_time = "/tmp/" + bucket_file_name
    ssh_stdout, ssh_stderr = ssh.exec_command(f"sudo mysqldump -u {data['database']['user_name']} "
                                              f"-p{data['database']['user_password']} "
                                              f"--single-transaction --databases {data['database']['db_name']} "
                                              f"| gzip -c > {date_time}")[1:]
    exit_status = ssh_stdout.channel.recv_exit_status()
    error = ssh_stderr.read().decode()
    if exit_status != 0:
        raise BadRequest(f"Backup Failed with error: {ssh_stderr.read().decode()}")

    if error != "":
        return {
            "operation": "mongo db backup",
            "std_error": error
        }, 400

    if sftp_(ssh, date_time):
        ssh.exec_command(f"rm -rf {date_time}")
    else:
        raise InternalServerError("Failed to download backup")

    ssh.close()

    cloud_selection(data["cloud_details"], date_time, bucket_file_name)
    return {
        "back_file_name": bucket_file_name
    }
