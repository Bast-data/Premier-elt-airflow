from sqlalchemy import create_engine, text

def transform():
    engine = create_engine("postgresql+psycopg2://airflow:airflow@db_postgres:5432/airflow_metadata")

    requete_truncate = """
         TRUNCATE TABLE commandes_propres;
"""

    requete_insert = r"""
        INSERT INTO commandes_propres(prenom, nom, email, age, telephone, ville, date_inscription)
        SELECT DISTINCT
          INITCAP(prenom),
          INITCAP(nom),
          LOWER(email),
          CAST(age AS INT),
          regexp_replace(telephone, '\D', '', 'g'),
          INITCAP(ville),
          CAST(date_inscription as DATE)
          FROM commandes_brutes
          WHERE CAST(age AS INT) > 0
           AND prenom IS NOT NULL AND prenom <> ''
           AND nom IS NOT NULL AND nom <> ''
           AND email IS NOT NULL AND email <> ''
           AND telephone IS NOT NULL AND telephone <> ''
           AND ville IS NOT NULL AND ville <> ''
           AND date_inscription ~ '^\d{4}-\d{2}-\d{2}$';
"""
    with engine.begin() as connexion:
       connexion.execute(text(requete_truncate))
       connexion.execute(text(requete_insert))

if __name__ == "__main__":
    transform()