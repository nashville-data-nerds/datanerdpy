#!/usr/bin/env python3

import boto3
import botocore

def download_s3_file(bucket, key):
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(bucket).download_file(key, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise