import os
from tornado.options import define

BASE_DIRS = os.path.dirname(__file__)

define("port", default=8888, help="run on the given port", type=int)
define("file_dir_path", default="files", help="save file in the directory", type=str)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    autoreload=True
)