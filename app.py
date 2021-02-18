#!/usr/bin/env python3

from aws_cdk import core

from aws_python_topic.aws_python_topic_stack import AwsPythonTopicStack


app = core.App()
AwsPythonTopicStack(app, "aws-python-topic", env={'region': 'us-west-2'})

app.synth()
