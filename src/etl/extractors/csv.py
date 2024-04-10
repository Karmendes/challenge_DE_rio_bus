from src.etl.main import Extractors
from src.library.data_manipulator.main import DataManipulator

class ExtractCSVFromListFiles(Extractors):
    def __init__(self,path):
        self.manipulator = DataManipulator
        self.path = path
    def extract(self):
        dfm = DataManipulator({})
        return dfm.read_csv_from_list(self.path)
