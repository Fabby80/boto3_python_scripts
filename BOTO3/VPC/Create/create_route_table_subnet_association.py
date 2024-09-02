import boto3

route_table_id = 'rtb-08dd0b9096be8bf18'
subnet_id = 'subnet-02f9f72728b5e6272'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association['AssociationId'])