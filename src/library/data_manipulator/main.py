from io import StringIO
import pandas as pd

class DataManipulator:
    def __init__(self,data):
        if list == type(data):
            if isinstance(data[0], pd.DataFrame):
                self.df = pd.concat( data , ignore_index=True )
                self.df.drop_duplicates(inplace=True)
            else:
                self.df = pd.DataFrame( [{**row} for row in data] )
        elif dict == type(data) and data.get('data', None):
            self.df = pd.DataFrame(data['data'], columns=data['columns'])
        elif isinstance(data, dict):
            self.df = pd.DataFrame(data)
        elif isinstance(data, StringIO):
            self.df = pd.read_csv(data, sep=',')
        else:
            self.df = data
    def read_csv_from_list(self,paths):
        list_df = [pd.read_csv(x) for x in paths]
        self.df = pd.concat(list_df)
        return self.df
    def write_csv(self,path):
        self.df.to_csv(path)