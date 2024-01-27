import requests
from bs4 import BeautifulSoup
import boto3

def lambda_handler(event, context):
    print(event)

    if event:
        return {
            'statusCode': 200,
            'body': 'Website crawled successfully'
        }

    # Get the website URL from the event
    website_url = event['website_url']
    
    # Make a GET request to the website
    response = requests.get(website_url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Process the parsed content or perform any other desired actions
    # ...
    
    # Store visited links in RDS
    visited_links = []
    for link in soup.find_all('a'):
        visited_links.append(link.get('href'))
    
    # Connect to RDS
    rds_host = ''
    rds_user = ''
    rds_password = ''
    rds_db = ''
    
    # Create an RDS client using boto3
    rds_client = boto3.client('rds')
    
    # Insert visited links into RDS
    for link in visited_links:
        sql = "INSERT INTO visited_links (link) VALUES (%s)"
        rds_client.execute_statement(
            resourceArn='arn:aws:rds:us-east-1:123456789012:cluster:your-rds-cluster',
            secretArn='arn:aws:secretsmanager:us-east-1:123456789012:secret:your-rds-secret',
            database=rds_db,
            sql=sql,
            parameters=[
                {'name': 'link', 'value': {'stringValue': link}}
            ]
        )
    
    # Return a response
    return {
        'statusCode': 200,
        'body': 'Website crawled successfully'
    }
