import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1', endpoint_url="http://192.168.87.127:8000")
table = dynamodb.create_table(
    TableName='TibameTable',
        KeySchema=[
            {
                'AttributeName': 'class', 'KeyType': 'HASH'
            },
            {
                'AttributeName': 'number', 'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'class', 'AttributeType': 'S'
            },
            {
                'AttributeName': 'number', 'AttributeType': 'S'
            }
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
