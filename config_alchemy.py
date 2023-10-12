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
    # fonction pour insérer des données dans la base de données
    def insertData(class_to_insert, data):

        if not data:
            return {"error": "No data provided"}

        sql_req = insert(class_to_insert).values(data)
        # retourn le résultat de la requête
        # si la requête a réussi, le résultat sera {"result": "Data has been added."}
        try:
            with Session(Config.engine) as session:
                session.execute(sql_req)
                session.commit()
                return {"result": "Data has been added."}

        # si la requête a échoué, le résultat sera {"error": "le message d'erreur"}
        # verifiez le type d'erreur pour savoir ce qui s'est mal passé
        except Exception as e:
            error = type(e)
            print(error.__name__)
            if error.__name__ == "CompileError":
                return {"error": "Data key error"}
            if error.__name__ == "IntegrityError":
                return {"error": "There was a foreign key violation or data duplication."}
            return {"error": str(e)}

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

                # récupère les données mises à jour
                updated_data = session.query(class_to_insert).filter(getattr(class_to_insert, column) == condition).first()
                return updated_data

        # si la requête a échoué, le résultat sera un objet avec "resultat" et l'erreur à l'intérieur
        except Exception as e:
            return "erreur", {e}

    @staticmethod
    # fonction pour supprimer des données dans la base de données
    def deleteData(class_to_delete, condition):
        # retourn le résultat de la requête
        # si la requête a réussi, le résultat sera "Donnée supprimée avec succès"
        # sinon le résultat sera "Erreur : Donnée non trouvée"
        with Session(Config.engine) as session:
            item_to_delete = session.query(class_to_delete).get(condition)
            if item_to_delete is not None:
                session.delete(item_to_delete)
                session.commit()
                return "Donnée supprimée avec succès"
            else:
                return "Erreur : Donnée non trouvée"
