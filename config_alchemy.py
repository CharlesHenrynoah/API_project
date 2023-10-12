import json
import os
from sys import exc_info

from dotenv import load_dotenv
import psycopg2
from pathlib import Path
from sqlalchemy import create_engine, select, orm, insert, update
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()


class Config:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    @staticmethod
    def database_connection():
        Config.engine = create_engine(Config.DATABASE_URL, echo=False)
        try:
            Config.engine.connect()
            return f'Connecté à PostgresSQL'
        except Exception as e:
            return f"Erreur de connexion à la base de données : {e}"

    @staticmethod
    def selectData(class_to_select):
        sql_req = select(class_to_select)
        results = []

        try:
            with Session(Config.engine) as session:
                for row in session.execute(sql_req):
                    result = row[0]
                    results.append(result.as_dict())

            return results
        except Exception as e:
            return e

    @staticmethod
    def insertData(class_to_insert, data):

        if not data:
            return {"error": "No data provided"}

        sql_req = insert(class_to_insert).values(data)
        try:
            with Session(Config.engine) as session:
                session.execute(sql_req)
                session.commit()
                return {"result": "Data has been added."}

        except Exception as e:
            error = type(e)
            print(error.__name__)
            if error.__name__ == "CompileError":
                return {"error": "Data key error"}
            return {"error": str(e)}

    # Dans votre config.py
    @staticmethod
    def updateData(class_to_insert, data, column, condition):
        try:
            sql_req = update(class_to_insert).where(getattr(class_to_insert, column) == condition).values(data)
            with Config.Session() as session:
                session.execute(sql_req)
                session.commit()
                updated_data = session.query(class_to_insert).filter(
                    getattr(class_to_insert, column) == condition).first()
                return updated_data
        except Exception as e:
            return "erreur", str(e)

    @staticmethod
    def deleteData(class_to_delete, condition):
        with Config.Session() as session:
            item_to_delete = session.query(class_to_delete).get(condition)
            if item_to_delete is not None:
                session.delete(item_to_delete)
                session.commit()
                increment_and_log_api_counter('DELETE')
                return "Donnée supprimée avec succès"
            else:
                return "Erreur : Donnée non trouvée"

def increment_and_log_api_counter(request_method):
    # Lire les compteurs actuels à partir du fichier
    counters = {'GET': 0, 'POST': 0, 'PATCH': 0, 'DELETE': 0}

    try:
        with open("log.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" => ")
                if len(parts) == 2:
                    method, count = parts[0], int(parts[1])
                    if method in counters:
                        counters[method] = count
    except (FileNotFoundError, ValueError):
        pass

    # Incrémenter le compteur pour la méthode de la requête actuelle
    if request_method in counters:
        counters[request_method] += 1

    # Écrire les compteurs mis à jour dans le fichier
    with open("log.txt", "w") as file:
        for method, count in counters.items():
            file.write(f"{method} => {count}\n")

    # Retourner le compteur mis à jour pour la méthode de la requête actuelle
    return counters[request_method]
