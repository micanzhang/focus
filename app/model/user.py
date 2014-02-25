__author__ = 'micanzhang'

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from app.model.model import Base
from sqlalchemy.ext.hybrid import hybrid_property
import hashlib
import time
import web
from app.constants import Roles


class User(Base):
    __tablename__ = 'user'

    id = Column(mysql.INTEGER, primary_key=True)
    username = Column(mysql.VARCHAR(32))
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

    def login(self):
        session = web.config._session
        if session.login > Roles.GUEST:
            return 0

        if self.id:
            session.login = Roles.AUTHROIZED
            session.user = self
            return 0

        user = web.ctx.orm.query(User).filter(User.email==self.email).first()
        if user:
            if user.password == self.password:
                session.login = Roles.AUTHROIZED
                session.user = user
                return 0
            else:
                return 1    #password is invalid
        else:
            return 2    #user doesn't exists


    def is_guest(self):
        pass

    def logout(self):
        pass