import boto3

s3 = boto3.client('s3')

with open("test_test.txt", 'rb') as f:
 s3.put_object(Bucket="faby-boto3-22082024", Key="test_test.txt", Body=f, ContentType="text/plain")
