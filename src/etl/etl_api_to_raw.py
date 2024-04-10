import json
from datetime import datetime
import pandas as pd
from src.etl.main import ETL
from src.library.utils.main import convert_timestamp

class ETLApiToRaw(ETL):
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader
        self.data = None
        self.now = datetime.now()
    def extract(self):
        self.data = self.extractor.extract()
    def transform(self):
        decoded_data = self.data.decode('utf-8')
        dict_data = json.loads(decoded_data)
        df = pd.DataFrame.from_records(dict_data['veiculos'])
        df['dh_extraction'] = self.now
        df = df.rename(columns={'dataHora': 'datahora'})
        df['datahora'] = df['datahora'].apply(convert_timestamp)
        self.data = df
    def load(self):
        self.loader.data = self.data
        self.loader.path = f'brt_data_{self.now.strftime("%Y-%m-%d-%H-%M")}.csv'
        self.loader.load()
    def run(self):
        self.extract()
        self.transform()
        self.load()