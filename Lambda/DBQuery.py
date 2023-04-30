import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = event['table']
    query_params = event['query']
    
    table = dynamodb.Table(table_name)
    
    response = table.query(**query_params)
    
    return response['Items']
