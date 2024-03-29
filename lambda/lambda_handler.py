import boto3
import json
import urllib3


def handler(event, context):
    print(event)
    targetURL = event["url"]

    links = findLinks(targetURL)

    return {
        'statusCode': 200,
        'body': links
    }


def findLinks(link: str) -> list[str]:
    session = urllib3.PoolManager()
    r = session.request("GET", link)
    print("r:", r)
    print("r.data:", r.data)
    return []

