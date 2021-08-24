"""mongodump --db somedb --gzip --archive > dump_`date "+%Y-%m-%d"`.gz"""
from datetime import datetime

from werkzeug.exceptions import BadRequest, InternalServerError

from app.main.services.client import os_client
from app.main.services.utilities import sftp_, cloud_selection


def mongo_backup(data):
    ssh = os_client(data["os"])

    bucket_file_name = data['database']["backup_file_prefix"] + str(datetime.utcnow()).replace(" ", "-") + ".gz"
    date_time = "/tmp/" + bucket_file_name

    try:
        ssh_stdout, ssh_stderr = ssh.exec_command(
            f"""sudo mongodump --db {data["database"]["db_name"]} --gzip --archive > {date_time}""")[1:]
        exit_status = ssh_stdout.channel.recv_exit_status()

    except Exception as e:
        raise InternalServerError("Execution Failed!")

    if sftp_(ssh, date_time):
        ssh.exec_command(f"r -rf /tmp/{date_time}")
    else:
        raise BadRequest("File Transfer Failed!")

    cloud_selection(data["cloud_details"], date_time, bucket_file_name)

    return {
        "back_file_name": bucket_file_name
    }
