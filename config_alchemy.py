import json
import os
from datetime import datetime
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
                return "Donnée supprimée avec succès"
            else:
                return "Erreur : Donnée non trouvée"


from datetime import datetime

compteurV = {'GET': 0, 'POST': 0, 'PATCH': 0, 'DELETE': 0}  # Compteur
compteurR = {'GET': 0, 'POST': 0, 'PATCH': 0, 'DELETE': 0}  # Compteur
historique_log = []
dateTime = datetime.now()

def logCompteur(log_ajout, statut):
    global historique_log

    try:
        with open("log.txt", "r") as file:
            lignes = file.readlines()
            for ligne in lignes:
                compteur_app = ligne.strip().split(" => ")
                if len(compteur_app) == 2:
                    app_type, compte = compteur_app[0], int(compteur_app[1])
                    if app_type in compteurV and statut == "V":
                        compteurV[app_type] = compte
                    if app_type in compteurR and statut == "R":
                        compteurR[app_type] = compte
    except (FileNotFoundError, ValueError):
        pass

    if log_ajout in compteurV and statut == "V":
        compteurV[log_ajout] += 1
        historique_log.append(f"{dateTime} => {log_ajout} VALIDE")
        print("V +1")
    if log_ajout in compteurR and statut == "R":
        compteurR[log_ajout] += 1
        historique_log.append(f"{dateTime} => {log_ajout} REFUSÉ")
        print("R +1")

    # Ouvrir le fichier en mode écriture ici, après les mises à jour
    with open("log.txt", "w") as file:
        file.write(f"----Compteur log----\n\n")
        for app_type, compteV in compteurV.items():
            file.write(f"{app_type} => {compteV}\n")
        file.write("\n")
        for app_type, compteR in compteurR.items():
            file.write(f"{app_type} => {compteR}\n")
        file.write(f"----Historique des requetes----\n\n")
        for entry in historique_log:
            file.write(entry + "\n")

    if statut == "V":
        return compteurV[log_ajout]
    elif statut == "R":
        return compteurR[log_ajout]


