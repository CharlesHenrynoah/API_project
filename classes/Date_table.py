from sqlalchemy import Column, Date

from classes.Base import *


class DateTable(BaseModel):  # Renamed class because 'Date' is a reserved keyword
    __tablename__ = 'DATE'

    DATE = Column(Date, primary_key=True, autoincrement=True)
