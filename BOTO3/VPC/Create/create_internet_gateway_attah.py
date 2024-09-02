import boto3

internet_gateway_id = 'igw-0b6b97859e7f264a8'
vpc_id = 'vpc-03b2d3bb933416853'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)