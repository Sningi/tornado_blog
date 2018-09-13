import pymysql as Mysql
from datetime import datetime
# import tornado_mysql as Mysql
category_dict = {'Python': '1', 'C': '2', 'Java': '3', 'Android': '4', 'Html': '5', 'Linux': '6', 'Mysql': '7', 'Collection': '8', 'Other': '10', 'recommend': '%'
                 }
# 连接数据库
conn = Mysql.connect(host='127.0.0.1', user='sning',
                     passwd='197010', db='blog')


def createart(u_id, title, summary='', key_words='', category='10', image_url='b', content=''):
    fin_image_url = 'static/title_img/' + image_url + '.jpg'
    # 获得一个游标
    cur = conn.cursor()
    # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
    cmd = "Insert into articles values(0,'%s','%s','%s','%s',%s,'%s',0,'%s',0); " % (
        Mysql.escape_string(title), Mysql.escape_string(summary), Mysql.escape_string(content), key_words, category, datetime.now(), fin_image_url)
    countadd = 'update category set sum=sum+1 where id = ' + category + ';'
    try:
        cur.execute(cmd)
        cur.execute(countadd)
        # 提交
        conn.commit()
    except Exception as e:
        # 错误回滚
        print(e)
        conn.rollback()
    # finally:
    #     conn.close()
    return True


def generate_articles_list(category='%', page=0):
    if category == 99:
        category = '%'
    cur = conn.cursor()
    # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
    cmd = 'select image_url,title,summary,Key_words,creatime,read_num,id from articles where category like "' + \
        str(category) + '" order by id desc limit ' + str(page * 8) + ',8;'
    # print(cmd)
    cur.execute(
        'select image_url,title,summary,Key_words,creatime,read_num,id from articles where category like "' + str(category) + '" order by id desc limit ' + str(page * 8) + ',8;')
    # 获取数据库的信息
    data = cur.fetchall()
    return data


def generate_article(id='1'):
    cur = conn.cursor()
    # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
    cur.execute(
        'select title,creatime,read_num,summary,content,category from articles where id=' + id)
    # 获取数据库的信息
    data = cur.fetchone()
    return data


def getcate_count():
    cur = conn.cursor()
    # 执行SQL语句  (返回值是查询表中的行数，影响的行数)
    cur.execute(
        'select sum from category;')
    # 获取数据库的信息
    data = cur.fetchall()
    return data


def file_list():
    pass


if __name__ == '__main__':
    data = getcate_count()
    print(data)
