import json
import boto3
import botocore

def lambda_handler(event, context):
    
    # How to get the event json object
    # print(json.dumps(event))
    
    body = event['Records'][0]['body']
    message = json.loads(body)
    
    # Get the image
    file_name = message['Records'][0]['s3']['object']['key']
    print("The image that is in this record: ", file_name)
    
    # Declare bucket name (taken from code/console)
    bucket_name = "my-bucket-s1108900"
    
    # Declare table name (taken from cloud formation yaml file/console)
    table = 's1108900-table'

    # Detect labels using rekognition.
    rek_client = boto3.client('rekognition')
    response = rek_client.detect_labels(Image = {"S3Object": {"Bucket": bucket_name, "Name": file_name}}, MaxLabels=5, MinConfidence=75)
    
    # Get the labels from the rekognition response & print them to console.
    labels = response['Labels']
    print(f'Found {len(labels)} labels in the image:')
    
    # DynamoDB - add item to table
    def add_to_database(item):
        client = boto3.client('dynamodb')
        try:
            client.put_item(TableName = table, Item = item)
        except Exception as e:
            print(e)

    # Declare a JSON string for insert into DB
    insert = '{"Image": {"S": "' + file_name + '"}'
        
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        insert = insert + ',"' + name + '": { "N" :"' + str(confidence) + '"}'
        print(f'> Label "{name}" with confidence {confidence:.2f}')
    
    # Complete json string with ending bracket
    insert = insert + '}'
    print(insert)
    insert_dict = json.loads(insert)
    add_to_database(insert_dict)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Label detection complete!')
    }