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

    def as_dict(self):
        dict_class = {}
        for c in self.__table__.columns:
            isinstance(getattr(self, c.name), datetime.date)
            if isinstance(getattr(self, c.name), datetime.date):
                dict_class[c.name] = getattr(self, c.name).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, c.name), str):
                dict_class[c.name] = getattr(self, c.name).strip()
            elif isinstance(getattr(self, c.name), decimal.Decimal):
                dict_class[c.name] = float(getattr(self, c.name))
            else:
                dict_class[c.name] = getattr(self, c.name)
        return dict_class
