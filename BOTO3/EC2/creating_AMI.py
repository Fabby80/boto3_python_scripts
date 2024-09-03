import boto3

instance_id = 'i-0f582981a6217581f'
name = 'Go to Ami'

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId=instance_id,
    Name=name,
    )
print(response['ImageId'])