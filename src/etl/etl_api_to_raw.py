import json
from datetime import datetime
import pandas as pd
from src.etl.main import ETL
from src.library.utils.main import convert_timestamp
from src.library.logger.main import Logger

PREFIX = 'data/brt_data_'
KEY_FROM_API = 'veiculos'

class ETLApiToRaw(ETL):
    def __init__(self,extractor,loader):
        Logger.emit('Initializing ETL api to raw')
        self.extractor = extractor
        self.loader = loader
        self.data = None
        self.now = None
    def extract(self):
        Logger.emit('Extracting data')
        self.data = self.extractor.extract()
    def transform(self):
        Logger.emit('Transforming data')
        self.now = datetime.now()
        decoded_data = self.data.decode('utf-8')
        dict_data = json.loads(decoded_data)
        df = pd.DataFrame.from_records(dict_data[KEY_FROM_API])
        df['dh_extraction'] = self.now
        df = df.rename(columns={'dataHora': 'datahora'})
        df['datahora'] = df['datahora'].apply(convert_timestamp)
        self.data = df
    def load(self):
        Logger.emit('Loading data')
        self.loader.data = self.data
        self.loader.path = f'{PREFIX}{self.now.strftime("%Y-%m-%d-%H-%M")}.csv'
        self.loader.load()
    def run(self):
        Logger.emit('Starting process')
        self.extract()
        self.transform()
        self.load()
        Logger.emit('Ending process')