import os
import tempfile
from PIL import Image
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, key.split('/')[-1])
        with open(filepath, 'wb') as f:
            f.write(response['Body'].read())
        
        with Image.open(filepath) as image:
            image.thumbnail((128, 128))
            thumbnail = image.tobytes()
            
        thumbnail_key = key.replace('original', 'thumbnail')
        s3.put_object(Bucket=bucket, Key=thumbnail_key, Body=thumbnail)
