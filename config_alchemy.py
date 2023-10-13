import json
import os
from datetime import datetime
from sys import exc_info

import datetime

from dotenv import load_dotenv
import psycopg2
from pathlib import Path
from sqlalchemy import create_engine, select, orm, insert, update, desc, asc, text, and_
from sqlalchemy.orm import Session,sessionmaker
from starlette import status
from starlette.responses import JSONResponse

from classes.Culture import Culture
from utils.filters import apply_filters
from utils.get_fields import get_fields
from utils.order_by import order_by
from utils.to_dict import to_dict

load_dotenv()


class Config:
    # prend les variables d'environnement du fichier .env
    # si vous n'avez pas de fichier .env, créez-en un et mettez-y les variables d'environnement
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # default postgres port is 5432
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5433)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "culture")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # pour se connecter à la base de données
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    @staticmethod
    # fonction pour se connecter à la base de données
    def database_connection():
        Config.engine = create_engine(Config.DATABASE_URL, echo=False)
        try:
            Config.engine.connect()
            return f'Connecté à PostgresSQL'
        except Exception as e:
            return f"Erreur de connexion à la base de données : {e}"

    @staticmethod
    def selectData(class_to_select, skip, limit, filters, sort_by, fields):
        try:
            results = []
            # Gestion du tri
            order_by_clauses = order_by(sort_by, class_to_select)

            # Gestion des champs
            fields_to_get = get_fields(fields, class_to_select)

            #Gestion des filtres
            filter_clauses = apply_filters(filters,class_to_select)

            # Requête et pagination
            sql_req = select(*fields_to_get).offset(skip).limit(limit)
            if order_by_clauses:
                sql_req = sql_req.order_by(*order_by_clauses)
            if filter_clauses:
                sql_req = sql_req.where(and_(*filter_clauses))

            with Session(Config.engine) as session:
                for row in session.execute(sql_req).all():
                    if fields:
                        results.append(to_dict(row, fields_to_get))
                    else:
                        results.append(row[0].as_dict())

            logCompteur("GET", "V", results)
            return {"results": results}
        except Exception as e:
            error = type(e)
            print(type(e).__name__)
            logCompteur("GET", "R", type(e))
            if error.__name__ == "DataError":
                return {"error": "Il y a un problème avec la condition"}
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                                content={"error": str(e)})

    @staticmethod
    # fonction pour insérer des données dans la base de données
    def insertData(class_to_insert, data):

        if not data:
            logCompteur('POST', "R")
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "No data provided"})

        sql_req = insert(class_to_insert).values(data)
        # retourn le résultat de la requête
        # si la requête a réussi, le résultat sera {"result": "Data has been added."}
        try:
            with Session(Config.engine) as session:
                session.execute(sql_req)
                session.commit()
                logCompteur("POST", "V", sql_req)
                return JSONResponse(status_code=status.HTTP_201_CREATED, content={"result": "Data has been added."})

        # si la requête a échoué, le résultat sera {"error": "le message d'erreur"}
        # verifiez le type d'erreur pour savoir ce qui s'est mal passé
        except Exception as e:
            error = type(e)
            logCompteur('POST', "R", error.__name__)
            print(error.__name__)
            if error.__name__ == "CompileError":
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Data key error"})
            if error.__name__ == "IntegrityError":
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "There was a foreign key violation or data duplication."})
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(e)})

    # Dans votre config.py
    @staticmethod
    # fonction pour mettre à jour des données dans la base de données
    def updateData(class_to_insert, data, column, condition):
        # retourn le résultat de la requête
        # si la requête a réussi, le résultat sera un objet avec "resultat" et les données mises à jour
        try:
            sql_req = update(class_to_insert).where(getattr(class_to_insert, column) == condition).values(data)
            with Config.Session() as session:
                session.execute(sql_req)
                session.commit()
                updated_data = session.query(class_to_insert).filter(
                    getattr(class_to_insert, column) == condition).first()
                logCompteur('PATCH', "V", sql_req)
                return updated_data
        except Exception as e:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"erreur": str(e)})

    @staticmethod
    # fonction pour supprimer des données dans la base de données
    def deleteData(class_to_delete, condition):
        with Session(Config.engine) as session:
            item_to_delete = session.query(class_to_delete).get(condition)
            if item_to_delete is not None:
                session.delete(item_to_delete)
                session.commit()
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
                    "error": "Donnée supprimée avec succès"})
            else:
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error" : "Donnée non trouvée"})


from datetime import datetime

compteurV = {'GET': 0, 'POST': 0, 'PATCH': 0, 'DELETE': 0}  # Compteur
compteurR = {'GET': 0, 'POST': 0, 'PATCH': 0, 'DELETE': 0}  # Compteur
historique_log = []
dateTime = datetime.now()

def logCompteur(log_ajout, statut, requete):
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
        historique_log.append(f"{dateTime} => {log_ajout} {requete} | VALIDE")
        print("V +1")
    if log_ajout in compteurR and statut == "R":
        compteurR[log_ajout] += 1
        historique_log.append(f"{dateTime} => {log_ajout} {requete} | REFUSÉ")
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


