from app.model import Post, User
from app.helper import BaseAction
from app.constants import Roles
import web



class IndexAction(BaseAction):
    access_role = Roles.GUEST

    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        return self.render("index.html")

class SignInAction(BaseAction):
    def access_filter(self):
        if self.role > Roles.GUEST:
            web.seeother('/profile')


    def GET(self):
        return self.render('signin.html')

    def POST(self):
        data = web.input()
        user = web.ctx.orm.query(User).filter(User.email==data.email).first()
        if user and user.password == user.password_hash(data.password):
            self.session.login = 1
            self.session.user = user
            return web.seeother('/')
        else:
            return self.render('signin.html')

class SignUpAction:
    def access_filter(self):
        if self.role > Roles.GUEST:
            web.seeother('/profile')

    def GET(self):
        return self.render('signup.html')

    def POST(self):
        data = web.input()
        user = User(
            username=data.username,
            email=data.email,
            password=data.password
        )

        if web.ctx.orm.add(user):
            return web.seeother('/')

        return self.render('signup.html')

class SignOutAction:
    def GET(self):
        self.session.login = Roles.GUEST
        self.session.user = None
        return web.seeother('/signin')

