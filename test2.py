import boto3

# create an EC2 client
ec2 = boto3.client('ec2', region_name='us-west-2')

# call the describe_instances method
response = ec2.describe_instances()

# extract the instances from the response
instances = response['Reservations']

# print the instances
for reservation in instances:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])