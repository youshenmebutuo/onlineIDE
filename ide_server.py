import tornado.ioloop
import tornado.web
import os
import tornado.websocket
import tornado.escape
import subprocess
from ide_settings import Settings
import ide_functions

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        return None

    def on_message(self, message):
        message = tornado.escape.json_decode(message)
        file_path = os.getcwd() + "/files/source.cpp"
        output_path = os.getcwd() + "/files/source.out"
        if message['task'] == 'compile':
            (err_output, std_output) = ide_functions.compile(file_path, message, output_path)
            self.write_message("成功上传代码至服务器")
            self.write_message(std_output)
            self.write_message(err_output)
        elif message['task'] == 'start':
            proc = ide_functions.start()

    def on_close(self):
        return None


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }  # 配置静态文件路径
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/websocket', WebSocketHandler),
    ], **settings)


def main():
    app = make_app()
    app_settings: Settings = Settings()
    app.listen(app_settings.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
