#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers.html import HtmlHandler
from handlers.resource import ResourceHandler, FileHandler, ImageHandler, CreateHandler

url = [
    (r"/", HtmlHandler),
    (r"/file", FileHandler),
    (r"/createart", CreateHandler),
    (r"/uploadImages", ImageHandler),
    (r"/.+?\.html", HtmlHandler),
    (r".+?", ResourceHandler)
]
