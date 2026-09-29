from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="Pipeline_commandes",
    schedule_interval="@daily",
    start_date=datetime(2026,2,1),
    catchup=False,
) as dag:

    tache_extraction = BashOperator(
        task_id="Extract",
        bash_command="python /opt/airflow/scripts/extraction_commandes.py",
    )

    tache_chargement = BashOperator(
        task_id="Load",
        bash_command="python /opt/airflow/scripts/chargement_commandes.py",
    )

    tache_transformation = BashOperator(
        task_id="Transform",
        bash_command="python /opt/airflow/scripts/transformation_commandes.py",
    )

    tache_extraction >> tache_chargement >> tache_transformation