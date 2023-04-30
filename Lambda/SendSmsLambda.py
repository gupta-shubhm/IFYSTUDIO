import boto3
import json

# create an SNS client
sns = boto3.client('sns')

def lambda_handler(event, context):
    # get the message and phone number from the event
    message = event['message']
    phone_number = event['phone_number']

    # send the message to the phone number using SNS
    response = sns.publish(
        PhoneNumber=phone_number,
        Message=message
    )

    return {
        'status':200,
        'body':json.dumps(response)
    }

