from application import Application
from tornado.options import options
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

if __name__ == "__main__":
    options.parse_command_line()
    server = HTTPServer(Application())
    server.listen(options['port'])
    IOLoop.current().start()