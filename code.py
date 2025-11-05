#importing packages
import json
import boto3
#function definition
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    #table name
    table = dynamodb.Table('EmpMaster')
    #inserting values into table
    response = table.put_item(
       Item={
            'EmpId': '1234',
            'FirstName':'vaishali',
            'LastName':'rao',
            'DOJ':'15-07-2025'
        }
    )
    return response
