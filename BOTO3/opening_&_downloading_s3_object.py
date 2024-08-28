import boto3

bucket = 'faby-boto3-22082024'
key = 'test_test_upload.txt'
filename = "test_test_upload.txt"

s3 = boto3.client('s3')

def download_single_object(client, bucket, key, filename):
 client.download_file(bucket, key, filename)