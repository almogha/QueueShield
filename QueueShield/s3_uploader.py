import logging

import boto3

from QueueShield.config import AWS_DEFAULT_REGION, S3_BUCKET_NAME


def upload_log_to_s3(file_path="log.txt"):
    """Uploads the log file to an S3 bucket."""
    s3 = boto3.client("s3", region_name=AWS_DEFAULT_REGION)
    s3.upload_file(file_path, S3_BUCKET_NAME, "log.txt")
    logging.info("Log file uploaded to S3 successfully.")
