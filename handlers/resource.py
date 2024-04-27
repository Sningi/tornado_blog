import os
import json
import time
from tornado.web import RequestHandler
from mariadb.dboperate import MariaDB


class ResourceHandler(RequestHandler):
    """文件资源处理"""

    def get(self):
        print('ResourceHandler', self.request.uri)
        try:
            self.write(open('static' + self.request.uri, 'rb').read())
        except FileNotFoundError:
            self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.write('404 Not Found')
        else:
            self.write('error:' + str(status_code))


class ImageHandler(RequestHandler):
    """CKeditor 图片上传功能代码"""

    def post(self):
        file_metas = self.request.files.get(
            'upload', None)  # 提取表单中‘name’为‘file’的文件元数据
        filename = ''
        for meta in file_metas:
            filename = meta['filename']
            file_path = 'static/blog_img/' + filename

            with open(file_path, 'wb') as up:
                up.write(meta['body'])
            print('save finish')
        print("file")
        json_res = {
            "uploaded": True,
            "url": 'static/blog_img/' + filename
        }
        self.write(json_res)
        self.flush()


class CreateHandler(RequestHandler):
    """添加文章处理"""

    def post(self):
        u_id = str(self.get_argument('u_id'))
        title = str(self.get_argument('title'))
        key_words = str(self.get_argument('key_words'))
        category = str(self.get_argument('category'))
        # image_url = str(self.get_argument('image_url'))
        summary = str(self.get_argument('summary'))
        content = str(self.get_argument('content'))
        if(MariaDB.insert_article(u_id, title, summary, key_words, category, content)):
            print("articles insert finish")
        else:
            self.set_status(201)
            self.flush()


class FileHandler(RequestHandler):
    """上传文件接收"""

    def post(self):
        file_metas = self.request.files.get(
            'file', None)  # 提取表单中‘name’为‘file’的文件元数据

        if not file_metas:
            self.set_status(201)
            return

        for meta in file_metas:
            filename = meta['filename']
            file_path = 'static/file/' + filename
            if os.path.exists(file_path):
                file_path = file_path + '_' + \
                    time.strftime("%Y-%m-%d %H:%M:%S")
            with open(file_path, 'wb') as up:
                up.write(meta['body'])
        self.set_status(200)
        self.flush()
