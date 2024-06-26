import numpy as np
from etl.main import ETL
from library.logger.main import Logger

FOLDER_FROM = 'data/'
FOLDER_TO = 'data/processed'
PATTERN = '*.csv'

class ETLRawToSilver(ETL):
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader
        self.data = None
    def extract(self):
        Logger.emit('Extracting data')
        self.data = self.extractor.extract()
    def transform(self):
        Logger.emit('Transforming data')
        self.data = self.data.replace(np.nan, None)
    def load(self):
        Logger.emit('Loading data')
        self.loader.set_data(self.data)
        self.loader.load()
    def clean(self):
        Logger.emit('Cleaning data')
        self.extractor.clean()
    def run(self):
        Logger.emit('Starting process')
        self.extract()
        self.transform()
        self.load()
        self.clean()
        Logger.emit('Ending process')