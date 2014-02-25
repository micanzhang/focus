from app.model import Post, User, postGeo
from app.helper import BaseAction
from app.constants import Roles
import web
from sqlalchemy import literal_column



class IndexAction(BaseAction):
    access_role = Roles.GUEST

    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        return self.render("index.html")

class SignInAction(BaseAction):
    def access_filter(self):
        if self.role > Roles.GUEST:
            return web.seeother('/@' + self.session.user.username)


    def GET(self):
        return self.render('signin.html')

    def POST(self):
        data = web.input()
        user = User(
            email=data.email,
            password=data.password
        )

        login_response = user.login()
        if login_response == 0:
            return web.seeother('/@'+self.session.user.username)
        else:
            return self.render('signin.html',error=login_response)

class SignUpAction(BaseAction):
    def access_filter(self):
        if self.role > Roles.GUEST:
            return web.seeother('/@' + self.session.user.username)

    def GET(self):
        return self.render('signup.html')

    def POST(self):
        data = web.input()
        user = User(
            username=data.username,
            email=data.email,
            password=data.password
        )

        web.ctx.orm.add(user)
        web.ctx.orm.commit()
        if user.id and user.login() == 0:
            return web.seeother('/@'+user.username)

        return self.render('signup.html')

class SignOutAction(BaseAction):
    def GET(self):
        self.session.login = Roles.GUEST
        self.session.user = None
        return web.seeother('/signin')


class TestAction(BaseAction):
    def GET(self):
        return self.render('test.html')
        # lat = 31.202408
        # lng = 121.586972
        # R = 6371    #3959
        # radius = 25
        # WA = 'radians({0})'.format(lat)
        # JA = 'radians({0})'.format(lng)
        # WB = 'radians(lat)'
        # JB = 'radians(lng)'
        #
        # #acos(cos(WA)cos(WB)cos(JB-JA) + sin(WA)sin(WB))
        # distance='{0} * acos(cos({1}) * cos({2}) * cos({3} - {4}) + sin({5}) * sin({6}))'.format(R, WA, WB, JB, JA, WA, WB)
        # sql = 'SELECT post_id, {0} AS distance FROM post_geo HAVING distance < {1} ORDER BY distance LIMIT 0 , 20;'.format(distance, radius)
        # data = web.ctx.orm.query(PostGeo).from_statement(sql).all()
        # print data


