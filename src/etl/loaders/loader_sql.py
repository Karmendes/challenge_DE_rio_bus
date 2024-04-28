from etl.main import Loaders


class LoadSQLByPandas(Loaders):
    def __init__(self,connector,table_name):
        self.connector = connector
        self.table_name = table_name
        self.data = None
    def set_data(self,data):
        self.data = data
    def load(self):
        self.data.to_sql(self.table_name, self.connector.conn, schema='sc_silver', if_exists='append', index=False)