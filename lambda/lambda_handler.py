import boto3

def lambda_handler(event, context):
    print(event)

    if event:
        return {
            'statusCode': 200,
            'body': 'Website crawled successfully'
        }
