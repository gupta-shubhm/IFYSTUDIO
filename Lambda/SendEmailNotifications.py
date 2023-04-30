import boto3
import json

# Initialize the SNS client
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Extract the message and subject from the event
    message = event['message']
    subject = event['subject']
    
    # Publish the message to the SNS topic
    response = sns.publish(
        TopicArn='topic-arn',
        Message=json.dumps({'default': message}),
        Subject=subject,
        MessageStructure='json'
    )
    
    # Print the response to the CloudWatch logs
    print(response)
    
    return 'Email notification sent successfully!'
