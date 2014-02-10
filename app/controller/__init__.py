__author__ = 'micanzhang'

import os
import web
from sqlalchemy.orm import scoped_session, sessionmaker
from app.model import engine
from jinja2 import Environment,FileSystemLoader

def render(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    #template_dir =  os.path.join(os.path.dirname(__file__), '../view');

    jinja_env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../view')),
        extensions = extensions,
        )

    jinja_env.globals = globals.update(globals)
    return jinja_env.get_template(template_name).render(context)

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