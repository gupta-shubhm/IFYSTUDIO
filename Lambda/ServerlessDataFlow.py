import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response['Body'].read().decode('utf-8'))
    
    processed_data = [item.upper() for item in data]
    
    processed_key = key.replace('input', 'output')
    s3.put_object(Bucket=bucket, Key=processed_key, Body=json.dumps(processed_data))
