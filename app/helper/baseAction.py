__author__ = 'micanzhang'

import web
import os
from app.constants import Roles
from jinja2 import Environment,FileSystemLoader

class BaseAction:
    access_role = Roles.AUTHROIZED

    def __init__(self):
        self.session = web.config._session
        self.role = self.session.login
        self.access_filter()

    def access_filter(self):
        if self.access_role > self.role:
            return web.seeother('/signin')

    def render(self, template_name, **context):
        extensions = context.pop('extensions', [])
        globals = context.pop('globals', {})

        jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../view')),
            extensions=extensions,
        )

        jinja_env.globals = globals.update(globals)
        return jinja_env.get_template(template_name).render(context)
