__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
import time
import re

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'

    id = Column(mysql.INTEGER, primary_key=True)
    username = Column(mysql.VARCHAR(32))
    author = Column(mysql.VARCHAR(32))
    content = Column(mysql.VARCHAR(255))
    create_time = Column(mysql.INTEGER, default=int(time.time()))

    @staticmethod
    def parse_topic(post_content):
        return re.findall(r'#([^#]+)#',post_content)

    @staticmethod
    def parse_mention(post_content):
        return re.findall(r'@([\w]+)', post_content)
