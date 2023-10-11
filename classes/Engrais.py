from sqlalchemy import Column, SmallInteger, String, ForeignKey

from classes.Base import Base, BaseModel


class Engrais(BaseModel):
    __tablename__ = 'ENGRAIS'

    ID_ENGRAIS = Column(SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    UN = Column(String(20),ForeignKey("UNITE.UN"))
    NOM_ENGRAIS = Column(String(20))