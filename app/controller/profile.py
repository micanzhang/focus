__author__ = 'micanzhang'

from app.helper import BaseAction
from app.model import User, Post, Mention
import web
from sqlalchemy import and_

class ViewAction(BaseAction):
    def GET(self, username):
        user = web.ctx.orm.query(User).filter(User.username==username).first()
        if not user:
               raise web.notfound

        posts = web.ctx.orm.query(Post).filter(Post.username==username).all()
        mention_posts = web.ctx.orm.query(Post).join(Mention, and_(Post.id==Mention.post_id, Mention.username==username)).all()
        return self.render('profile_view.html', user=user, posts=posts, mention_posts=mention_posts)

