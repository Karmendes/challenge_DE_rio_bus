from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from hooks.hook_requests import call_api



default_args={
  'owner': 'karmendes',
  'start_date': datetime(2023,3,21),
  'email': ['lucas.mendes@play9.com.br'],
  'email_on_failure': True,
  'retries': 0,
  'retry_delay': timedelta(minutes=5),
  'execution_timeout': timedelta(minutes=30),
}

dag = DAG(
  'brt_dag',
  default_args=default_args,
  description='Pipeline responsavel pela atualizacao do brt',
  schedule_interval=None,
  dagrun_timeout=timedelta(minutes=60),
  catchup=False,
  tags=['api'],
)


task_raw = PythonOperator(
    task_id='api_to_raw',
    python_callable=call_api,
    op_args=['api_to_raw'],
    dag=dag
    )

task_silver = PythonOperator(
    task_id='raw_to_silver',
    python_callable=call_api,
    op_args=['raw_to_silver'],
    dag=dag
    )

task_gold = PythonOperator(
    task_id='silver_to_gold',
    python_callable=call_api,
    op_args=['silver_to_gold'],
    dag=dag
)


task_raw >> task_silver >> task_gold