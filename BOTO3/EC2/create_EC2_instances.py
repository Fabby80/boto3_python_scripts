import boto3

ami_id = 'ami-0876cb8b2611473ff'
key_pair_name = 'key from boto3'
sg_group_id = 'sg-01c2e98cc20f5d65d'

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        sg_group_id
    ]
    )

print(response['Instances'][0]['InstanceId'])