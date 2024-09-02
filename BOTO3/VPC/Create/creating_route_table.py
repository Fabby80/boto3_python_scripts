import boto3

vpc_id = 'vpc-03b2d3bb933416853'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id,)

print(routeTable['RouteTable']['RouteTableId'])