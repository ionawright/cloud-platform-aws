# sudo pip3 install boto3
import boto3

BUCKET_NAME = 'ionawright-bucket-s1108900'

s3_client = boto3.client('s3')
# ability to interact with s3 in AWS

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