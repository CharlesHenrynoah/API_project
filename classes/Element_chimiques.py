from sqlalchemy import Column, String, ForeignKey

from classes.Base import Base, BaseModel


class ElementChimiques(BaseModel):
    __tablename__ = 'ELEMENT_CHIMIQUES'

    CODE_ELEMENT = Column(String(5), primary_key=True, nullable=False)
    UN = Column(String(20), ForeignKey("UNITE.UN"))
    LIBELLE_ELEMENT = Column(String(20))