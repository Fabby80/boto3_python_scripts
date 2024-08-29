import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "faby-boto3-22082024", 'Key': "test_test.txt"}, ExpiresIn=300)

print(response)