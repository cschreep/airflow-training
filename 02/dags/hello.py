from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hello',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag:

    t1 = PythonOperator(
        task_id='hello',
        python_callable=lambda: "Hello, Airflow!"
    )

    t2 = PythonOperator(
        task_id='goodbye',
        python_callable=lambda: "Goodbye, Airflow!"
    )

    t1 >> t2
