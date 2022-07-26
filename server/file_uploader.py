from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "localhost:9001",
        access_key="admin",
        secret_key="password",
    )

    # Make 'project_data' bucket if not exist.
    found = client.bucket_exists("project")
    if not found:
        client.make_bucket("project")
    else:
        print("Bucket 'project_data' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "project", "02-src-data", "C:\\Users\\froxe\\Test_Task\\02-src-data",
    )
    print(
        "'C:\\Users\\froxe\\Test_Task\\02-src-data' is successfully uploaded as "
        "object '02-src-data' to bucket 'project_data'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)