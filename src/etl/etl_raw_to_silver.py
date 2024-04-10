import numpy as np
from src.etl.main import ETL


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
    def run(self):
        self.extract()
        self.transform()
        self.load()