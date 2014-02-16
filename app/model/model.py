__author__ = 'mican'

import json
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def sqla_json(obj):
    if isinstance(obj, Base):
        return json.dumps(obj, default=lambda o:{key.name : getattr(o, key.name) for key in o._sa_class_manager.mapper.mapped_table.columns})
    elif isinstance(obj, list):
        return map(lambda o:sqla_json(o), obj)
    else:
        return False
