import boto3

internet_gateway_id = 'igw-0b6b97859e7f264a8'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)