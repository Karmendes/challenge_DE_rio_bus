import os
from io import StringIO
import boto3
from dotenv import load_dotenv
import pandas as pd
from src.etl.main import Extractors

# Load environment variables from .env file
load_dotenv()


def list_files(s3_client,bucket_name,prefix='', ext=''):
    paginator = s3_client.get_paginator('list_objects_v2')
    files = []
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for content in page['Contents']:
            if ext and not content['Key'].endswith(ext):
                continue
            files.append(content['Key'])
    return files


class ExtractFromListFiles(Extractors):
    def __init__(self,bucket_name,path,ext):
        self.__s3_client = boto3.client('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                                        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                                        region_name=os.environ['REGION'])
        self.bucket_name = bucket_name
        self.path = path
        self.ext = ext
        self.list_files = list_files(self.__s3_client,self.bucket_name,self.path,self.ext)
    def extract(self):
        list_df = []
        for file in self.list_files:
            s3_object = self.__s3_client.get_object(Bucket=self.bucket_name, Key=file)
            csv_data = s3_object['Body'].read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            list_df.append(df)
        return pd.concat(list_df)
    def clean(self):
        for file in self.list_files:
            name_file = file.split('/')[1]
            self.__s3_client.copy_object(
                    CopySource={'Bucket': self.bucket_name, 'Key': file},
                    Bucket=self.bucket_name,
                    Key=f'data/processed/{name_file}'
                )
            self.__s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=file
                )