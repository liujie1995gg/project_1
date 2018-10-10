import redis,hashlib,time

class redis_server(object):
    def __init__(self,host,port,db,password=None):
        if not password:
            password = None
        r_pool = redis.ConnectionPool(host=host, port=port,db=db,password=password)
        self.redis_r = redis.Redis(connection_pool=r_pool,password=password)
    def set(self,name,value):
        return self.redis_r.set(name,value)

    def get(self,name):
        return self.redis_r.get(name)

    def delete(self,name):
        return self.redis_r.delete(name)

    def setex(self,name,value,time):
        return self.redis_r.setex(name,value,time)

    def redis_change(self,key,value):#查询在内存的数据
        _ = self.get(key)
        if _:
            p = _.decode()
            if value == p:
                return True

class A(object):
    @staticmethod
    def Judge(self,username,password,**kwargs):
        cur = self.session_.query(self.User_obj.username==username).filter(self.User_obj.password==password).first()
        if cur:
            _ = self.do_thing(A.get_vip,self,username).result()
            self.redis_cook.setex(username,_,self.time_expire)
            return True
        try:
            if kwargs['regesit']:#这里是注册情况
                self.session_.add(self.User_obj(username=username,password=password))
                self.session_.commit()
                self.redis_cook.setex(username, self.key_values_redis, self.time_expire)
                return True
        except:
            return False

    @staticmethod
    def get_sec_cooke(self):#判断登录状态
        try:
            _ = self.get_secure_cookie('username')
            _ = _.decode()
        except:
            pass
        if self.redis_cook.get(_):
            self.redis_cook.setex(_,self.redis_cook.get(_),self.time_expire)
            return _
        else:
            return False


    @staticmethod
    def post_t(self,**kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        if self.redis_cook.redis_change(username,password):
            return username
        elif A.Judge(self,username,password,**kwargs):#这里去读redis
            return username
        return False

    @staticmethod #从数据库读
    def get_vip(self,username):
        _ = self.session_.query(self.User_obj.vip).filter(self.User_obj.username==username).scalar()
        if _ =='Y':
            return True
        else:
            return False

    @staticmethod #从redis读
    def get_vip_redis(self,username):
        _ = self.redis_cook.get(username)
        _ = _.decode()
        return _



    @staticmethod
    def set_state(self,code,order_id,list1=False):#更改record表纪录
        ip = self.request.remote_ip
        username = A.get_sec_cooke(self)
        code_ = code
        list_ = list1
        self.session_.add(self.Record_obj(ip=ip,username=username,order_n=order_id,code_=code_,list_=list_))
        self.session_.commit()
        return True

    @staticmethod
    def set_state_user(self):#充值之后改状态为Ｙ#并重新设置值为Ｔrue
        _ = A.get_sec_cooke(self)
        self.session_.query(self.User_obj.username==_).update({self.User_obj.vip:'Y'})
        self.session_.commit()
        self.redis_cook.setex(_,True,self.time_expire)
        return True

    @staticmethod
    def get_retu_dict(self):##渲染页头字典
        id = '注册'
        id1 = '登录'
        u = A.get_sec_cooke(self)
        id2 = '成为会员'
        id3 = './pay'
        if u:
            id1 = u
            u1 = A.get_vip_redis(self, u)
            if u1 == str(True):
                id = ''
                id2 = 'vip'
                id3 = './'
            else:
                id = ''
                pass
        return {'regesit':'./regesit',
                'regesit_id':id,
                'login':'./login',
                'index': './index',
                'visual':'./',
                'info':'./',
                'id':id1,
                'id2':id2,
                'id3':id3}

    @staticmethod
    def get_adve(self,num=3):
        u = A.get_sec_cooke(self)
        if u:
            u1 = A.get_vip_redis(self, u)
            if u1 == str(True):#
                #返回１０条
                return []
            else:
                #返回7条
                pass
        a = list()

        #从广告数据库读取广告
        #c = self.session_.query(self.Adve_obj.bt_,self.Adve_obj.lj_).filter(self.Adve_obj.cs_!=0)[0:num]
        c = [('这是广告１',111),('广告２',2222),('广告３',333)]
        for i in c:
            a.append(i)
        return a

    @staticmethod
    def get_md5():
        m5 = hashlib.md5()
        a= str(time.time())
        m5.update(a.encode())
        pasd= m5.hexdigest()
        return pasd
