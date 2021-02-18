import json
import pytest

from aws_cdk import core
from aws-python-topic.aws_python_topic_stack import AwsPythonTopicStack


def get_template():
    app = core.App()
    AwsPythonTopicStack(app, "aws-python-topic")
    return json.dumps(app.synth().get_stack("aws-python-topic").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
