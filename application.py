#!/usr/bin/env Python
# coding=utf-8
from url import url
import tornado.web
import os
import mariadb.test
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret='0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    xsrf_cookies=False,
    autoreload=True,
    ui_methods=mariadb.test,
    # static_url_prefix='/statics/',
    debug=True,
    log_path=os.path.join(os.path.dirname(__file__), 'logs/log')
)

application = tornado.web.Application(
    handlers=url,
    **settings
)
