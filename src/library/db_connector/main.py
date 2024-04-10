from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



connections = {
    "production":
    {
        'user':'postgres',
        'pwd':'postgres',
        'host':'localhost',
        'db':'db_brt_bus',
        'port':5432,
        'schema':'sc_shorter',
        'server':'postgresql'
    }
}


class DBConnector:
    def __init__(self,name_connection,model = None):
        self.connection = connections[name_connection]
        self.model = model
        self.connect()
    def connect(self):
        self.engine = create_engine(f"{self.connection['server']}://{self.connection['user']}:{self.connection['pwd']}@{self.connection['host']}:{self.connection['port']}/{self.connection['db']}?options=-csearch_path%3D{self.connection['schema']}")
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        self.conn = self.engine.connect()