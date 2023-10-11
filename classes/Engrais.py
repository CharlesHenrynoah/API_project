from sqlalchemy import Column, Integer, String

from classes.Base import Base, BaseModel


class Engrais(BaseModel):
    __tablename__ = 'ENGRAIS'

    ID_ENGRAIS = Column(Integer, primary_key=True)
    UN = Column(String(20))
    NOM_ENGRAIS = Column(String(20))