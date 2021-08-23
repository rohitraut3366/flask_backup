import datetime

import paramiko
from werkzeug.exceptions import BadRequest, InternalServerError

from app.main.cloud_object_storage.gcp import upload_gcp_bucket


def mysql_backup(data):
    db_os_username = data["db_os_username"]
    db_os_ip_address = data["db_os_ip_address"]
    mysql_user_name = data["mysql_user_name"]
    mysql_password = data["mysql_password"]
    mysql_db_name = data["mysql_db_name"]
    destination_object_storage = data["destination_object_storage"]
    destination_object_storage_name = data["destination_object_storage_name"]
    destination_object_storage_path = data["destination_object_storage_path"]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if "db_os_password" in data:

        db_os_password = data["db_os_password"]
        try:
            ssh.connect(db_os_ip_address, username=db_os_username, password=db_os_password)
        except Exception as e:
            raise BadRequest("Server Connection failed!")

    elif "db_os_private_key" in data:
        db_os_private_key = data["db_os_private_key"]
        try:
            ssh.connect(hostname=db_os_ip_address, username=db_os_username, pkey=db_os_private_key)
        except Exception as e:
            raise BadRequest("Server Connection failed!")
    else:
        raise BadRequest("At least one key should be present. [db_os_password, db_os_private_key]")

    date_time = str(datetime.datetime.utcnow()) + ".gz"
    ssh_stdout, ssh_stderr = ssh.exec_command(f"mysqldump -u {mysql_user_name} -p{mysql_password} --single-transaction"
                                              f" database {mysql_db_name} | gzip -c ")[1:]

    if ssh_stderr.read().decode() != "":
        return {
            "operation": "mysql db backup",
            "std_error": ssh_stderr.read().decode()
        }

    if destination_object_storage is "gcp":
        try:
            upload_gcp_bucket(ssh_stdout.read(), destination_object_storage_name,
                              filename=date_time, path=destination_object_storage_path)
        except Exception as e:
            raise InternalServerError("Failed to upload backup")

    elif destination_object_storage is "aws":
        # TODO: upload_aws_bucket()
        pass

    elif destination_object_storage is "azure":
        # TODO: upload to azure object storage
        pass

    else:
        raise BadRequest("Destination object storage is not recognized!")
