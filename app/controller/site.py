from app.controller import render
from app.model.post import Post
from app.model.user import User
import web
from app import session

class IndexAction:
    def GET(self):
        posts = web.ctx.orm.query(Post).all()
        dir(posts)
        return render("index.html")

class SignInAction:
    def __init__(self):
        if 1 == session.login:
            web.seeother('/profile')


    def GET(self):
        return render('signin.html')

    def POST(self):
        data = web.input()
        user = web.ctx.orm.query(User).filter(User.email==data.email).first()
        if user and user.password == user.password_hash(data.password):
            session.login = 1
            session.user = user
            return web.seeother('/')
        else:
            return render('signin.html')

class SignUpAction:
    def __init__(self):
        if 1 == session.login:
            web.seeother('/profile')

    def GET(self):
        return render('signup.html')

    def POST(self):
        data = web.input()
        print data.password
        user = User(
            username=data.username,
            email=data.email,
            password=data.password
        )

        if web.ctx.orm.add(user):
            return web.seeother('/')

        return render('signup.html')

class SignOutAction:
    def GET(self):
        if 1== session.login:
            session.login = 0
            session.user = None
        return web.seeother('/signin')

