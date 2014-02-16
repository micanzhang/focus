__author__ = 'micanzhang'

from app.helper import BaseAction, ApiAction
from app.model import Post, PostTopic, Mention, User, postGeo
import web
import time
from app.model.model import sqla_json

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
            author=self.session.user.username,
            content=content,
            create_time=int(time.time())
        )

        topics = Post.parse_topic(content)
        if not topics or len(topics) == 0:
            raise web.notfound

        web.ctx.orm.add(p)
        web.ctx.orm.flush()

        if 'position' in data:
            geodata = data.position.split(',')
            (lat, lng) = geodata if len(geodata) == 2 else (None, None)
            if lat and lng:
                geo = postGeo(
                    post_id=p.id,
                    lat=lat,
                    lng=lng
                )
                web.ctx.orm.add(geo)


        for topic in topics:
            post_topic = PostTopic(
                post_id=p.id,
                topic=topic
            )
            web.ctx.orm.add(post_topic)

        mentions = Post.parse_mention(content)
        users = web.ctx.orm.query(User).filter(User.username.in_(mentions)).all() if len(mentions) > 0 else []
        for user in users:
             mention = Mention(
                 username=user.username,
                 post_id=p.id
             )
             web.ctx.orm.add(mention)

        return web.seeother('/post')

class RePostAction(BaseAction):
    def POST(self, id):
        username = self.session.user.username
        post = web.ctx.orm.query(Post).filter(Post.id==id).first()
        if post:
            n_post = Post(
                username=username,
                author=post.username,
                content=post.content
            )

            web.ctx.orm.add(n_post)
            return web.seeother('/post')
        else:
            return web.internalerror()


class CreateAction(ApiAction):
    def POST(self):
        return self.render()

class ReadAction(ApiAction):
    def GET(self, id):
        post = web.ctx.orm.query(Post).filter(Post.id==id).first()
        print sqla_json(post)
        if post:
            print post._sa_class_manager.mapper.mapped_table.columns
            print {key.name: getattr(post, key.name) for key in post._sa_class_manager.mapper.mapped_table.columns} #post.__dict__
        return self.render()

class DeleteAction(ApiAction):
    def POST(self, id):
        return self.render()

class ListAction(ApiAction):
    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        self.response.data = sqla_json(posts)
        return self.render()