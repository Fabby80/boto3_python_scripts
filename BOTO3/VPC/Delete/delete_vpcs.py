import boto3

vpc_id = 'vpc-03b2d3bb933416853'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)