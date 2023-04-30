import json

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        response_body = {'message': 'Hello, world!'}
        response_status_code = 200
    else:
        response_body = {'message': 'Invalid request method'}
        response_status_code = 405
    
    return {
        'statusCode': response_status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response_body)
    }