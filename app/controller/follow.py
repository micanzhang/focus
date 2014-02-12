__author__ = 'micanzhang'

from app.helper import BaseAction
from app.model import Follow
from app.constants import Response, ResponseStatus
import web

class FollowAction(BaseAction):
    def POST(self, following):
        follower = self.session.user.username
        exists = web.ctx.orm.query(Follow).filter(follower==follower,following==following).first()
        if exists:
            error = ResponseStatus.STATUS_REPEAT_REQUEST
            msg = 'You have followed ' + follower + ' aleardy!'
            return Response(error=error, msg=msg).json()

        follow = Follow(
            following=following,
            follower=follower
        )
        web.ctx.orm.add(follow)
        return Response().json()


class UnFollowAction(BaseAction):
    def POST(self, following):
        follower = self.session.user.username
        following = web.ctx.orm.query(Follow).filter(following==following,follower==follower).first()
        print following
        if following:
            web.ctx.orm.delete(following)
            return Response().json()
        else:
            error = ResponseStatus.STATUS_BAD_REQUEST
            msg = 'You can not cancel follow the one you didnot followed'
            return Response(error=error, msg=msg).json()

class FollowerAction(BaseAction):
    def GET(self, following):
        followers = web.ctx.orm.query(Follow).filter(following==following).all()
        return followers

class FollowingAction(BaseAction):
    def GET(self, follower):
        followings = web.ctx.orm.query(Follow).filter(follower==follower).all()
        return followings


