from sqlalchemy import Column, SmallInteger, String, Numeric, ForeignKey

from classes.Base import BaseModel


class Posseder(BaseModel):
    __tablename__ = 'POSSEDER'

    ID_ENGRAIS = Column(SmallInteger,ForeignKey('ENGRAIS.ID_ENGRAIS'), primary_key=True, nullable=False)
    CODE_ELEMENT = Column(String(5), ForeignKey('ELEMENT_CHIMIQUES.CODE_ELEMENT'), primary_key=True, nullable=False)
    VALEUR = Column(Numeric)