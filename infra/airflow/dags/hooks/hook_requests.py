from airflow.exceptions import AirflowException
from airflow.providers.http.hooks.http import HttpHook



def make_http_request(route):
    try:
        http_hook = HttpHook(method='GET',http_conn_id='flask-service')
        response = http_hook.run(endpoint=f'{route}')
        if response.status_code != 200:
            raise AirflowException('API returned non-200 status code')
        return response.status_code
        # Tratar a resposta da API conforme necessário
    except AirflowException as e:
        raise e