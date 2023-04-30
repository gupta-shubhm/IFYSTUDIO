import json
import boto3

kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    for record in event['Records']:
        data = json.loads(record['kinesis']['data'])
        
        processed_data = data.upper()
        
        kinesis.put_record(
            StreamName='your-output-stream-name',
            Data=json.dumps(processed_data),
            PartitionKey='our-partition-key'
        )
