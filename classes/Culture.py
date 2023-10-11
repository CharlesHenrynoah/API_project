from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Date, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from classes.Base import Base, BaseModel


class Culture(BaseModel):
    __tablename__ = 'CULTURE'

    IDENTIFIANT_CULTURE = Column(Integer, primary_key=True)
    NO_PARCELLE = Column(Integer)
    CODE_PRODUCTION = Column(Integer)
    DATE_DEBUT = Column(Date)
    DATE_FIN = Column(Date)
    QTE_RECOLTEE = Column(Numeric)


