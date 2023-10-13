import os

from dotenv import load_dotenv

load_dotenv()

from classes.User import User
from config_alchemy import Config
from jose import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session

SECRET_KEY: str = os.getenv("SECRET_KEY")


def check_permission(method, api, auth):
    try:
        # The following paths are always allowed:
        if method == 'GET' and api[1:] in ['docs', 'openapi.json', 'favicon.ico']:
            return True
        if method == 'POST' and api[1:] in ['login']:
            return True
        bearer, token = auth.split(' ')
        if bearer != 'Bearer':
            return False
        if token is None:
            return False
        token_decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        sql_req = select(User).where(User.EMAIL == token_decoded.get('email'))
        session = Session(Config.engine)
        user = session.execute(sql_req).first()
        if user is None:
            return False
        return True
    except Exception as e:
        print(e)
        return False
