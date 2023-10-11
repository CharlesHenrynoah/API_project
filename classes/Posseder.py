from sqlalchemy import Column, SmallInteger, String, Numeric, ForeignKey

from classes.Base import BaseModel


class Posseder(BaseModel):
    __tablename__ = 'POSSEDER'

    ID_ENGRAIS = Column(SmallInteger, primary_key=True, autoincrement=True)
    CODE_ELEMENT = Column(String(5), ForeignKey('ELEMENT_CHIMIQUES.CODE_ELEMENT'))
    VALEUR = Column(Numeric)