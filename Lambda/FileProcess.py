import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    contents = response['Body'].read().decode('utf-8')
    
    processed_contents = process_file(contents)
    
    s3.put_object(Bucket=bucket, Key='processed/' + key, Body=processed_contents)
    
    return 'File processed successfully!'
    
def process_file(contents):
    return contents.upper()
