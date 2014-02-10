__author__ = 'micanzhang'

from app.controller import render
from app.model.post import Post
import web
import time

class PostAction:
    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        return render('post_index.html', posts=posts)

    def POST(self):
        data = web.input()
        if not data or not data.has_key('content') or len(data['content']) == 0:
            return "invalid post."

        content = data['content']
        p = Post(content=content, create_time=int(time.time()))
        web.ctx.orm.add(p)
        web.seeother('/post')

