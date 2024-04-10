import os
import datetime

def list_files(folder, prefix):
    files = []
    for file in os.listdir(folder):
        if file.startswith(prefix):
            files.append(file)

    return files

def convert_timestamp(timestamp):
    timestamp_seconds = timestamp / 1000
    datetime_object = datetime.datetime.fromtimestamp(timestamp_seconds)
    #formatted_date = datetime_object.strftime('%y-%m-%d %H:%M:%S')
    return datetime_object