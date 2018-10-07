import redis
import pickle

class OperateRedis(object):
    def __init__(self,localhost,ports=6379,dbs=0,password=None):
        #使用连接池连接数据库，实现多个redis实例共享一个连接池
        pool = redis.ConnectionPool(host=localhost,port=ports,db=dbs,password=password)
        self.r = redis.Redis(connection_pool = pool)
        self.id = 1

    #i为写入redis数据库时对应的id,tuples为id对应的内容
    def write(self,i,tuples):
        #将tuples序列化
        a = pickle.dumps(tuples)
        self.r.hset('extract',i,a)

    #n为页数，i为第一页的显示条数，line为非第一页的显示条数
    def read(self,n=1,i=7,line=10):
        if n == 1:
            l = []
            ids = self.id
            while i != 0:
                 a = self.r.hget('extract',ids)
                 #将返回结果解序列化
                 l.append(pickle.loads(a))
                 i -= 1
                 ids += 1
            return l
        else:
            l = []
            #根据传参判断从哪个id处开始取值
            ids = (self.id+i)+(n-2)*line
            while line != 0:
                a = self.r.hget('extract',ids)
                #判断是否到达数据库末尾
                if a == None:
                    break
                l.append(pickle.loads(a))
                line -= 1
                ids += 1
            return l