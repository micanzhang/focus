import web
from app.routes import urls

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()