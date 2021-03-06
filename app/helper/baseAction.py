__author__ = 'micanzhang'

import web
import os
from app.constants import Roles
from jinja2 import Environment,FileSystemLoader
from app.helper import filter
from app.constants import ResponseStatus, Response

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
        globals['ctx'] = web.ctx
        globals['session'] = self.session

        jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../view')),
            extensions=extensions,
        )
        jinja_env.globals.update(globals)
        jinja_env.filters['strftime'] = filter.strftime
        jinja_env.filters['decorate'] = filter.decorate
        return jinja_env.get_template(template_name).render(context)


class ApiAction(BaseAction):
    def __init__(self):
        BaseAction.__init__(self)
        self.response = Response()

    def render(self):
        return self.response.json()
