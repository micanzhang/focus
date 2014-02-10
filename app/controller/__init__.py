__author__ = 'micanzhang'

import os
import web
from jinja2 import Environment,FileSystemLoader

def render(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    template_dir =  os.path.join(os.path.dirname(__file__), '../view');

    jinja_env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../view')),
        extensions = extensions,
        )

    jinja_env.globals = globals.update(globals)
    return jinja_env.get_template(template_name).render(context)