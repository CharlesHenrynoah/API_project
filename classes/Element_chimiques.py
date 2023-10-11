from sqlalchemy import Column, String

from classes.Base import Base, BaseModel


class ElementChimiques(BaseModel):
    __tablename__ = 'ELEMENT_CHIMIQUES'

    CODE_ELEMENT = Column(String(5), primary_key=True)
    UN = Column(String(20))
    LIBELLE_ELEMENT = Column(String(20))