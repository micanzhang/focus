from app.controller import render

class IndexAction:
    def GET(self):
        return render("index.html")
