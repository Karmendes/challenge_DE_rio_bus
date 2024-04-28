from etl.etl_api_to_raw import ETLApiToRaw
from etl.etl_raw_to_silver import ETLRawToSilver
from etl.etl_silver_to_gold import ETLSilverToGold
from etl.extractors.api import ExtractAPI
from etl.extractors.s3 import ExtractFromListFiles
# from etl.loaders.loader_csv import LoadCSV
from etl.loaders.loader_sql import LoadSQLByPandas
from etl.loaders.s3 import LoadS3ByCSV
from library.utils.main import list_files_from_dir
from library.db_connector.main import DBConnector

# Helpers
files = list_files_from_dir('data/','*.csv')
USER = 'production'
TABLE_DEST = 'tb_brt_api'

etls = {
    'api_to_raw': ETLApiToRaw(ExtractAPI(),LoadS3ByCSV('raw-brt')),
    'raw_to_silver': ETLRawToSilver(ExtractFromListFiles('raw-brt','data','csv'),LoadSQLByPandas(DBConnector(USER),TABLE_DEST)),
    'silver_to_gold': ETLSilverToGold({},{})
}