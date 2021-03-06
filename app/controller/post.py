__author__ = 'micanzhang'

from app.helper import BaseAction, ApiAction
from app.model import Post, PostTopic, Mention, User, PostGeo

import web
import time
from app.model.model import sqla_json
from app.constants import ResponseStatus
from sqlalchemy import desc

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


class ListCreateAction(ApiAction):
    def GET(self):
        params = web.input(offset=0,limit=20)
        posts = web.ctx.orm.query(Post) \
            .order_by(desc(Post.id)) \
            .offset(params['offset']) \
            .limit(params['limit']) \
            .all()
        self.response.data = sqla_json(posts)
        return self.render()

    def POST(self):
        data = web.input()
        if not data or not data.has_key('content') or len(data['content']) == 0:
            self.response.error = ResponseStatus.STATUS_INCORRECT_PARAMS
            self.response.msg = "invalid parameters"
            return self.render()


        content = data['content']
        p = Post(
            username=self.session.user.username,
            author=self.session.user.username,
            content=content,
            create_time=int(time.time())
        )

        topics = Post.parse_topic(content)
        if not topics or len(topics) == 0:
            self.response.error = ResponseStatus.STATUS_INCORRECT_PARAMS
            self.response.msg = "missing topic"
            return self.render()

        web.ctx.orm.add(p)
        web.ctx.orm.flush()

        if 'position' in data and 'address' in data:
            geodata = data.position.split(',')
            (lat, lng) = geodata if len(geodata) == 2 else (None, None)
            if lat and lng and data.address:
                geo = PostGeo(
                    post_id=p.id,
                    lat=lat,
                    lng=lng,
                    address=data.address
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

        return self.render()

class ReadUpdateAction(ApiAction):
    def GET(self, id):
        post = web.ctx.orm.query(Post).get(id)
        if post:
            self.response.data = sqla_json(post)
        else:
            self.response.error = ResponseStatus.STATUS_NOT_FOUND
            self.response.msg = "Post not Found."
        return self.render()

class DeleteAction(ApiAction):
    def POST(self, id):
        #delete post
        post = web.ctx.orm.query(Post).get(id)

        if post:
            if post.username == self.session.user.username:
                web.ctx.orm.delete(post)
                #delete post_topic
                web.ctx.orm.query(PostTopic).filter(PostTopic.post_id==id).delete()
                #delete post_geo
                web.ctx.orm.query(PostGeo).filter(PostGeo.post_id==id).delete()
                #delete mention
                web.ctx.orm.query(Mention).filter(Mention.post_id==id).delete()
            else:
                self.response.error = ResponseStatus.STATUS_AUTH_FAILED
                self.response.msg = "Forbidden"
        else:
            self.response.error = ResponseStatus.STATUS_NOT_FOUND
            self.response.msg = "Post not found"

        return self.render()
