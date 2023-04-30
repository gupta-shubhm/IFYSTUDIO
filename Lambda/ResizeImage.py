import boto3
from io import BytesIO
from PIL import Image
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Find the bucket name and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the image from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    img_data = response['Body'].read()
    
    # Open the image using Pillow
    img = Image.open(BytesIO(img_data))
    
    # Resize the image
    img = img.resize((500, 500))
    
    # Save the resized image to a BytesIO object
    output = BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)
    
    # Upload the resized image back to S3
    s3.put_object(Bucket=bucket, Key='resized-' + key, Body=output)
    
    return {
        'status':200,
        'body':json.dumps('Image resized successfully!')
    }
