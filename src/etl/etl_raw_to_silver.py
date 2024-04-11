import numpy as np
from src.etl.main import ETL
from src.library.utils.main import move_files_with_pattern

FOLDER_FROM = 'data/'
FOLDER_TO = 'data/processed'
PATTERN = '*.csv'

class ETLRawToSilver(ETL):
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader
        self.data = None
    def extract(self):
        self.data = self.extractor.extract()
    def transform(self):
        self.data = self.data.replace(np.nan, None)
    def load(self):
        self.loader.set_data(self.data)
        self.loader.load()
    def clean(self):
        move_files_with_pattern(FOLDER_FROM, FOLDER_TO, pattern=PATTERN)
    def run(self):
        self.extract()
        self.transform()
        self.load()
        self.clean()