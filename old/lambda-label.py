# Started with this function but it was only adding one label to the DB - needed to modify so that all labels would be added

def add_to_db(item)
try:
    client.put_item(TableName = table, Item = item)
except Ecveption as e:
    print(e)
    
  for label in labels:
  name = label['Name']
  confidence = label['Confidence']
  add_db(name, confidence)
  print(f'> Label "{name}" with confidence {confidence:.2f}')


    def add_db(name, confidence):
    
        for record in event['Records']:
            client.put_item(
                TableName = table,
                Item ={'Image':{'S': file_name}, 'label': {'S': name}, 'confidence': {'N': str(confidence)}}
            )