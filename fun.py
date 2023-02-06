# Jenkins user needs sts assume role and cross account role to use
import boto3

def assume_role(role_arn, session_name):
    sts_client = boto3.client("sts")
    assumed_role_object=sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name
    )
    credentials=assumed_role_object["Credentials"]
    return boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

role_arn = "arn:aws:iam::603566123900:role/s3-cross-accountrole-A"
session_name = "session_name"

s3_client = assume_role(role_arn, session_name).client("s3")

bucket_name = "cloudgalaxyhq123"
prefix = "home"

result = s3_client.list_objects(Bucket=bucket_name, Prefix=prefix)

objects = result.get("Contents", [])

print("Objects in bucket '{}':".format(bucket_name))
for obj in objects:
    print("  -", obj["Key"])
