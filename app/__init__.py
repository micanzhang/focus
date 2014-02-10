__author__ = 'micanzhang'

import web
from app.routes import urls
from app.controller import load_sqla, orm
from app.model.dBSession import DBSession
from app.helper.DBStore import SQLAStore

app = web.application(urls, globals())
app.add_processor(load_sqla)
web.ctx.orm = orm()
session = web.session.Session(app, SQLAStore(DBSession), initializer={'login': 0, 'user': None})