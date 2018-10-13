import tornado.ioloop
import tornado.web
from route_ import application_route
from setting import port,address

if __name__ == "__main__":
    app = application_route#application路由
    app.listen(port,address,xheaders=True)
    tornado.ioloop.IOLoop.current().start()#启动