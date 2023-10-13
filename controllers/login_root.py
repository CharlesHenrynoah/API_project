import datetime
import os

from dotenv import load_dotenv

from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse
from jose import jwt

from classes.User import User
from config_alchemy import Config

load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY")


def login_root(email, password):
    try:
        sql_req = select(User).where(User.EMAIL == email)
        with Session(Config.engine) as session:
            for row in session.execute(sql_req).first():
                user = row
        if user is None or user.PASSWORD.strip() != password:
            print("L'utilisateur n'existe pas ou le mot de passe est incorrect.")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"message": "Informations d'identification incorrectes"}
            )

        print(f"Connexion réussie. Vous êtes connecté en tant qu'utilisateur : {user.EMAIL}")

        token_payload = {
            "email": user.EMAIL.strip(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")

        print(f"Votre jeton JWT a été généré avec succès.")

        # Retournez le token directement comme valeur de retour
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": token}
        )

    except Exception as e:
        print(f"Une erreur s'est produite lors de la vérification de l'utilisateur : {e}")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Une erreur interne s'est produite"}
        )

    finally:
        session.close()
