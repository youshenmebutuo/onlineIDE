import tornado.escape
import tornado.websocket
from libs import ide_functions
from tornado.options import options


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        return None

    def on_message(self, message):
        message = tornado.escape.json_decode(message)
        if message['task'] == 'compile':
            (err_output, std_output) = \
                ide_functions.compile(options['file_dir_path'], message['data'], message['filename'])
            self.write_message("成功上传代码至服务器\n")
            self.write_message(std_output)
            self.write_message(err_output)
        elif message['task'] == 'start':
            self.c_proc = ide_functions.start(options['file_dir_path'], message['filename'])
        elif message['task'] == 'args':
            try:
                (err_output, std_output) = self.c_proc.communicate(input=message['data'].encode('utf-8'))
                self.write_message(std_output)
                self.write_message(err_output)
            except:
                self.write_message('目前没有程序在运行\n')

    def on_close(self):
        return None