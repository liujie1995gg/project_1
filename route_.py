from view_ import *
import tornado.web
from setting import static_path,template_path,cookie_secret

application_route=tornado.web.Application(
    [
    (r"/", MainHandler),
    (r"/index", Main_page),
    (r'/login', login_in),
    (r'/regesit',regesit_page),
    (r'/pay',Alipay_page),
    (r'/pay_check',pay_check),
    (r'/l_out',login_out),
    (r'/joblist',joblist),
    (r'/joblists',joblists),
    (r'/jobxl',jobxl)

],
template_path = template_path,
static_path = static_path,
debug = True,
cookie_secret=cookie_secret,
login_url='/login',

)

