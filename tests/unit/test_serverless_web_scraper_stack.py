import aws_cdk as core
import aws_cdk.assertions as assertions
from serverless_web_scraper.serverless_web_scraper_stack import ServerlessWebScraperStack


def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessWebScraperStack(app, "serverless-web-scraper")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })

