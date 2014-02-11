__author__ = 'micanzhang'

from app.helper import BaseAction
from app.model import Post, PostTopic, Mention, User
import web
import time

class PostAction(BaseAction):
    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        return self.render('post_index.html', posts=posts)

    def POST(self):
        data = web.input()
        if not data or not data.has_key('content') or len(data['content']) == 0:
            return "invalid post."

        content = data['content']
        p = Post(
            username=self.session.user.username,
            content=content,
            create_time=int(time.time())
        )

        topics = Post.parse_topic(content)
        if not topics or len(topics) == 0:
            raise web.notfound

        web.ctx.orm.add(p)
        web.ctx.orm.flush()

        for topic in topics:
            post_topic = PostTopic(
                post_id=p.id,
                topic=topic
            )
            web.ctx.orm.add(post_topic)

        mentions = Post.parse_mention(content)
        users = web.ctx.orm.query(User).filter(User.username.in_(mentions)).all()
        for user in users:
             mention = Mention(
                 username=user.username,
                 post_id=p.id
             )
             web.ctx.orm.add(mention)

        web.seeother('/post')

