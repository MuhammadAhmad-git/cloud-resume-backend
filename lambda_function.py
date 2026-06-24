import json
import boto3

# Initialize the DynamoDB resource explicitly in Frankfurt
dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('RESUME-COUNTER')

def lambda_handler(event, context):
    # Atomic increment operation on DynamoDB
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='ADD #c :val',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    # Extract the updated count
    updated_count = int(response['Attributes']['count'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        },
        'body': json.dumps({'count': updated_count})
    }
