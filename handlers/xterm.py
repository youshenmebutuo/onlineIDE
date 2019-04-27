import tornado.web

class XtermHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("xterm.html")