from sqlalchemy import Column, Integer, String

from classes.Base import BaseModel


class Production(BaseModel):
    __tablename__ = 'PRODUCTION'

    CODE_PRODUCTION = Column(Integer, primary_key=True)
    UN = Column(String(20))
    NOM_PRODUCTION = Column(String(20))