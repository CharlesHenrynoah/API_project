from sqlalchemy import Column, SmallInteger, String

from classes.Base import BaseModel


class Production(BaseModel):
    __tablename__ = 'PRODUCTION'

    CODE_PRODUCTION = Column(SmallInteger, primary_key=True)
    UN = Column(String(20))
    NOM_PRODUCTION = Column(String(20))