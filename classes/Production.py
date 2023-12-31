from sqlalchemy import Column, SmallInteger, String, ForeignKey

from classes.Base import BaseModel


class Production(BaseModel):
    __tablename__ = 'PRODUCTION'

    CODE_PRODUCTION = Column(SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    UN = Column(String(20),ForeignKey("UNITE.UN"))
    NOM_PRODUCTION = Column(String(20))