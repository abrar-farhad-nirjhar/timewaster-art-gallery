import boto3
from config import config


def s3():
    return boto3.client("s3", region=config.DDB_REGION)