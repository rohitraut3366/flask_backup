"""mongodump --db somedb --gzip --archive > dump_`date "+%Y-%m-%d"`.gz"""
from datetime import datetime

from app.main.cloud_object_storage.aws import aws_s3
from app.main.cloud_object_storage.gcp import upload_gcp_bucket
from app.main.services.client import os_client
from werkzeug.exceptions import BadRequest, InternalServerError

from app.main.services.utilities import sftp_, cloud_selection


def mongo_backup(data):
    ssh = os_client(data)
    bucket_file_name = str(datetime.utcnow()).replace(" ", "-") + ".gz"

    date_time = "/tmp/" + data['database']["backup_file_prefix"] + bucket_file_name
    try:
        ssh_stdout, ssh_stderr = ssh.exec_command(
            f"""sudo mongodump --db {data["database"]} --gzip --archive > /tmp/{datetime}""")[1:]
    except Exception as e:
        raise BadRequest("Backup Failed!")
    if sftp_(ssh, date_time):
        ssh.exec_command(f"r -rf /tmp/{date_time}")
    else:
        raise BadRequest("File Transfer Failed!")

    cloud_selection(data["cloud_details"], date_time, bucket_file_name)

    return "OK"
