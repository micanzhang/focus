__author__ = 'micanzhang'

import web
from app.routes import urls
from app.model import DBSession
from app.helper import load_sqla, orm, SQLAStore


# web.py application instance
app = web.application(urls, globals())
app.add_processor(load_sqla)
web.ctx.orm = orm()
if web.config.get('_session') is None:
    web.config._session = web.session.Session(app, SQLAStore(DBSession), initializer={'login': 0, 'user': None})




