from flask import jsonify
from flask import Blueprint
from src.etl.factory import etls
from src.library.logger.main import Logger

routes = Blueprint('routes', __name__)

def run_etl(etl_name):
    try:
        Logger.emit(f'Inicializando ETL {etl_name}')
        etls[etl_name].run()
        Logger.emit(f'Terminando ETL {etl_name}')
        return jsonify({"status": "success", "status_code": 200})
    except Exception as e:
        Logger.emit(f'ETL {etl_name} nao completado: {str(e)}')
        return jsonify({"status": "fail", "status_code": 500})

@routes.route("/liveness", methods=["GET"])
def liveness():
    return jsonify('I am alive!')

@routes.route("/api_to_raw", methods=["GET"])
def etl_api_to_raw():
    return run_etl('api_to_raw')

@routes.route("/raw_to_silver", methods=["GET"])
def etl_raw_to_silver():
    return run_etl('raw_to_silver')

@routes.route("/silver_to_gold", methods=["GET"])
def etl_raw_to_gold():
    return run_etl('silver_to_gold')
