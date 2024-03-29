import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('TibameTable')

classes = 'dc103'
number = 15
name = 'SHI HAO'

response = table.put_item(
    Item={
        'class': classes,
        'number': number,
        'name': name
        }
    )
