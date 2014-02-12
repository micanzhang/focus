__author__ = 'micanzhang'

from app.model import Post, PostTopic
from app.helper import BaseAction
from app.constants import Roles
import web

class ListAction(BaseAction):
    def GET(self):
        topics = web.ctx.orm.query(PostTopic.topic).distinct()
        return self.render('topic_list.html', topics=topics)

class ViewAction(BaseAction):
    def GET(self, topic_content):
        #if topic_content exists
        post_topics = web.ctx.orm.query(PostTopic).filter(PostTopic.topic==topic_content).all()
        posts_id = []
        for post_topic in post_topics:
            posts_id.append(post_topic.post_id)

        posts = web.ctx.orm.query(Post).filter(Post.id.in_(posts_id)).all()

        return self.render('topic_view.html', posts=posts)
