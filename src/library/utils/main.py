import os
import datetime
from pathlib import Path
import shutil

def list_files(folder, prefix):
    files = []
    for file in os.listdir(folder):
        if file.startswith(prefix):
            files.append(file)

    return files

def list_files_from_dir(dir_path, pattern="*"):
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise ValueError(f"Diretório não encontrado: {dir_path}")
    return [str(file.absolute()) for file in dir_path.glob(pattern)]

def move_files_with_pattern(source_dir, dest_dir, pattern="*"):
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)
    if not source_dir.is_dir():
        raise ValueError(f"Diretório de origem não encontrado: {source_dir}")
    if not dest_dir.is_dir():
        raise ValueError(f"Diretório de destino não encontrado: {dest_dir}")
    moved_files = []
    for file in source_dir.glob(pattern):
        shutil.move(str(file), str(dest_dir / file.name))
        moved_files.append(file.name)
    return moved_files


def convert_timestamp(timestamp):
    timestamp_seconds = timestamp / 1000
    datetime_object = datetime.datetime.fromtimestamp(timestamp_seconds)
    #formatted_date = datetime_object.strftime('%y-%m-%d %H:%M:%S')
    return datetime_object