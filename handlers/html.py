import os
import time
from tornado.web import RequestHandler
from mariadb.dboperate import *


"""



"""
category_dict = {'01': 'Python', '02': 'C/C++', '03': 'Java', '04': 'Android', '05': 'Web',
                 '06': 'Linux', '07': 'MariaDB', '08': '收 藏', '10': 'Other', '99': '推 荐'}


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
    if self.request.uri == '/' or self.request.uri == "/index.html":
      article_list = MariaDB.get_article_list()
      max_read_arts = MariaDB.max_read_articles()
      self.render('index.html', articles=article_list, paihang=max_read_arts)

    elif self.request.uri[:11] == '/blog_list=':
      cate = category_dict[str(self.request.uri[11:13])]
      basecateurl = str(self.request.uri[:13])
      beforpage = "%02d" % (int(self.request.uri[13:15]) - 1)
      if beforpage == '-1':
        beforpage = '00'
      nextpage = "%02d" % (int(self.request.uri[13:15]) + 1)
      categorys = MariaDB.get_category_info()
      al = MariaDB.get_article_list(
          int(self.request.uri[11:13]), int(self.request.uri[13:15]))
      max_read_arts = MariaDB.max_read_articles()
      self.render('bloglist.html', articles=al, categorys=categorys,
                  cate=cate, top_cateurl=basecateurl + "00.html", basecateurl=basecateurl, beforpage=beforpage, nextpage=nextpage, paihang=max_read_arts)

    elif self.request.uri[:12] == '/article_id=':
      basecateurl = str(self.request.uri[:13])
      categorys = MariaDB.get_category_info()
      data = MariaDB.get_article(self.request.uri[12:-5])
      cate = category_dict["%02d" % data[5]]
      max_read_arts = MariaDB.max_read_articles()
      self.render('article.html', categorys=categorys, data=data, cate=cate,
                  top_cateurl="blog_list=" + str("%02d" % data[5]) + "00.html", paihang=max_read_arts)
      MariaDB.read_num_increase(self.request.uri[12:-5])

    # 搜索处理
    elif self.request.uri[:7] == '/search':
      beforpage = "%02d" % (int(self.request.uri[7:9]) - 1)
      if beforpage == '-1':
        beforpage = '00'
      nextpage = "%02d" % (int(self.request.uri[7:9]) + 1)
      categorys = MariaDB.get_category_info()
      al = MariaDB.get_search_article_list(
          self.get_argument('key', self.request.uri[7:9]))
      max_read_arts = MariaDB.max_read_articles()
      self.render('bloglist.html', articles=al, categorys=categorys,
                  cate="搜 索", top_cateurl="", basecateurl="search", beforpage=beforpage, nextpage=nextpage, paihang=max_read_arts)

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
