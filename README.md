# flask_backup_restapi
### TODO: AWS AND AZURE is in progress

1. MYSQL_BACK and Upload to GCP 
Example <br>

NOTE: ```must pass one of the key: db_os_private_key or db_os_password```
```
Endpoint: api/v1.0/mysql
INPUT JSON: 
{
    "os": {
        "db_os_ip_address": "52.66.40.221",
        "db_os_private_key or db_os_password": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAkb1j0sjJv41nV8FMVFYAF0UQKBGZOUzBLUo1ClgOf4w06D5Mi07AbROpiEzgxuPHMqzV54eoNP+aECM/9M+IVLoU/ws21hf6/kBOt2HqzAGUuoQPRJnHwLwEV86w6ykVFLiN/DWGT9sbcLR4+8mdOneOqooD+TWo5E69R7zoCxx4k0q7OtQ+ZYOp8s6ePxIntEhb58BTUFxHm/E5JG/+nlrtKi9zqXN5o4dhdAQhMSiigqKoRe0DVZCGg5SbY3d7VZXMGOarGkkRCBQIDAQABAoIBAHuas/IOx0UFybMcxv70HYme0nAZVOnLFj+yI0ANpJZLCmHcZZamivsIIJ6eJ4XmBMz1H/80Hwb6b1xsYSF6bg7HhEGsq/2lAGDY7U+u5uKjlxmtVzp7elXBRZViVA5j9yAz1b/0m9BNP30CQ5CBklPjCu2Y/rwA2S3/x8fIYnHvWt6EaMr+PnEdRijxjNOoZzrDx3Po3+pNMWrH8JKHnFefMcNs59AL8tw+8w1XW40tVyeB6k/6/0NFx63WNwxxeVxsaHYU/fHIZeRqQVFkE4XoBix2QrFyNuKNgcTm2OHwvlyYVAeI6rgE2WCRjQ//BZgxpmKdARdGsDoW6/4ySrUCgYEA/dIJint/HR0W8ub8fKKaO3NhPIRClIL6zH3sQsXSdd+YzTzs9pfyKB3tsKuyqDsxVYVozFtF+VR/uRRzZREhMthXm0k3ZzYppCh6JhSIZp9RqftTLAEXtM0VQ9paEwOxPBO/MvRhm2Knznh2T6B4G94jDjNCaP00GEYFI/SS/G8CgYEAkv3DeGmskYxYiPCM3QJmPdF21Yq4yGkIudGyN47mwz2cUaxYpbLwrAmfMaCn5cqL5yib66qN9hojX1IcVgzYIjc3TRRtqg+l1llwb++CUR9VAU0PzfM2xMCY61TPvch64w5/tMdmoX2hKqnCF1SQAE7OxvBvxuUEE0JW+UIiSssCgYEAh8MGk2nG7d2XXskqF8gpUs8+HU5pBmKgnyxjaLvC/IVih7Sk0qknP0nyzuKnptAybRn0mgnf/aKyxl4n8tEcvsN06HxbA/u2fjWgUCn/Y1SoK5FgRVM4SN7BFw/9ydnZvNabGDga1TAJrahFMAYW+GDywy+rv9hfOvSI31h8HkUCgYEAkEzApSgQej4t+Bk2IA0n8836+/2YE15Ra6H5c+M8lTSZjfBEgj5dWHaFqoGN8d9aYo6SKtOfU5crXHtOSAeJ8mUETA4e7lE4O2pIIAsfgqXgnEtblZILFTIBrRzwZ941DUwBgKY0EZs0KZ7HZIHmb/bttYz6HmZbDtEUctRCt+sCgYEAz2BMv6u9B7Rg2XsiGX88yfQmzVESBUu8V9F6tmlSi9ZCHtMT5fK+DCoIxXVvPXBwASX9HejjNBE8zRX9oCZCKVgZABrJx2XOG4ZPmA8LQwKz6WVeOnoP8BeoaGC7Gu92iFC7h6C7ld54jwRCFfBTEmCnISxkxAu1mV5aBO6ksKU=\n-----END RSA PRIVATE KEY-----",
        "db_os_username": "ec2-user"
    },
    "database": {
        "user_name": "rohit",
        "user_password": "3366",
        "db_name": "mydb",
        "backup_file_prefix": "wordpress"
    },
    "cloud_details": {
        "provider": "gcp",
        "destination_object_storage_name": "rohittest",
        "destination_object_storage_path": "",
        "cloud_credentials": {
            "type": "service_account",
            "project_id": "",
            "private_key_id": "",
            "private_key": "",
            "client_email": "",
            "client_id": "",
            "auth_uri": "",
            "token_uri": "",
            "auth_provider_x509_cert_url": "",
            "client_x509_cert_url": ""
        }
    }
}
```
OUTPUT:
```OK```

