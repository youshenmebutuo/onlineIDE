from handlers.main import MainHandler
from handlers.websocket import WebSocketHandler
from handlers.fileupload import FileUploadHandler

handlers = [
    (r"/", MainHandler),
    (r'/websocket', WebSocketHandler),
    (r"/file/upload", FileUploadHandler),
]
