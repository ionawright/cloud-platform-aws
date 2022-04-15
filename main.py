# sudo pip3 install boto3
import boto3
from time import sleep 

BUCKET_NAME = 'ionawright-bucket-s1108900'

s3_client = boto3.client('s3')
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


s3_client.put_object(Body='image1.png', Bucket=BUCKET_NAME, Key='image1.png')
print("Image 1 uploaded ")
sleep(30)
s3_client.put_object(Body='image1.png', Bucket=BUCKET_NAME, Key='image2.png')
print("Image 2 uploaded ")
sleep(30)
s3_client.put_object(Body='image1.png', Bucket=BUCKET_NAME, Key='image3.png')
print("Image 3 uploaded ")
sleep(30)
s3_client.put_object(Body='image1.png', Bucket=BUCKET_NAME, Key='image4.png')
print("Image 4 uploaded ")
sleep(30)
s3_client.put_object(Body='image1.png', Bucket=BUCKET_NAME, Key='image5.png')
print("Image 5 uploaded ")


# snsSub = sns_client.subscribe(
#     TopicArn='arn:aws:sns:us-east-1:132123009992:ionawright-sns-topic-s1108900',
#     Protocol='sms',
#     Endpoint='07880342772'
# )

# response = sns.subscribe(TopicArn=topic_arn, Protocol="SMS", Endpoint="+48123456789")
# subscription_arn = response["SubscriptionArn"]

# List subscriptions by topic
# response = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
# subscriptions = response["Subscriptions"]


# Send a single SMS (no topic, no subscription needed)
# sns.publish(PhoneNumber="+48123456789", 
#             Message="message text")

# print(snsSub)


# create a SQS queue
# def create_queue():
#     sqs_client = boto3.client("sqs", region_name="us-west-2")
#     response = sqs_client.create_queue(
#         QueueName="my-new-queue",
#         Attributes={
#             "DelaySeconds": "0",
#             "VisibilityTimeout": "60",  # 60 seconds
#         }
#     )
#     print(response)

# def get_queue_url():
#     sqs_client = boto3.client("sqs", region_name="us-west-2")
#     response = sqs_client.get_queue_url(
#         QueueName="my-new-queue",
#     )
#     return response["QueueUrl"]

# send message to SQS
# def send_message():
#     sqs_client = boto3.client("sqs", region_name="us-west-2")

#     message = {"key": "value"}
#     response = sqs_client.send_message(
#         QueueUrl="https://us-west-2.queue.amazonaws.com/xxx/my-new-queue",
#         MessageBody=json.dumps(message)
#     )
#     print(response)




