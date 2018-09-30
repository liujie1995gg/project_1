import tornado.web

print(1)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.write(self.request.remote_ip)

class Main_slave(tornado.web.RequestHandler):
    def get(self):
        self.write('wwwwwww')