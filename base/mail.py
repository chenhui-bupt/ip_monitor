import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

class Mail():	
    def __init__(self):
        print("I am sending the mails...")

    def setSmtpServer(self, smtpServer):
        self.smtpserver = smtpServer

    def setSender(self, sender, password):
        self.sender = sender
        self.password = password

    def setReceivers(self, receivers):
        self.receivers = receivers

    def setMessage(self, subject, content, From="ip_monitor", To="ant1009"):
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header(From, 'utf-8')
        message['To'] =  Header(To, 'utf-8')
        self.message = message

    def sendMail(self):
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(self.smtpserver, 25)    # 25 为 SMTP 端口号
            smtpObj.login(self.sender, self.password)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    def __del__(self):
        print("%s\n" % datetime.datetime.now())
