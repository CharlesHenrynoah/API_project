from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Date, SmallInteger
from sqlalchemy.orm import relationship

from classes.Base import Base, BaseModel


class Culture(BaseModel):
    __tablename__ = 'CULTURE'

    IDENTIFIANT_CULTURE = Column(SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    NO_PARCELLE = Column(SmallInteger, ForeignKey("PARCELLE.NO_PARCELLE"))
    CODE_PRODUCTION = Column(SmallInteger, ForeignKey('PRODUCTION.CODE_PRODUCTION'))
    DATE_DEBUT = Column(Date)
    DATE_FIN = Column(Date)
    QTE_RECOLTEE = Column(Numeric)


