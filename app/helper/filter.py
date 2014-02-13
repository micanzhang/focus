__author__ = 'micanzhang'
import time
from app.model import Post

def strftime(seconds, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.gmtime(seconds))


def decorate(content):
    topics = Post.parse_topic(content)
    mentions = Post.parse_mention(content)
    for topic in topics:
        old = '#{0}#'.format(topic)
        new = '<a href="/topic/{0}" class="topic">{1}</a>'.format(topic, old)
        content = content.replace(old, new)

    for mention in mentions:
        old = '@{0}'.format(mention)
        new = '<a href="/{0}" class="mention">{1}</a>'.format(old, old)
        content = content.replace(old, new)
    return content