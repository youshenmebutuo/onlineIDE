import tornado.web
from config import settings
from urls import handlers

class Application(tornado.web.Application):
    def __init__(self, db=None):
        self.c_proc = None
        super(Application, self).__init__(handlers, **settings)