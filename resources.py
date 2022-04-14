# create EC2 instance
import boto3

client = boto3.client('ec2')

response = client.run_instances(
    ImageId = 'ami-08e4e35cccc6189f4',
    InstanceType = 't2.micro',
    MinCount = 1,
    MaxCount = 1,
    Keyname = 'vockey'
)

# create an EC2 instance using boto3, you may want to wait till it reaches a “Running” state until you can do something with this EC2 instanc 
ec2_inst_id = response["Instances"][0]["InstanceId"]
waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[ecs_inst_id])

#create bucket - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html

# import logging
# from botocore.exceptions import ClientError


# def create_bucket(bucket_name, region=None):
#     """Create an S3 bucket in a specified region

#     If a region is not specified, the bucket is created in the S3 default
#     region (us-east-1).

#     :param bucket_name: Bucket to create
#     :param region: String region to create bucket in, e.g., 'us-west-2'
#     :return: True if bucket created, else False
#     """

#     # Create bucket
#     try:
#         if region is None:
#             s3_client = boto3.client('s3')
#             s3_client.create_bucket(Bucket=bucket_name)
#         else:
#             s3_client = boto3.client('s3', region_name=region)
#             location = {'LocationConstraint': region}
#             s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrations3.html

s3.create_bucket(Bucket='bucket-S1108900')
s3.create_bucket(Bucket='bucket-S1108900', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


#create sns topic - this creates a communication channel. A topic lets you group multiple endpoints (such as AWS Lambda, Amazon SQS, HTTP/S, or an email address). 
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#topic 

# Amazon Simple Notification Service (SNS) Topic
sns = boto3.resource('sns')
topic = sns.Topic('arn')