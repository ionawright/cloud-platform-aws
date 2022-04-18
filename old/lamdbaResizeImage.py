import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')

def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)
        s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)




def lambda_handler(event, context):

    import json
    import boto3

    bucket_name = "my-bucket-s1108900"
    file_name = "image1.jpg"

    rek_client = boto3.client('rekognition')
    response = rek_client.detect_labels(Image = {"S3Object": {"Bucket": bucket_name, "Name": file_name}}, MaxLabels=5, MinConfidence=80)

    labels = response['Labels']
    print(f'Found {len(labels)} labels in the image:')
    
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        print(f'> Label "{name}" with confidence {confidence:.2f}')

    return {
        'statusCode': 200,
        'body': json.dumps('Complete!')
    }

    
#     def detect_labels(image, bucket):
#         client = boto3.client('rekognition')
        
#         response = client.detect_protective_equipment(Image={'S3Object':{'Bucket': my-bucket-s1108900,'Name': image1.jpg}}, 
#         SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
        
#         print('Detected PPE for people in image ' + image) 
#         print('\nDetected people\n---------------')   
#         for person in response['Persons']:
#             print('Person ID: ' + str(person['Id']))
#             print ('Body Parts\n----------')
        
#         body_parts = person['BodyParts']
#         if len(body_parts) == 0:
#             print ('No body parts found')
#         else:
#             for body_part in body_parts:
#                 print('\t'+ body_part['Name'] + '\n\t\tConfidence: ' + str(body_part['Confidence']))
#                 print('\n\t\tDetected PPE\n\t\t------------')
                    
#                 ppe_items = body_part['EquipmentDetections']
#                 if len(ppe_items) ==0:
#                     print ('\t\tNo PPE detected on ' + body_part['Name'])
#                 else:    
#                     for ppe_item in ppe_items:
#                         print('\t\t' + ppe_item['Type'] + '\n\t\t\tConfidence: ' + str(ppe_item['Confidence'])) 
#                         print('\t\tCovers body part: ' + str(ppe_item['CoversBodyPart']['Value']) + '\n\t\t\tConfidence: ' + str(ppe_item['CoversBodyPart']['Confidence']))
#                         print('\t\tBounding Box:')
#                         print ('\t\t\tTop: ' + str(ppe_item['BoundingBox']['Top']))
#                         print ('\t\t\tLeft: ' + str(ppe_item['BoundingBox']['Left']))
#                         print ('\t\t\tWidth: ' +  str(ppe_item['BoundingBox']['Width']))
#                         print ('\t\t\tHeight: ' +  str(ppe_item['BoundingBox']['Height']))
#                         print ('\t\t\tConfidence: ' + str(ppe_item['Confidence']))

#         print('Person ID Summary\n----------------')
#         display_summary('With required equipment',response['Summary']['PersonsWithRequiredEquipment'] )
#         display_summary('Without required equipment',response['Summary']['PersonsWithoutRequiredEquipment'] )
#         display_summary('Indeterminate',response['Summary']['PersonsIndeterminate'] )
        
#         return len(response['Persons'])

#     #Display summary information for supplied summary.
#     def display_summary(summary_type, summary):
#         print (summary_type + '\n\tIDs: ',end='')
#         if (len(summary)==0):
#             print('None')
#         else:
#             for num, id in enumerate(summary, start=0):
#                 if num==len(summary)-1:
#                     print (id)
#                 else:
#                     print (str(id) + ', ' , end='')

#     def main():
#         image='image1.jpg'
#         bucket='my-bucket-s1108900'
#         person_count=detect_labels(image, bucket)
#         print("Persons detected: " + str(person_count))

#         if __name__ == "__main__":
#             main()
