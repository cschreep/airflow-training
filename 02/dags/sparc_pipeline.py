from pathlib import Path

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = dict(
    owner='RENCI',
)

DATA_DIR = Path("/opt/airflow/data/")


def fetch_data(source: str, dest: Path):
    """Print the Airflow context and ds variable from the context."""
    response = requests.get(source)
    if response.status_code == 200:
        with dest.open('w') as out_file:
            out_file.write(response.text)
    else:
        raise ValueError(f"Failed with HTTP {response.status_code}: {response.text}")


with DAG(
    dag_id="ingest_sparc",
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    description="Data ingest and crawl pipeline for HEAL SPARC data",
) as dag:

    # TODO: Allow user to specify source and destination when triggering DAG

    fetch_data_task = PythonOperator(
        task_id="fetch data",
        python_callable=fetch_data,
        op_kwargs={
            "source": "https://stars.renci.org/var/kgx_data/sparc/curation-export.json",
            "dest": DATA_DIR / 'sparc_export.json'
        }
    )
