import os
from etl.main import ETL
from library.dbt_navigator.main import DBTNavigator
from library.logger.main import Logger

RELATIVE_PATH = 'dbt_pipelines'

# Obtém o caminho completo usando o módulo os
PATH = os.path.abspath(RELATIVE_PATH)
ENV = 'PROD'

#PATH = "C:/Users/User/Desktop/projects/challenge_DE_rio_bus/dbt_pipelines"
MODEL = "finals"

class ETLSilverToGold(ETL):
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader
        self.data = None
    def extract(self):
        Logger.emit('Extracting data')
        pass
    def transform(self):
        Logger.emit('Transforming data')
        dbt = DBTNavigator(PATH,env = ENV)
        dbt.execute(MODEL)
    def load(self):
        Logger.emit('Loading data')
        pass
    def run(self):
        Logger.emit('Starting process')
        self.extract()
        self.transform()
        self.load()
        Logger.emit('Ending process')