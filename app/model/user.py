__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
import hashlib
import time

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(mysql.INTEGER, primary_key=True)
    username = Column(mysql.VARCHAR(64))
    _password = Column('password', mysql.VARCHAR(128))
    email = Column(mysql.VARCHAR(64))
    status = Column(mysql.TINYINT, default=0)
    create_time = Column(mysql.INTEGER, default=int(time.time()))
    update_time = Column(mysql.INTEGER, default=int(time.time()))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self.password_hash(value)


    def password_hash(self, value):
        salt = '83071f6280615f2ff970a259d6ce8324'
        if len(value) == 0:
            return value
        else:
            return hashlib.md5(salt + hashlib.md5(value).hexdigest()).hexdigest()

