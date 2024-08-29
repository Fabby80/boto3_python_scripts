import boto3

s3 = boto3.client('s3')

s3.upload_file('test_test.txt', 'faby-boto3-22082024', 'test_test_upload.txt', ExtraArgs={'ContentType':'text/plain'})