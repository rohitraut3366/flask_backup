import subprocess

import boto3
from botocore.exceptions import ClientError


def aws_s3(access_key, secret_access_key, local_file, bucket, object_name, path):
    client = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key,
                          )
    try:
        response = client.upload_file(local_file, bucket, path + "/" + object_name)
    except ClientError as e:
        return False
    try:
        subprocess.getstatusoutput(f"rm -rf {local_file}")
    except Exception as e:
        pass
    return True
