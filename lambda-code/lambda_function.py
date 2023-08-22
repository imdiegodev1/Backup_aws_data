import boto3
import os

class DynamoAccesor:
    def __init__(self, dyynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dyynamo_table)

    def get_data_from_dynamo(self):
        response = self.table.scan()

        return response
    

def lambda_handler(event, context):

    dynamo_backend = DynamoAccesor(context['table'])
    db_elements = dynamo_backend.get_data_from_dynamo()

    return db_elements