import os
import base64
import uuid

address = '0.0.0.0'
port = 8888

Dir_path = os.path.dirname(__file__)


static_path = os.path.join(Dir_path,'static')
Aplipay_path = os.path.join(Dir_path,'alipay')
template_path = os.path.join(Dir_path,'templates')

alipay_public_key_path = os.path.join(Dir_path,'alipay','alipay_public_key.pem')
app_private_key_path = os.path.join(Dir_path,'alipay','app_private_key.pem')
APPID = 2016091600528103
GETAWAY = "https://openapi.alipaydev.com/gateway.do"

cookie_secret = base64.b64encode(uuid.uuid1().bytes + uuid.uuid4().bytes).decode()

#[redis]
redis_config_cook={'redis_host':'127.0.0.1',
                'redis_port' : 6379,
                'redis_auth' : '',
                'db':0,
                'auth':'',
                'time_':60,
                   'defalite':'N',
                }


redis_config_cache={'redis_host':'127.0.0.1',
                'redis_port' : 6379,
                'redis_auth' : '',
                'db':1,
                'auth':'',
                    'time_':60
                }

redis_config_iptables={'redis_host':'127.0.0.1',
                'redis_port' : 6379,
                'redis_auth' : '',
                'db':2,
                'auth':'',
                'time_':60
                }

db_config={'host':'176.215.155.241',
            'port':3306,
            'user':'root',
            'password':"liu",
            'database':'text',
            'charset':'utf8',
            }