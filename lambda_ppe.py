import json
import boto3

def lambda_handler(event, context):
    
    def send_text_message(file_name):
        text_message_sns = boto3.client('sns')
        message = '** !! ** NO PPE DETECTED ** !! ** Source: ' + file_name

        try:
            response = text_message_sns.publish(
                PhoneNumber='+447880342772',
                Message = message
            )
                
            print(f'Text message sent: {message}')
            print(response)
        except Exception as e:
            print('Failed to send')

    
    body = event['Records'][0]['body']
    message = json.loads(body)
    
    file_name = message['Records'][0]['s3']['object']['key']    
    bucket_name = 'my-bucket-s1108900'
    
    rek_client = boto3.client('rekognition')
    response = rek_client.detect_protective_equipment(
        Image = {
            "S3Object": {"Bucket": bucket_name, "Name": file_name}
        }, 
        SummarizationAttributes={
        'MinConfidence': 75,
        'RequiredEquipmentTypes': ['FACE_COVER','HAND_COVER']
        }
    )
    
    ppe_response = response['Summary']
    print(ppe_response)

    if bool(ppe_response['PersonsWithoutRequiredEquipment']):
        send_text_message(file_name)
    elif bool(ppe_response['PersonsIndeterminate']):
        send_text_message(file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('PPE detection complete!')
    }