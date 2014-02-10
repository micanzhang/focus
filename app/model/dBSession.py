__author__ = 'micanzhang'

import datetime
from sqlalchemy import Column
from sqlalchemy.dialects import mysql

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBSession(Base):
    __tablename__ = 'session'

    session_id = Column(mysql.CHAR(128), nullable=False, unique=True, primary_key=True)
    atime = Column(mysql.DATETIME, default=datetime.datetime.now())
    data = Column(mysql.TEXT, nullable=True)
