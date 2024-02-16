# example_dag.py
import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sys
import os

# AsegÃºrate de que Python pueda encontrar el script dentro de la carpeta 'scripts'
script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'scripts')
sys.path.append(script_path)

# Importa la funciÃ³n desde el nuevo script. AsegÃºrate de que el nombre de la funciÃ³n coincida.
from bigquery import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2024, 2, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag = DAG(
    'datos_a_bigquery',  # CambiÃ© el nombre del DAG para reflejar el nuevo script
    default_args=default_args,
    description='DAG que procesa archivos desde la carpeta silver hasta la instancia de bigquery',
    schedule_interval=None,
)

process_task = PythonOperator(
    task_id='process_bigquery',  # task_id para reflejar el nombre del script, no necesita .py
    python_callable=main,  # debe coincidir con el nombre de la funcion dentro del script
    dag=dag,
)