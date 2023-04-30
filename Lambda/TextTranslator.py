import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):
    text = event['text']
    target_language = event['language']
    
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode=target_language
    )
    
    return response['TranslatedText']
