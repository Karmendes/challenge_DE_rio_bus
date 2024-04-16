from src.etl.main import ETL
from src.library.dbt_navigator.main import DBTNavigator
from src.library.logger.main import Logger

PATH = "C:/Users/User/Desktop/projects/challenge_DE_rio_bus/dbt_pipelines"
MODEL = "finals"

class ETLSilverToGold(ETL):
    def __init__(self,extractor,loader):
        Logger.emit('Initializing ETL silver to gold')
        self.extractor = extractor
        self.loader = loader
        self.data = None
    def extract(self):
        Logger.emit('Extracting data')
        pass
    def transform(self):
        Logger.emit('Transforming data')
        dbt = DBTNavigator(PATH)
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