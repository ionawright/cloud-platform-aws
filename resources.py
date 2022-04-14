# create EC2 instance
import boto3

client = boto3.client('ec2')

response = client.run_instances(
    ImageId = '',
    InstanceType = 't2.micro',
    MinCount = 1,
    MaxCount = 1,
    Keyname = 'vockey'
)

#create bucket



# create SQS
sqs = boto3.resource('sqs')