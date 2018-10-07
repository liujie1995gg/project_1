import tornado.web
from xm_.setting import redis_config_cook,redis_config_cache
from concurrent.futures import ThreadPoolExecutor
from xm_.ser_.mysql_tor import mysql_con,User,Record,Adve
from xm_.ser_.redis_tor import redis_server
from xm_.setting import db_config


class Req(tornado.web.RequestHandler):
    def initialize(self):
        self.redis_cook = redis_server(redis_config_cook['redis_host'],redis_config_cook['redis_port'],
                                       db=redis_config_cook['db'],password=redis_config_cook['redis_auth'])
        self.redis_cache = redis_server(redis_config_cache['redis_host'],redis_config_cache['redis_port'],
                                       db=redis_config_cache['db'],password=redis_config_cache['redis_auth'])
        self.Thrad_t = ThreadPoolExecutor(20)
        self.do_thing = self.Thrad_t.submit
        self.mysql_obj = mysql_con(db_config['user'],db_config['password'],db_config['host'],
                                   db_config['port'],db_config['database'])
        self.session_ = self.mysql_obj.get_session_()
        self.User_obj = User
        self.Record_obj = Record
        self.Adve_obj = Adve

        self.time_expire = redis_config_cook['time_']
        self.key_values_redis = redis_config_cook['defalite']
        print('初始化方法')




    def get_current_user(self):
        current_user = self.get_secure_cookie('username')
        if current_user:
            return current_user
        return None
