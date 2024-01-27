#!/usr/bin/env python3

import aws_cdk as cdk

from serverless_web_scraper.serverless_web_scraper_stack import ServerlessWebScraperStack


app = cdk.App()
ServerlessWebScraperStack(app, "ServerlessWebScraperStack")

app.synth()
