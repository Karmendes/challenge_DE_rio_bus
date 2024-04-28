from json import dumps
from flask import jsonify,Response
from flask import Blueprint
from etl.factory import etls


routes = Blueprint('routes', __name__)

def run_etl(etl_name):
    try:
        etls[etl_name].run()
        o = dumps({'status':'ok','message': 'ETL concluded' })
        response = Response(o, 200, mimetype='application/json')
    except Exception as e:
        o = dumps({'status':'fail','message': 'ETL not concluded','error': e})
        response = Response(o, 500, mimetype='application/json')
    return response

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
