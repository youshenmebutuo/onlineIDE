import json
import os
import tornado.web
from libs import ide_functions
from tornado.options import options



class FileUploadHandler(tornado.web.RequestHandler):
    async def post(self):
        file_metas = self.request.files.get('fileContent', None)  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            file_path = options['file_dir_path'] + '/' + meta['filename']
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            self.write(json.loads(ide_functions.open_file(options['file_dir_path'], meta['filename'])))