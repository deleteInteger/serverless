import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('TibameTable')

table.delete()
