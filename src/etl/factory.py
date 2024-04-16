from src.etl.etl_api_to_raw import ETLApiToRaw
from src.etl.etl_raw_to_silver import ETLRawToSilver
from src.etl.etl_silver_to_gold import ETLSilverToGold
from src.etl.extractors.api import ExtractAPI
from src.etl.extractors.csv import ExtractCSVFromListFiles
from src.etl.loaders.loader_csv import LoadCSV
from src.etl.loaders.loader_sql import LoadSQLByPandas
from src.library.utils.main import list_files_from_dir
from src.library.db_connector.main import DBConnector

# Helpers
files = list_files_from_dir('data/','*.csv')
USER = 'production'
TABLE_DEST = 'tb_brt_api'

etls = {
    'api_to_raw': ETLApiToRaw(ExtractAPI(),LoadCSV()),
    'raw_to_silver': ETLRawToSilver(ExtractCSVFromListFiles(files),LoadSQLByPandas(DBConnector(USER),TABLE_DEST)),
    'silver_to_gold': ETLSilverToGold({},{})
}