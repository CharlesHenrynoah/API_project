from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date

from classes.Base import Base,BaseModel


class Epandre(BaseModel):
    __tablename__ = 'EPANDRE'

    ID_ENGRAIS = Column(Integer, primary_key=True)
    NO_PARCELLE = Column(Integer, ForeignKey('PARCELLE.NO_PARCELLE'))
    DATE = Column(Date, ForeignKey('DATE.DATE'))
    QTE_EPANDUE = Column(Numeric)