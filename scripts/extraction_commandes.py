import pandas as pd 

def Extract():
    df=pd.read_csv("/opt/airflow/brutes/clients_raw.csv")

    df=df.drop(coloms=["client_id"])


    df.to_csv("/opt/airflow/donnees/clients_extraits.csv", index=False)

if __name__ == "__main__":
    Extract()