import boto3
import numpy as np
import json

sagemaker = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    input_data = np.array(event['input'])
    
    response = sagemaker.invoke_endpoint(
        EndpointName='your-endpoint-name',
        Body=json.dumps(input_data.tolist()),
        ContentType='application/json'
    )
    
    inference_response = json.loads(response['Body'].read().decode())
    output_data = np.array(inference_response['predictions'])
    
    return output_data.tolist()
