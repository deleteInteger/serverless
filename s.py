from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url="http://192.168.87.127:8000")

table = dynamodb.Table('TibameTable')

response = table.query(
    KeyConditionExpression=Key('class').eq('dc10')
)



#dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

#response = dynamodb.batch_get_item(TableName='TibameTable', Key={'class':{'S':'dc103'}, 'number':{'N':16}})

print("---------------------------------------------\n")

for i in response['Items']:
    print(i['class'], ' ', i['number'], i['name'])
