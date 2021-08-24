from app.main.cloud_object_storage.aws import aws_s3
from app.main.cloud_object_storage.gcp import upload_gcp_bucket
from werkzeug.exceptions import BadRequest, InternalServerError


def sftp_(ssh, file_name):
    sftp = ssh.open_sftp()
    try:
        sftp.get(file_name, file_name)
    except Exception as e:
        return False
    sftp.close()
    return True


def cloud_selection(cloud, date_time, bucket_file_name):
    if cloud["provider"] == "gcp":
        try:
            upload_gcp_bucket(local_file=date_time, bucket_name=cloud["destination_object_storage_name"],
                              filename=bucket_file_name, path=cloud["destination_object_storage_path"],
                              credentials=cloud["cloud_credentials"])

        except Exception as e:
            raise InternalServerError("Failed to upload backup")

    elif cloud["provider"] == "aws":
        if not aws_s3(local_file=date_time,
                      access_key=cloud['cloud_credentials']["access_key"],
                      secret_access_key=cloud['cloud_credentials']["secret_access_key"],
                      bucket=cloud["destination_object_storage_name"],
                      object_name=date_time,
                      path=cloud["destination_object_storage_path"], ):
            raise InternalServerError("Upload Failed!")

    elif cloud["provider"] == "azure":
        # TODO: upload to azure object storage
        pass

    else:
        raise BadRequest("Destination object storage is not recognized!")
