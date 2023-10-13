from sqlalchemy import Column, String, Integer, Sequence
from classes.Base import BaseModel


class User(BaseModel):
    __tablename__ = 'USER'

    ID = Column(Integer, primary_key=True,
                autoincrement=True)
    EMAIL = Column(String(20), unique=True, nullable=False)
    PASSWORD = Column(String(20), nullable=False)