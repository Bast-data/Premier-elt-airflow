import pandas as pd
from sqlalchemy import create_engine

def Chargement():

    df=pd.read_csv("/opt/airflow/donnees/clients_extraits")

    engine = create_engine("postgresql+psycopg2://airflow:airflow@db_postgres:5432/airflow_metadata")

    df.to_sql(
        "ventes_brutes",
        engine,
        if_exists="append",
        index=False,
    )

if __name__ == "__main__":
    Chargement()