import tornado.ioloop
import tornado.web
from xm_.route_ import application_route
from xm_.setting import port,address


if __name__ == "__main__":
    app = application_route
    app.listen(port,address,xheaders=True)
    tornado.ioloop.IOLoop.current().start()