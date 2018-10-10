import time,json
from tornado import gen
import tornado.web
from alipay import AliPay
from setting import alipay_public_key_path,app_private_key_path,APPID,GETAWAY

from ser_.herit import Req
from ser_.redis_tor import A

class MainHandler(Req):
    def get(self):
        self.write("Hello, world")
        self.write(self.request.remote_ip)

class Main_page(Req):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self):
        _ = yield self.do_thing(A.get_sec_cooke,self)
        self.render('index.html',user=_)

class login_in(Req):
    @gen.coroutine
    def get(self):
        self.render('login.html', regesit='./regesit', url='')

    @gen.coroutine
    def post(self):
        try:
            nextname = self.get_argument('next')
            u = self.do_thing(A.post_t,self).result()
            self.set_secure_cookie('username', u, expires_days=None)
            self.redirect(nextname)
        except:
            u =self.do_thing(A.post_t,self).result()
            if u:
                self.set_secure_cookie('username', u, expires_days=None)
                self.redirect('./index')
            else:
                self.redirect('./login')


class login_out(Req):

    def get(self):
        _ = self.do_thing(A.get_sec_cooke,self).result()
        self.redis_cook.delete(_)
        self.cookies.clear()
        self.redirect('/login')


class regesit_page(Req):
    @gen.coroutine
    def get(self):
        self.render('regesit.html',url='')

    @gen.coroutine
    def post(self):
        u =self.do_thing(A.post_t,self,regesit=True).result()
        if u:
            self.set_secure_cookie('username', u, expires_days=None)
            self.redirect('/index')


class Alipay_page(Req):
    @tornado.web.authenticated
    def get(self):
        a = 1154343440012#随机生成16位码
        self.render('pay_index.html',
                    orderid=a,
                    post_pay='',
                    get_chack_='./pay_check?order_id='
         )

    def post(self):
        order_id = self.get_body_argument('order_id')
        a = self.pay(order_id)
        self.finish(a)
        self.do_thing(A.set_state,self,9999,order_id).result()


    def pay(self,order_id):
        alipy_ = AliPay(APPID,
                       app_notify_url=None,
                       app_private_key_path=app_private_key_path,
                       alipay_public_key_path=alipay_public_key_path,
                       sign_type="RSA2",
                       debug=True
                       )

        order_string = alipy_.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=str(0.01),
            subject='tornado测试',
            return_url=None,
            notify_url=None
        )  # 传参到支付宝进行校验
        url = GETAWAY + "?" + order_string
        return {"code": 0, "message": "请求支付中","url": url}

class pay_check(Req):
    def get(self):
        order_id= self.get_argument('order_id')
        a = self.check_pay(order_id)
        self.finish(a)
        self.do_thing(A.set_state,self, a['code'], order_id, True).result()
        self.do_thing(A.set_state_user,self).result()

    def check_pay(self, order_id):
        alipay_ = AliPay(
            appid=APPID,
            app_notify_url=None,
            app_private_key_path=app_private_key_path,
            alipay_public_key_path=alipay_public_key_path,
            sign_type='RSA2',
            debug=True
        )
        _ = 0
        while True:
            _ += 1
            try:
                response = alipay_.api_alipay_trade_query(order_id)
                code = response.get('code')
                sub_msg =response.get('sub_msg')
                trade_status = response.get('trade_status')

                if code == "10000" and trade_status == 'TRADE_SUCCESS':
                    #付款成功，需要改变状态，，未做完
                    return {"code": 1, "message": "成功"}

                elif code == '40004' or (code == "10000" and trade_status == "WAIT_BUYER_PAY"):
                    if _ >=60:
                        #需要在此标记订单状态###此处是ＢＵＧ
                        break
                    time.sleep(2)
                    continue
                else:
                    return {"code": -1, "message": "失败"}

            except Exception as e:
                time.sleep(3)
        return {"code": -2, "message": "失败"}

class joblist(Req):#未完成
    #@tornado.web.authenticated

    def get(self):
        try:
            b = int(self.get_argument('page'))
            print(b,'bbbbbbbbbbbbbb',self.current_user)
            if b == 1:
                raise 1
            if b <= 1:
                raise 1
            print(b,'进来')
            a = self.do_thing(A.get_retu_dict, self).result()  # 返回
            self.Upage = b - 1
            self.Npage = b + 1
            print('#'*100)
            list_1 = self.do_thing(self.redis_cache.read, b).result()
            self.render('block1.html', **a, id_1='./joblist', id_2='./joblist?page=%s' % self.Upage,
                        id_3='joblist?page=%s' % self.Npage, b=list_1)
            print('#' * 100)
        except:
            a = self.do_thing(A.get_retu_dict, self).result()
            list_ = self.do_thing(A.get_adve,self,3).result()#返回广告内容
            list_1 = self.do_thing(self.redis_cache.read).result()
            self.render('block.html',**a,
                        a=list_,b=list_1,id_1='./joblist?page=1',
                        sumit1='1',id_2='./joblist?page=2',sumit2='2')

class joblists(Req):
    def get(self):
        pass


class jobxl(Req):
    @gen.coroutine
    def get(self):
        a=self.do_thing(A.get_retu_dict,self).result()
        self.render('jobxl.html', **a)