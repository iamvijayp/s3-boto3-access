import boto3

# Define the AWS role to assume
role_arn = "arn:aws:iam::603566123900:role/s3-cross-accountrole-A"


# Define the session and client for the S3 service
session = boto3.Session(
)
client = session.client("s3")

# Use the STS service to assume the role
sts_client = session.client("sts")
assumed_role_object = sts_client.assume_role(
    RoleArn=role_arn,
    RoleSessionName="AssumeRoleSession1"
)

# Update the session with the assumed role credentials
session = boto3.Session(
    aws_access_key_id=assumed_role_object["Credentials"]["AccessKeyId"],
    aws_secret_access_key=assumed_role_object["Credentials"]["SecretAccessKey"],
    aws_session_token=assumed_role_object["Credentials"]["SessionToken"]
)

# Define the S3 bucket and prefix (if desired)
bucket_name = "cloudgalaxyhq123"
prefix = "/"

# Use the S3 service to list objects from the bucket
result = client.list_objects(Bucket=bucket_name, Prefix=prefix)

# Get the list of objects from the result
objects = result.get("Contents", [])

# Print the object keys
for obj in objects:
    print(obj["Key"])
