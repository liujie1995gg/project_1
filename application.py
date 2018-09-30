import tornado.ioloop
import tornado.web

from xm_.route_1 import *


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", Main_slave),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port=8888,address='127.0.0.1',xheaders=True)
    tornado.ioloop.IOLoop.current().start()