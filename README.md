### 1、Init database
    # *detail see the init_mariadb.sql*
    #
    MariaDB [blog]> show tables;
    +----------------+
    | Tables_in_blog |
    +----------------+
    | articles       |
    | category       |
    | users          |
    +----------------+
    <br>
    #
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

### 2、pip install pymysql tronado
### 3、python3 server.py
### 4、blog show
##### index
![首页](https://github.com/Sningi/tornado-blog/blob/master/showpic/pindex.png)
##### index
![详情](https://github.com/Sningi/tornado-blog/blob/master/showpic/partcile.png)