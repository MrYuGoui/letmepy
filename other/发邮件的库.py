from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

邮箱 = "18530840706@163.com"
密码 = "yhw19920830"
对象 = "18530840706@163.com"

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('霍格沃兹<%s>' % 邮箱)
msg['To'] = _format_addr('管理员 <%s>' % 对象)
msg['Subject'] = Header('来自***的问候……', 'utf-8').encode()

server = smtplib.SMTP("smtp.163.com", 25)
server.set_debuglevel(1)
server.login(邮箱, 密码)
server.sendmail(邮箱, [对象], msg.as_string())
server.quit()