2. MONGO DB BACKUP and UPLOAD TO GCP 
Example <br>
```
endpoint: api/v1.0/mongodb
INPUT:
  {
    "os": {
        "db_os_ip_address": "",
        "db_os_private_key or db_os_password": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCBLUo1ClgOIUw0b4uHJDJuVTFNfExatu/xbDrGAGpBUHIakdyzHbDq5cS4SizEH1eIKuT/U2WXUag2tBOf4w06D5Mi07AbROpiEzgxuPHMqzV54eoNP+aECM/9M+IVLoU/ws21hf6/kBOt2HqzAGUuoQPRJnHwLwEV86w6ykVFLiN/DWGT9sbcLR4+8mdOneOqooD+TWo5E69R7zoCxx4k0q7OtQ+ZYOp8s6ePxIntEhb58BTUFxHm/E5JG/+nlrtKi9zqXN5o4dhdAQhMSiigqKoRe0DVZCGg5SbY3d7VZXMGOarGkkRCBQIDAQABAoIBAHuas/IOx0UFybMcxv70HYme0nAZVOnLFj+yI0ANpJZLCmHcZZamivsIIJ6eJ4XmBMz1H/80Hwb6b1xsYSF6bg7HhEGsq/2lAGDY7U+u5uKjlxmtVzp7elXBRZViVA5j9yAz1b/0m9BNP30CQ5CBklPjCu2Y/rwA2S3/x8fIYnHvWt6EaMr+PnEdRijxjNOoZzrDx3Po3+pNMWrH8JKHnFefMcNs59AL8tw+8w1XW40tVyeB6k/6/0NFx63WNwxxeVxsaHYU/fHIZeRqQVFkE4XoBix2QrFyNuKNgcTm2OHwvlyYVAeI6rgE2WCRjQ//BZgxpmKdARdGsDoW6/4ySrUCgYEA/dIJint/HR0W8ub8fKKaO3NhPIRClIL6zH3sQsXSdd+YzTzs9pfyKB3tsKuyqDsxVYVozFtF+VR/uRRzZREhMthXm0k3ZzYppCh6JhSIZp9RqftTLAEXtM0VQ9paEwOxPBO/MvRhm2Knznh2T6B4G94jDjNCaP00GEYFI/SS/G8CgYEAkv3DeGmskYxYiPCM3QJmPdF21Yq4yGkIudGyN47mwz2cUaxYpbLwrAmfMaCn5cqL5yib66qN9hojX1IcVgzYIjc3TRRtqg+l1llwb++CUR9VAU0PzfM2xMCY61TPvch64w5/tMdmoX2hKqnCF1SQAE7OxvBvxuUEE0JW+UIiSssCgYEAh8MGk2nG7d2XXskqF8gpUs8+HU5pBmKgnyxjaLvC/IVih7Sk0qknP0nyzuKnptAybRn0mgnf/aKyxl4n8tEcvsN06HxbA/u2fjWgUCn/Y1SoK5FgRVM4SN7BFw/9ydnZvNabGDga1TAJrahFMAYW+GDywy+rv9hfOvSI31h8HkUCgYEAkEzApSgQej4t+Bk2IA0n8836+/2YE15Ra6H5c+M8lTSZjfBEgj5dWHaFqoGN8d9aYo6SKtOfU5crXHtOSAeJ8mUETA4e7lE4O2pIIAsfgqXgnEtblZILFTIBrRzwZ941DUwBgKY0EZs0KZ7HZIHmb/bttYz6HmZbDtEUctRCt+sCgYEAz2BMv6u9B7Rg2XsiGX88yfQmzVESBUu8V9F6tmlSi9ZCHtMT5fK+DCoIxXVvPXBwASX9HejjNBE8zRX9oCZCKVgZABrJx2XOG4ZPmA8LQwKz6WVeOnoP8BeoaGC7Gu92iFC7h6C7ld54jwRCFfBTEmCnISxkxAu1mV5aBO6ksKU=\n-----END RSA PRIVATE KEY-----",
        "db_os_username": ""
    },
    "database": {
        "db_name": "mydb_context",
        "backup_file_prefix": "mongo-db"
    },
    "cloud_details": {
        "provider": "gcp",
        "destination_object_storage_name": "rohittest",
        "destination_object_storage_path": "",
        "cloud_credentials": {
            "type": "service_account",
            "project_id": "",
            "private_key_id": "",
            "private_key": "",
            "client_email": "",
            "client_id": "",
            "auth_uri": "",
            "token_uri": "",
            "auth_provider_x509_cert_url": "",
            "client_x509_cert_url": ""
        }
     }
    }

```

