import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
  for instance in reservation['Instances']:
    print(instance['InstanceId'], instance['InstanceType'], instance['ImageId'], instance['VpcId'], instance['SubnetId'], instance['State']['Name'])

for sg in instance['SecurityGroups']:
   print(sg['GroupId'], sg['GroupName'])

if 'PublicIpAddress' in instance:
   print(instance['PublicIpAddress'])

if 'IamInstanceProfile' in instance:
   print(instance['IamInstanceProfile'])
