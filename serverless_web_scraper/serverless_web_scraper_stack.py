from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
)


class ServerlessWebScraperStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "ServerlessWebScraperQueue",
            visibility_timeout=Duration.seconds(300),
        )

        crawler = lambda_.Function(
            self, "ServerlessWebScraperCrawler",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset("lambda"),
            handler="lambda_handler.handler",
            environment={
                "QUEUE_URL": queue.queue_url
            }
        )   

        sqs_event_source = lambda_event_sources.SqsEventSource(queue)

        crawler.add_event_source(sqs_event_source)

