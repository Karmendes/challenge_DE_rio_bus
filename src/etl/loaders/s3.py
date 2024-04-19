from io import StringIO
import os
import boto3
from dotenv import load_dotenv
from src.etl.main import Loaders


# Load environment variables from .env file
load_dotenv()


class LoadS3ByCSV(Loaders):
    def __init__(self,bucket_name):
        self.__s3_client = boto3.client('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                                        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                                        region_name=os.environ['REGION'])
        self.data = None
        self.bucket_name = bucket_name
        self.path = None
    def load(self):
        csv_buffer = StringIO()
        self.data.to_csv(csv_buffer)
        csv_buffer.seek(0)
        self.__s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=self.bucket_name, Key=self.path)
