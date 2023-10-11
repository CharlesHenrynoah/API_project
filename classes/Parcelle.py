from sqlalchemy import String, Column, SmallInteger, Numeric

from classes.Base import BaseModel


class Parcelle(BaseModel):
    __tablename__ = 'PARCELLE'

    NO_PARCELLE = Column(SmallInteger, primary_key=True)
    SURFACE = Column(Numeric)
    NOM_PARCELLE = Column(String(20))
    COORDONNEES = Column(String(20))