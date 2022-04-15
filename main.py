# sudo pip3 install boto3
import boto3

BUCKET_NAME = 'ionawright-bucket-s1108900'

s3_client = boto3.client('s3')
# ability to interact with s3 in AWS

#  def create_bucket(bucket_name, region=None):
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

# List all buckets
bucketResponse = s3_client.list_buckets()
for bucket in bucketResponse["Buckets"]:
    print(bucket)
    
# SNS topic creation
sns_client = boto3.client('sns')
topicResponse = sns_client.create_topic(
    Name='ionawright-sns-topic-s1108900',
)

# upload a file
import logging
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# snsSub = sns_client.subscribe(
#     TopicArn='arn:aws:sns:us-east-1:132123009992:ionawright-sns-topic-s1108900',
#     Protocol='sms',
#     Endpoint='07880342772'
# )

# print(snsSub)