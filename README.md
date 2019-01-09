#1 Init database
    #see the text mariadb.sql

    #
    MariaDB [blog]> select * from category;
    +----+---------------+------+
    | id | name          | sum  |
    +----+---------------+------+
    |  1 | Python        |    0 |
    |  2 | C/C++         |    0 |
    |  3 | Java          |    0 |
    |  4 | Android       |    0 |
    |  5 | Html/Css/Js   |    0 |
    |  6 | Linux         |    0 |
    |  7 | Mysql/MariaDB |    0 |
    |  8 | Collection    |    3 |
    | 10 | Other         |    0 |
    +----+---------------+------+
    #
#2 pip install pymysql

#3 pip install tronado

#4 python3 server.py