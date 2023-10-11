from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Date, SmallInteger
from sqlalchemy.orm import relationship

from classes.Base import Base, BaseModel


class Culture(BaseModel):
    __tablename__ = 'CULTURE'

    IDENTIFIANT_CULTURE = Column(SmallInteger, primary_key=True, autoincrement=True)
    NO_PARCELLE = Column(SmallInteger)
    CODE_PRODUCTION = Column(SmallInteger)
    DATE_DEBUT = Column(Date)
    DATE_FIN = Column(Date)
    QTE_RECOLTEE = Column(Numeric)


