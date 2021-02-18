#!/usr/bin/env python3

from aws_cdk import (
    core
)

from aws_python_topic.aws_python_topic_stack import AwsPythonTopicStack
from aws_python_topic.aws_python_topic_stack import RDSStack


app = core.App()
AwsPythonTopicStack(app, "aws-python-topic", env={'region': 'eu-west-2'})
RDSStack(app, "aws-python-rds", env={'region': 'eu-west-2'})

app.synth()
