from src.etl.main import Loaders


class LoadCSV(Loaders):
    def __init__(self):
        self.data = None
        self.path = None
    def load(self):
        self.data.to_csv(self.path,index = False)