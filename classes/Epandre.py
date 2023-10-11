from sqlalchemy import Column, SmallInteger, String, Numeric, ForeignKey, Date

from classes.Base import Base, BaseModel


class Epandre(BaseModel):
    __tablename__ = 'EPANDRE'

    ID_ENGRAIS = Column(SmallInteger, ForeignKey('ENGRAIS.ID_ENGRAIS'), primary_key=True, nullable=False)
    NO_PARCELLE = Column(SmallInteger, ForeignKey('PARCELLE.NO_PARCELLE'), primary_key=True, nullable=False)
    DATE = Column(Date, ForeignKey('DATE.DATE'), primary_key=True, nullable=False)
    QTE_EPANDUE = Column(Numeric)
