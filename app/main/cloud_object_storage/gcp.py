from google.oauth2 import service_account
from google.cloud import storage


def upload_gcp_bucket(stdout, bucket_name, path, filename, credentials):
    credentials = service_account.Credentials.from_service_account_info(credentials)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(path + f"/{filename}")
    blob.upload_from_string(stdout)
