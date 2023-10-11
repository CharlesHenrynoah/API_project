from sqlalchemy import Column, SmallInteger, String

from classes.Base import Base, BaseModel


class Engrais(BaseModel):
    __tablename__ = 'ENGRAIS'

    ID_ENGRAIS = Column(SmallInteger, primary_key=True, autoincrement=True)
    UN = Column(String(20))
    NOM_ENGRAIS = Column(String(20))