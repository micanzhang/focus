__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
import time
from app.model.model import Base

class Follow(Base):
    __tablename__ = 'follow'

    id = Column(mysql.INTEGER, primary_key=True)
    follower = Column(mysql.VARCHAR(32))
    following = Column(mysql.VARCHAR(32))
    create_time = Column(mysql.INTEGER, default=int(time.time()))