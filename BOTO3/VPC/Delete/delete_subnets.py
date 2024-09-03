import boto3

Subnet_id = 'subnet-02f9f72728b5e6272'
ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=Subnet_id,
)