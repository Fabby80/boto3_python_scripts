import boto3  # Import the boto3 library, which is the AWS SDK for Python

# Create an S3 client using boto3
# This client allows you to interact with the Amazon S3 service
s3 = boto3.client('s3')

# Create a new S3 bucket with the specified name
# 'Bucket' is the name of the bucket you want to create
# In this case, the bucket name is 'faby-boto3-22082024'
response = s3.create_bucket(
    Bucket='faby-boto3-22082024',
)

# Print the response from the create_bucket operation
# The response contains information about the created bucket
print(response)
