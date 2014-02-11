__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mention(Base):
    __tablename__ = 'mention'

    id = Column(mysql.INTEGER, primary_key=True)
    username = Column(mysql.VARCHAR(32))
    post_id = Column(mysql.INTEGER)