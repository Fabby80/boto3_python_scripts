import boto3

route_table_id = 'rtb-08dd0b9096be8bf18'
internet_gateway_id = 'igw-0b6b97859e7f264a8'


ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)