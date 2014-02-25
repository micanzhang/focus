__author__ = 'micanzhang'

import web
from sqlalchemy.orm import scoped_session, sessionmaker
from baseAction import BaseAction, ApiAction
from sqlalchemy import create_engine
from app.constants import DB_USERNAME, DB_HOST, DB_NAME, DB_PASSWORD
from DBStore import SQLAStore

# mysql connection string
engine_url = 'mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
engine = create_engine(engine_url)

def load_sqla(handler):
    web.ctx.orm = orm()
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()


def orm():
    return scoped_session(sessionmaker(bind=engine))


