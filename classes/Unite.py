from sqlalchemy import String, Column

from classes.Base import BaseModel


class Unite(BaseModel):
    __tablename__ = 'UNITE'

    UN = Column(String(20), primary_key=True, nullable=False)
