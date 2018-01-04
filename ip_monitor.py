# -*- coding: utf-8 -*-
import socket
import yaml
from mail_sender import MailSender

 
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
 
    return ip

print(get_host_ip())

if __name__ == '__main__':
    conf = yaml.load(open('conf/ip_monitor_conf.yaml', 'r'))
    last_ip = conf['last_ip']
    new_ip = get_host_ip()
    if new_ip != last_ip:
        conf['last_ip'] = new_ip
        yaml.dump(conf, open('conf/ip_monitor_conf.yaml', 'w+'), default_flow_style=False, allow_unicode=True)
        server = conf['send_server']
        user = conf['send_user']
        passwd = conf['send_passwd']
        receivers = [receiver['email'] for receiver in conf['receivers'] if receiver['active']]
        mail = MailSender()
        mail.setSmtpServer(server)
        mail.setSender(user, passwd)
        mail.setReceiver(receivers)
        mail.setSubject("IP地址更改通知")
        mail.setContent("Ant1009 服务器IP地址更改为: %s" % new_ip)
        mail.sendMail()

