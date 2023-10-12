import json
import os
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
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # default postgres port is 5432
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5433)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "culture")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    @staticmethod
    def database_connection():
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

            return {"results": results}
        except Exception as e:
            error = type(e)
            print(type(e).__name__)
            if error.__name__ == "DataError":
                return {"error": "Il y a un problème avec la condition"}
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                                content={"error": str(e)})

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

                updated_data = session.query(class_to_insert).filter(getattr(class_to_insert, column) == condition).first()
                return updated_data

        except Exception as e:
            return "erreur", {e}

    @staticmethod
    def deleteData(class_to_delete, condition):
        with Session(Config.engine) as session:
            item_to_delete = session.query(class_to_delete).get(condition)
            if item_to_delete is not None:
                session.delete(item_to_delete)
                session.commit()
                return "Donnée supprimée avec succès"
            else:
                return "Erreur : Donnée non trouvée"
