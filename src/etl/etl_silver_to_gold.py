from src.etl.main import ETL
from src.library.dbt_navigator.main import DBTNavigator

PATH = "C:/Users/User/Desktop/projects/challenge_DE_rio_bus/dbt_pipelines"
MODEL = "finals"

class ETLSilverToGold(ETL):
    def __init__(self,extractor,loader):
        self.extractor = extractor
        self.loader = loader
        self.data = None
    def extract(self):
        pass
    def transform(self):
        dbt = DBTNavigator(PATH)
        dbt.execute(MODEL)
    def load(self):
        pass
    def run(self):
        self.extract()
        self.transform()
        self.load()