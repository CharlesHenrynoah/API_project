import datetime
import decimal
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.upper()

    def as_dict(self, fields=None):
        dict_class = {}

        for c in self.__table__.columns:
            value = getattr(self, c.name)
            if isinstance(value, datetime.date):
                dict_class[c.name] = value.strftime('%Y-%m-%d')
            elif isinstance(value, str):
                dict_class[c.name] = value.strip()
            elif isinstance(value, decimal.Decimal):
                dict_class[c.name] = float(value)
            else:
                dict_class[c.name] = value
        return dict_class
