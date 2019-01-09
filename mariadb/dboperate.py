import pymysql as Mysql
from datetime import datetime

"""  
time:2018年12月25日  
  
@author: sning
"""


class Database(object):
    """数据库操作类"""

    def __init__(self):
        self.con = Mysql.connect(
            host='127.0.0.1', user='sning', passwd='197010', db='blog')
        self.cur = self.con.cursor()
        self.category_change = True
        self.category_info = ()

    def get_category_info(self):
        if self.category_change:
            self.cur.execute("select sum,id,name from category")
            self.category_info = self.cur.fetchall()
            self.category_change = False
        return self.category_info

    def insert_article(self, u_id, title, summary='', key_words='', category='10', content=''):
        # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
        cmd = "Insert into articles values(0,'%s','%s','%s','%s',%s,'%s',0,0); " % (
            Mysql.escape_string(title), Mysql.escape_string(summary), Mysql.escape_string(content), key_words, category, datetime.now())
        countadd = 'update category set sum=sum+1 where id = ' + category + ';'
        try:
            self.cur.execute(cmd)
            self.cur.execute(countadd)
            # 提交
            self.con.commit()
        except Exception as e:
            # 错误回滚
            print(e)
            self.con.rollback()
        self.category_change = True
        return True

    def get_article_list(self, category='%', page=0):
        if category == 99:
            category = '%'
        self.cur.execute('select id,title,summary,Key_words,creatime,read_num from articles where category like "' +
                         str(category) + '" order by id desc limit ' + str(page * 8) + ',8')
        return self.cur.fetchall()

    def get_article(self, id='1'):
        self.cur.execute(
            'select title,creatime,read_num,summary,content,category from articles where id=' + id)
        return self.cur.fetchone()

    def max_read_articles(self):
        self.cur.execute(
            'select id,title,summary from articles order by read_num desc limit 0,4')
        return self.cur.fetchall()

    def read_num_increase(self, article_id):
        self.cur.execute(
            'update articles set read_num=read_num+1 where id=' + article_id)
        self.con.commit()

    def get_search_article_list(self, key="%", page=0):
        self.cur.execute('select id,title,summary,Key_words,creatime,read_num from articles where Key_words like "%' +
                         str(key) + '%" order by id desc limit ' + str(page * 8) + ',8')
        return self.cur.fetchall()


MariaDB = Database()

# # 连接数据库
# conn = Mysql.connect(host='127.0.0.1', user='sning',
#                      passwd='197010', db='blog')
# # 获得一个游标
# cur = conn.cursor()
# def insert_article(u_id, title, summary='', key_words='', category='10', image_url='b', content=''):
#     fin_image_url = 'static/title_img/' + image_url + '.jpg'
#     # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
#     cmd = "Insert into articles values(0,'%s','%s','%s','%s',%s,'%s',0,'%s',0); " % (
#         Mysql.escape_string(title), Mysql.escape_string(summary), Mysql.escape_string(content), key_words, category, datetime.now(), fin_image_url)
#     countadd = 'update category set sum=sum+1 where id = ' + category + ';'
#     try:
#         cur.execute(cmd)
#         cur.execute(countadd)
#         # 提交
#         conn.commit()
#     except Exception as e:
#         # 错误回滚
#         print(e)
#         conn.rollback()
#     return True

# def get_article_list(category='%', page=0):
#     if category == 99:
#         category = '%'
#     cur.execute('select image_url,title,summary,Key_words,creatime,read_num,id from articles where category like "' +
#                 str(category) + '" order by id desc limit ' + str(page * 8) + ',8')
#     data = cur.fetchall()
#     return data


# def get_article(id='1'):
#     cur.execute(
#         'select title,creatime,read_num,summary,content,category from articles where id=' + id)
#     data = cur.fetchone()
#     return data


# def get_cate_count():
#     cur.execute('select sum from category')
#     data = cur.fetchall()
#     return data


# def max_read_articles():
#     cur.execute(
#         'select image_url,title,summary,id from articles order by read_num desc limit 0,4')
#     data = cur.fetchall()
#     return data


# def read_num_increase(article_id):
#     cur.execute('update articles set read_num=read_num+1 where id=' + article_id)
#     conn.commit()


# def get_search_article_list(key="%", page=0):
#     cur.execute('select image_url,title,summary,Key_words,creatime,read_num,id from articles where Key_words like "%' +
#                 str(key) + '%" order by id desc limit ' + str(page * 8) + ',8')
#     data = cur.fetchall()
#     return data


if __name__ == '__main__':
    db = Database()
    print(db.get_category_info())
