import boto3

s3 = boto3.client("s3")

bucket_name = "test-boto3-vijay"

# Retrieve a list of objects in the bucket
response = s3.list_objects(Bucket=bucket_name)

# Access the list of objects
objects = response.get("Contents", [])

# Loop through the list of objects
for obj in objects:
    print(obj["Key"])
