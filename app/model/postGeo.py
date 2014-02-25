__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from app.model.model import Base

class PostGeo(Base):
    __tablename__ = 'post_geo'

    post_id = Column(mysql.INTEGER, primary_key=True)
    lat = Column(mysql.FLOAT(10, 6))
    lng = Column(mysql.FLOAT(10, 6))
    address = Column(mysql.VARCHAR(255))
