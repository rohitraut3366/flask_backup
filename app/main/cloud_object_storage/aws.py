import boto3
from botocore.exceptions import ClientError


def aws_s3(access_key, secret_access_key, bucket, object_name, file_name):
    client = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key,
                          )
    try:
        response = client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        return False
    return True
