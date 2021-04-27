# coding:utf-8
import smtplib
import time,sys,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.log.mylog import log
from config import readconfig  as R
from config.allpath import result_path

Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
# 测试报告的路径
reportPath = result_path
logger = log
# 配置收发件人
r= R.ReadConfig()
recvaddress = r.get_mail("addr")
# 163的用户名和密码
sendaddr_name =r.get_mail("name")
sendaddr_pswd = r.get_mail("pwd")


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = r.get_mail("subject")
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')


        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp163.com', 25)
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(recvaddress, sendaddr_name, self.msg.as_string())
            logger.info("发送邮件成功")
            smtp.close()
        except:
            logger.error('发送邮件失败')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
