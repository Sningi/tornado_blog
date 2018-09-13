create table users(
    id integer primary key AUTO_INCREMENT,
    name varchar(15) unique,
    nickname varchar(20) ,
    Career varchar(20) ,
    motto varchar(80) default '个人格言',
    portrait varchar(70) default 'static/image/user_1.jpg',
    password varchar(16),
    tel varchar(15),
    email varchar(20)
);

create table category(
id integer primary key,
name varchar(10),
sum int default 0
);

create table articles(
    id integer primary key AUTO_INCREMENT,
    title varchar(30),
    summary text,
    content text,
    Key_words varchar(20),
    category integer REFERENCES category(id) ON DELETE CASCADE,
    creatime datetime,
    read_num integer,
    image_url varchar(60),
    u_id integer REFERENCES users(id) ON DELETE CASCADE
);

Insert into category (ID,NAME) values (1,'Java');
Insert into users (id,name,nickname,Career,motto,password,tel,email) values (0,'Sning','Insight','Student','青青子衿，悠悠我心','197010','17739458175','1620524565@qq.com');
    id integer primary key AUTO_INCREMENT,
    name varchar(15) unique,
    nickname varchar(20) ,
    Career varchar(20) ,
    motto varchar(80) default '个人格言',
    portrait varchar(70) default 'static/image/user_1.jpg',
    password varchar(16),
    tel varchar(15),
    email varchar(20)
Insert into articles values(
    0,
    'tesr',
    '用最。思路很简三个ul来调用。国cms列表模板',
    '需要做到以下就可以实  表模板',
    '示例',
    3,
    '2018-07-24 13:42:26',
    0,
    'static/images/text02.jpg',
    0
);