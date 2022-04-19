# sudo pip3 install boto3
import boto3
from botocore.exceptions import ClientError
import logging
from time import sleep 

bucket_name = 'my-bucket-s1108900'

# Create an EC2 instance - commented out as this happens when an env is created in cloud9
# __________________________________________________
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1e")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="vockey"
    )

    print(instances["Instances"][0]["InstanceId"])

# __________________________________________________
# ability to interact with s3 in AWS
s3_client = boto3.client('s3')
# __________________________________________________

# SNS topic creation
# __________________________________________________
sns_client = boto3.client('sns')
topicResponse = sns_client.create_topic(
    Name='sns-topic-s1108900',
)
print("Topic created", topicResponse)


# Create a bucket with boto3
# __________________________________________________
# If a region is not provided, the bucket is created in the S3 default region (us-east-1).
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# List all buckets & print to the console.
# __________________________________________________
s3 = boto3.client('s3')
response = s3.list_buckets()
for bucket in response["Buckets"]:
  print(bucket)

# +++++
# _____
# +++++
# _____

# CloudFormation - figure out how to get the script to automatically run it instead of manual upload in console
# __________________________________________________

# +++++
# _____
# +++++
# _____

# Uplaod images to S3 bucket and send message 
# Not correct syntax as it just uploads the string - needed to figure out how it would upload the image
# Alternative solution was to manually upload via the console
# __________________________________________________
s3.put_object(Body='image1.jpg', Bucket=bucket_name, Key='image1.jpg')
print("Image 1 uploaded ")
sleep(30)
s3.put_object(Body='image2.png', Bucket=bucket_name, Key='image2.png')
print("Image 2 uploaded ")
sleep(30)
s3.put_object(Body='image3.jpg', Bucket=bucket_name, Key='image3.jpg')
print("Image 3 uploaded ")
sleep(30)
s3.put_object(Body='image4.jpg', Bucket=bucket_name, Key='image4.jpg')
print("Image 4 uploaded ")
sleep(30)
s3.put_object(Body='image5.jpg', Bucket=bucket_name, Key='image5.jpg')
print("Image 5 uploaded ")

# Upload/Publish message to SNS topic - attempted this but needs more investigation and code for it to link up to a file upload. 
# Notifications setup in the console.
# __________________________________________________
message = 'Image has been uploaded into bucket-s1108900'

def publish_message(sns_client, message):
    response = sns_client.publish(Message=message)
    message_id = response['MessageId']
    return message_id

bucketMessage = publish_message(sns_client, message) 
print(bucketMessage)


# Subscribes an endpoint (phone number) to the aws SNS topic
# __________________________________________________
snsSubResponse = sns_client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:132123009992:ionawright-sns-topic-s1108900',
    Protocol='sms',
    Endpoint='ZZ-ZZZZZZZZZZ'
    #   Attribute={
    #       'key': 'value'
    #   }
)

# subscription_arn = snsSubResponse["SubscriptionArn"]

# List subscriptions by topic
# __________________________________________________
response = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)
subscriptions = response["Subscriptions"]


# Send a single SMS (no topic, no subscription needed)
# __________________________________________________
sns.publish(PhoneNumber="ZZ-ZZZZZZZZZZ", 
            Message="message text")

print(snsSub)


# create a SQS queue in boto3 - not used as created in cloud formation
# __________________________________________________
def create_queue():
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    response = sqs_client.create_queue(
        QueueName="s1108900-queue",
        Attributes={
            "DelaySeconds": 100,
            "VisibilityTimeout": 30,  # 30 seconds
        }
    )
    print(response)

def get_queue_url():
    response = s3_client.get_queue_url(
        QueueName="dynamoDB-SQS-stack-SQSQueuePolicy-GOi1utuLDDep",
    )
    return response["QueueUrl"]

print(get_queue_url)


# send message to SQS
# __________________________________________________
def send_message():
    sqs_client = boto3.client("sqs", region_name="us-east-1")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/132123009992/ppeDetection-SQS",
        MessageBody=json.dumps(message)
    )
    print(response)




