from handlers.main import MainHandler
from handlers.websocket import WebSocketHandler
from handlers.fileupload import FileUploadHandler
from handlers.xterm import XtermHandler
from terminado import TermSocket, SingleTermManager

handlers = [
    (r"/", MainHandler),
    (r"/xterm", XtermHandler),
    (r'/websocket', WebSocketHandler),
    (r"/file/upload", FileUploadHandler),
    (r"/terminal", TermSocket, {'term_manager': SingleTermManager(shell_command=['bash'])})
]
