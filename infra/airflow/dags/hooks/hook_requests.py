import requests


def call_api(route):
    endpoint = f'http://api-flask-service:5000/{route}'
    response = requests.get(endpoint,timeout= 60)
    return response.status_code