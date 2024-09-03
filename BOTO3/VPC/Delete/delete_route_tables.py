import boto3

route_table_id = 'rtb-08dd0b9096be8bf18'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)