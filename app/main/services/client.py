import paramiko

from werkzeug.exceptions import BadRequest
from io import StringIO


def os_client(data):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if "db_os_password" in data:
        db_os_password = data["db_os_password"]
        try:
            ssh.connect(data["db_os_ip_address"], username=data["db_os_username"], password=db_os_password)
        except Exception as e:
            raise BadRequest("Server Connection failed!")

    elif "db_os_private_key" in data:
        db_os_private_key = paramiko.RSAKey.from_private_key(StringIO(data["db_os_private_key"]))

        try:
            ssh.connect(hostname=data["db_os_ip_address"], username=data["db_os_username"], pkey=db_os_private_key)
        except Exception as e:
            raise BadRequest("Server Connection failed!")

    else:
        raise BadRequest("At least one key should be present. [db_os_password, db_os_private_key]")
    return ssh
