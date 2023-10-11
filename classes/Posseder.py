from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

from classes.Base import BaseModel


class Posseder(BaseModel):
    __tablename__ = 'POSSEDER'

    ID_ENGRAIS = Column(Integer, primary_key=True)
    CODE_ELEMENT = Column(String(5), ForeignKey('ELEMENT_CHIMIQUES.CODE_ELEMENT'))
    VALEUR = Column(Numeric)