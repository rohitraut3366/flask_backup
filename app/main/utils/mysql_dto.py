from flask_restplus import Namespace, fields


class MYSQL(object):
    api = Namespace("MYSQL BACKUP API")

    request = api.model("Request", {
        "db_os_username": fields.String(),
        "db_os_ip_address": fields.String(),
        "db_os_password": fields.String(),
        "db_os_private_key": fields.String(),
        "mysql_user_name": fields.String(),
        "mysql_password": fields.String(),
        "mysql_db_name": fields.String(),
        "destination_object_storage": fields.String(default="gcp"),
        "destination_object_storage_name": fields.String(),
        "destination_object_storage_path": fields.String(),
        "cloud_credentials": fields.String()
    })
