import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url="http://192.168.87.127:8000")

table = dynamodb.Table('TibameTable')

classes = 'dc10'
number = '16'
name = 'ZENG HONG'

response = table.put_item(
    Item={
        'class': classes,
        'number': number,
        'name': name
        }
    )
