import tornado.web
from setting import redis_config_cook,redis_config_cache
from concurrent.futures import ThreadPoolExecutor
from ser_.mysql_tor import mysql_con,User,Record,Adve
from ser_.redis_tor import redis_server
from setting import db_config
from ser_.OperateRedis import OperateRedis


print('初始化开始'*10)
redis_cook = redis_server(redis_config_cook['redis_host'],redis_config_cook['redis_port'],
                                       db=redis_config_cook['db'],password=redis_config_cook['redis_auth'])

redis_cache = OperateRedis(redis_config_cache['redis_host'],redis_config_cache['redis_port'],
                                   dbs=redis_config_cache['db'],password=redis_config_cache['redis_auth'])

Thrad_t = ThreadPoolExecutor(20)
do_thing = Thrad_t.submit
mysql_obj = mysql_con(db_config['user'],db_config['password'],db_config['host'],
                           db_config['port'],db_config['database'])
session_ = mysql_obj.get_session_()
User_obj = User
Record_obj = Record
Adve_obj = Adve

time_expire = redis_config_cook['time_']
key_values_redis = redis_config_cook['defalite']

print('初始化结束'*10)
class Req(tornado.web.RequestHandler):
    def initialize(self):
        # self.redis_cook = redis_server(redis_config_cook['redis_host'],redis_config_cook['redis_port'],
        #                                db=redis_config_cook['db'],password=redis_config_cook['redis_auth'])
        #
        # self.redis_cache = OperateRedis(redis_config_cache['redis_host'],redis_config_cache['redis_port'],
        #                                dbs=redis_config_cache['db'],password=redis_config_cache['redis_auth'])
        #
        # self.Thrad_t = ThreadPoolExecutor(20)
        # self.do_thing = self.Thrad_t.submit
        # self.mysql_obj = mysql_con(db_config['user'],db_config['password'],db_config['host'],
        #                            db_config['port'],db_config['database'])
        # self.session_ = self.mysql_obj.get_session_()
        # self.User_obj = User
        # self.Record_obj = Record
        # self.Adve_obj = Adve
        #
        # self.time_expire = redis_config_cook['time_']
        # self.key_values_redis = redis_config_cook['defalite']

        self.Upage = 0
        self.Npage = 0

        self.redis_cook =redis_cook
        self.redis_cache = redis_cache
        self.Thrad_t = Thrad_t
        self.do_thing = do_thing
        self.mysql_obj = mysql_obj
        self.session_ = session_
        self.User_obj = User_obj
        self.Record_obj = Record_obj
        self.Adve_obj = Adve_obj

        self.time_expire = time_expire
        self.key_values_redis = key_values_redis




    def get_current_user(self):
        current_user = self.get_secure_cookie('username')
        if current_user:
            return current_user
        return None
