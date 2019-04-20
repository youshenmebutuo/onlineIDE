import json

import tornado.ioloop
import tornado.web
import os
import tornado.websocket
import tornado.escape
import subprocess
from ide_settings import Settings
import ide_functions

app_settings: Settings = Settings()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        return None

    def on_message(self, message):
        message = tornado.escape.json_decode(message)
        if message['task'] == 'compile':
            (err_output, std_output) = \
                ide_functions.compile(app_settings.dir_path, message['data'], message['filename'])
            self.write_message("成功上传代码至服务器")
            self.write_message(std_output)
            self.write_message(err_output)
        elif message['task'] == 'start':
            (err_output, std_output) = ide_functions.start(app_settings.dir_path, message['filename'])
            self.write_message(std_output)
            self.write_message(err_output)

    def on_close(self):
        return None

class FileUploadHandler(tornado.web.RequestHandler):
    async def post(self):
        file_metas = self.request.files.get('fileContent', None)  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            file_path = os.path.join(app_settings.dir_path, filename)
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            self.write(json.loads(ide_functions.open_file(app_settings.dir_path, filename)))



def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }  # 配置静态文件路径
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/websocket', WebSocketHandler),
        (r"/file/upload", FileUploadHandler),
    ], **settings)


def main():
    app = make_app()
    # app.listen(port=app_settings.port, address="172.19.114.167")
    app.listen(port=app_settings.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
