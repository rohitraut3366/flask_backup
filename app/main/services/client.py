import paramiko

from werkzeug.exceptions import BadRequest
from io import StringIO


def os_client(connection_data):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if "db_os_password" in connection_data:
        db_os_password = connection_data["db_os_password"]
        try:
            ssh.connect(connection_data["db_os_ip_address"],
                        username=connection_data["db_os_username"],
                        password=db_os_password)

        except Exception as e:
            raise BadRequest("Server Connection failed!")

    elif "db_os_private_key" in connection_data:
        try:
            db_os_private_key = paramiko.RSAKey.from_private_key(StringIO(connection_data["db_os_private_key"].__str__()))
        except Exception as e:
            raise BadRequest("Incorrect private key format!")

        try:
            ssh.connect(hostname=connection_data["db_os_ip_address"],
                        username=connection_data["db_os_username"],
                        pkey=db_os_private_key)

        except Exception as e:
            raise BadRequest("Server Connection failed!")

    else:
        raise BadRequest("At least one key should be present. [db_os_password, db_os_private_key]")
    return ssh
