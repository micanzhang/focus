__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
import time

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'

    id = Column(mysql.INTEGER, primary_key=True)
    username = Column(mysql.VARCHAR(64))
    content = Column(mysql.VARCHAR(255))
    create_time = Column(mysql.INTEGER, default=int(time.time()))

