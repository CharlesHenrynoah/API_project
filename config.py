import os
from dotenv import load_dotenv
import psycopg2

from pathlib import Path

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    @staticmethod
    def test_database_connection():
        print(Settings.POSTGRES_USER)
        try:
            conn = psycopg2.connect(
                host=Settings.POSTGRES_SERVER,
                database=Settings.POSTGRES_DB,
                user=Settings.POSTGRES_USER,
                password=Settings.POSTGRES_PASSWORD
            )

            cursor = conn.cursor()

            cursor.execute(requete_execute)

            try:
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            except:
                conn.commit()

                cursor.close()
                conn.close()

            return f"Opérations réussies"

        except Exception as e:
            return f"Erreur de connexion à la base de données : {e}"

# Test de la connexion à la base de données
test_result = Settings.test_database_connection()
