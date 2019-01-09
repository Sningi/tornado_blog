## 1、博客展示
#### 首页
![首页](https://github.com/Sningi/tornado-blog/blob/master/showpic/pindex.png)
#### 详情
![详情](https://github.com/Sningi/tornado-blog/blob/master/showpic/partcile.png)
#### 列表
![列表](https://github.com/Sningi/tornado-blog/blob/master/showpic/pbloglist.png)
#### 项目分享
![项目分享](https://github.com/Sningi/tornado-blog/blob/master/showpic/pshare.png)
#### 文件
![文件](https://github.com/Sningi/tornado-blog/blob/master/showpic/pfile.png)
#### 关于
![关于](https://github.com/Sningi/tornado-blog/blob/master/showpic/pabout.png)

## 2、数据库初始化 Init database
    **detail see the init_mariadb.sql**
'''
    MariaDB [blog]> show tables;
    +----------------+
    | Tables_in_blog |
    +----------------+
    | articles       |
    | category       |
    | users          |
    +----------------+
    <br>
    MariaDB [blog]> select * from category;
    +----+---------------+------+
    | id | name          | sum  |
    +----+---------------+------+
    |  1 | Python        |    1 |
    |  2 | C/C++         |    0 |
    |  3 | Java          |    0 |
    |  4 | Android       |    2 |
    |  5 | Html/Css/Js   |    0 |
    |  6 | Linux         |    1 |
    |  7 | Mysql/MariaDB |    1 |
    |  8 | 收 藏         |    3 |
    | 10 | Others        |    0 |
    +----+---------------+------+
'''
## 3、pip install pymysql tronado
## 4、python3 server.py