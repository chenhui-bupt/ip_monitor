# -*- coding: utf-8 -*-
import smtplib
import string
from email.mime.text import MIMEText
import base64
import sys


class MailSender():	
    def __init__(self):
        print("I am sending the mails...")

    def setSmtpServer(self, smtpServer):
        self.smtpserver = smtpServer

    def setSender(self, sender, password):
        self.sender = sender
        self.password = password

    def setReceiver(self, receiver):
        self.receiver = receiver

    def setSubject(self, subject):
        self.subject = subject

    def setContent(self, content):
        self.content = content

    def sendMail(self):
        smtp = smtplib.SMTP_SSL()
        smtp.connect(self.smtpserver, 465)
        smtp.login(self.sender, self.password)
        self.content = base64.encodestring(self.content.encode())
        msg = "From:%s\nTo:%s\nSubject:%s\nContent-Type:text/html;charset=UTF-8\nContent-Transfer-Encoding:base64\n\n%s" % (self.sender, self.receiver, self.subject, self.content)
        smtp.sendmail(self.sender, self.receiver, msg)
        smtp.close()

    def __del__(self):
        print("Finish sending mails !")

    