import json

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Hello, World!'})
        }
    elif event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Hello, {body["name"]}!'})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid HTTP method'})
        }
