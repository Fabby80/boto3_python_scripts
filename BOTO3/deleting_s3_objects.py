import boto3

bucket = "faby-boto3-22082024"
key = "test_test.txt"

s3 = boto3.client('s3')



response = s3.delete_object(
    Bucket=bucket,
    Key=key
)