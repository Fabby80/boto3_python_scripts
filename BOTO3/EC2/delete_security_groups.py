import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-01c2e98cc20f5d65d',
)

print(response)