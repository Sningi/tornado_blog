#!/usr/bin/env python
# coding=utf-8
import os
from tornado.web import RequestHandler
from mariadb.test import generate_articles_list, createart, generate_article, getcate_count
import time
category_dict = {'01': 'Python', '02': 'C/C++', '03': 'Java', '04': 'Android', '05': 'Html/Css/Js',
                 '06': 'Linux/Shell', '07': 'MariaDB', '08': 'Collection', '10': 'Other', '99': 'recommend'}
# bloglist 格式 ——（category） ——（page）


def ls_all_file(filepath, flist):
  # 遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath, fi)
    if os.path.isdir(fi_d):
      ls_all_file(fi_d, flist)
    else:
      flist.append(fi_d[12:])


class HtmlHandler(RequestHandler):
  def get(self):
    # print('HtmlHandler:' + self.request.uri)
    if self.request.uri == '/' or self.request.uri == "/index.html":
      al = generate_articles_list()
      self.render('index.html', articles=al)
    elif self.request.uri[:11] == '/blog_list=':
      cate = category_dict[str(self.request.uri[11:13])]
      basecateurl = str(self.request.uri[:13])
      beforpage = "%02d" % (int(self.request.uri[13:15]) - 1)
      if beforpage == '-1':
        beforpage = '00'
      nextpage = "%02d" % (int(self.request.uri[13:15]) + 1)
      count = getcate_count()
      al = generate_articles_list(
          int(self.request.uri[11:13]), int(self.request.uri[13:15]))
      self.render('bloglist.html', articles=al, count=count,
                  cate=cate, basecateurl=basecateurl, beforpage=beforpage, nextpage=nextpage)
    elif self.request.uri[:12] == '/article_id=':
      basecateurl = str(self.request.uri[:13])
      count = getcate_count()
      data = generate_article(self.request.uri[12:-5])
      cate = category_dict["%02d" % data[5]]
      self.render('article.html', count=count, data=data, cate=cate,
                  basecateurl=basecateurl)
    elif self.request.uri == '/about.html':
      self.render('about.html')
    elif self.request.uri == '/write.html':
      self.render('cke_write.html')
    elif self.request.uri == '/share.html':
      self.render('share.html')
    elif self.request.uri == '/file.html':
      list = []
      ls_all_file('static/file', list)
      self.render('file.html', list=list)
