import boto3
import json

class DynamoAccesor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self):
        response = self.table.scan()

        return response['Items'][0]
    
class S3Accesor:
    def __init__(self):
        self.s3_client = boto3.resource('s3')

    def upload_file(self,
                    file_name: str,
                    bucket_name: str,
                    data: dict):
        s3Object = self.s3_client.Object(bucket_name, file_name)
        s3Object.put(
            Body=(bytes(json.dumps(data).encode('UTF-8')))
        )
    

def lambda_handler(event, context):

    dynamo_backend = DynamoAccesor(event['table'])
    db_elements = dynamo_backend.get_data_from_dynamo()

    s3_object = S3Accesor()
    s3_object.upload_file(event['file_name'], #Ex. folder_path/file_name.test
                          event['bucket_name'],
                          db_elements)

    return db_elements