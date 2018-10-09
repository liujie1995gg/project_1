#from xm_.setting import mysql_config
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import String,Text,Date,Integer,Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
class User(base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(16))
    c_time = Column(Date)
    vip = Column(String(1))

class Record(base):
    __tablename__= 'record'
    id =Column(Integer,primary_key=True,autoincrement=True)
    ip = Column(String(20))
    username = Column(String(20))
    order_n = Column(String(16))
    code_ = Column(String(5))
    list_ = Column(String(50))
    time_ =Column(Date)

class Adve(base):
    __tablename__ = 'adve'
    id = Column(Integer,primary_key=True,autoincrement=True)
    bt_=Column(String(40))
    lj_=Column(String(100))
    cs_=Column(Integer)
    time_ =Column(Date)

class Extract(base):
    __tablename__ ='extract'
    id = Column(Integer,primary_key=True,autoincrement=True)
    url=Column(String(128))
    x_coordinate=Column(Float)
    y_coordinate=Column(Float)
    att1=Column(Text)
    company_info=Column(Text)
    company_name=Column(Text)
    company_nature=Column(Text)
    company_scale=Column(Text)
    company_trade=Column(Text)
    job_title=Column(Text)
    position_info= Column(Text)
    treatment=Column(Text)
    area=Column(Text)
    year =Column(Integer)
    education=Column(Text)
    position_count=Column(Integer)
    treatment_k=Column(Float)

class mysql_con(object):
    def __init__(self,use,pasd,host,port,database,encoding='utf-8'):
        _ ='mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'%(use,pasd,host,port,database)
        engine = create_engine(_, encoding='utf-8', echo=True)
        dbsession = sessionmaker(bind=engine)
        self.session = dbsession()
    def get_session_(self):
        return self.session

# from ser_.OperateRedis import OperateRedis
# r =OperateRedis('127.0.0.1',ports=6379,dbs=3,password=None)
class mysql_con1(object):#测试类，不调用
    def __init__(self):
        _ = 'mysql+pymysql://root:liu@176.215.155.241:3306/text?charset=utf8'
        engine = create_engine(_, encoding='utf-8', echo=True)
        dbsession = sessionmaker(bind=engine)
        self.session = dbsession()
        # c= self.session.query(Extract.id,Extract.x_coordinate,Extract.y_coordinate,
        #                       Extract.company_info,Extract.company_name,Extract.company_nature,
        #                       Extract.company_scale,Extract.job_title,
        #                       Extract.position_info,Extract.treatment,Extract.area,
        #                       Extract.year,Extract.education,Extract.position_count).all()
        # for i in c:
        #     r.write(i.id,(i.id,i.x_coordinate,i.y_coordinate,
        #                       i.company_info,i.company_name,i.company_nature,
        #                       i.company_scale,i.job_title,
        #                       i.position_info,i.treatment,i.area,
        #                       i.year,i.education,i.position_count))


#a = mysql_con1()
# r.read()


#print(r.read())


#print(session.query(User.vip).filter(User.id==1).update({User.vip:'Y'}))更改会员权限
#print(session.add(User(username='liu',password='jie',vip='Y')))#；增加
#print(session.add(Record(ip='127.0.0.1',list_='成功'.encode('utf8'))))#；增加


