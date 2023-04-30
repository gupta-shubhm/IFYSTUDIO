import datetime

def lambda_handler(event, context):
    now = datetime.datetime.now()
    
    # Log a message
    print(f'The time is now {now}')
    
    # Perform some scheduled task
