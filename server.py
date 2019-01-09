#!/usr/bin/python
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define, options
from application import application

define("port", default=8888, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        application, max_buffer_size=1506270927)
    print("Development server is running at http://127.0.0.1:%s" % options.port)
    print("Quit the server with Control-C")
    # -----------修改----------------
    http_server.bind(options.port)
    http_server.start(1)
    # ------------------------------
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
