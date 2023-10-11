from sqlalchemy import Column, SmallInteger, String, Numeric, ForeignKey, Date

from classes.Base import Base,BaseModel


class Epandre(BaseModel):
    __tablename__ = 'EPANDRE'

    ID_ENGRAIS = Column(SmallInteger, primary_key=True, autoincrement=True)
    NO_PARCELLE = Column(SmallInteger, ForeignKey('PARCELLE.NO_PARCELLE'))
    DATE = Column(Date, ForeignKey('DATE.DATE'))
    QTE_EPANDUE = Column(Numeric)