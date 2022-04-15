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

snsSub = sns_client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:132123009992:ionawright-sns-topic-s1108900',
    Protocol='sms',
    Endpoint='07880342772'
)

print(snsSub)