import datetime

from werkzeug.exceptions import InternalServerError

from app.main.services.client import os_client
from app.main.services.utilities import sftp_, cloud_selection


def mysql_backup(data):
    ssh = os_client(data["os"])
    bucket_file_name = str(datetime.datetime.utcnow()).replace(" ", "-") + ".gz"
    date_time = "/tmp/" + data['database']["backup_file_prefix"] + bucket_file_name
    ssh_stdout, ssh_stderr = ssh.exec_command(f"sudo mysqldump -u {data['database']['mysql_user_name']} "
                                              f"-p{data['database']['mysql_user_password']} "
                                              f"--single-transaction --databases {data['database']['mysql_db_name']} "
                                              f"| gzip -c > {date_time}")[1:]

    if ssh_stderr.read().decode() != "":
        return {
            "operation": "mysql db backup",
            "std_error": ssh_stderr.read().decode()
        }

    if sftp_(ssh, date_time):
        ssh.exec_command(f"rm -rf {date_time}")
    else:
        raise InternalServerError("Failed to download backup")

    ssh.close()

    cloud_selection(data["cloud_details"], date_time, bucket_file_name)
    return "OK"
