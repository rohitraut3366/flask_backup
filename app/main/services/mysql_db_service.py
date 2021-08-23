import datetime

from werkzeug.exceptions import BadRequest, InternalServerError
from app.main.cloud_object_storage.gcp import upload_gcp_bucket
from app.main.services.client import os_client


def mysql_backup(data):
    ssh = os_client(data)

    date_time = str(datetime.datetime.utcnow()) + ".gz"
    ssh_stdout, ssh_stderr = ssh.exec_command(f"sudo mysqldump -u {data['mysql_user_name']} -p{data['mysql_password']} "
                                              f"--single-transaction database {data['mysql_db_name']} | gzip -c ")[1:]

    if ssh_stderr.read().decode() != "":
        return {
            "operation": "mysql db backup",
            "std_error": ssh_stderr.read().decode()
        }

    if data["destination_object_storage"] is "gcp":
        try:
            upload_gcp_bucket(ssh_stdout.read(), data["destination_object_storage_name"],
                              filename=date_time, path=data["destination_object_storage_path"],
                              credentials=data["cloud_credentials"])

        except Exception as e:
            raise InternalServerError("Failed to upload backup")

    elif data["destination_object_storage"] is "aws":
        # TODO: upload_aws_bucket()
        pass

    elif data["destination_object_storage"] is "azure":
        # TODO: upload to azure object storage
        pass

    else:
        raise BadRequest("Destination object storage is not recognized!")
    return "OK"
