# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

def sendmail():
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText('邮件正文，我不想和你啪啪啪', 'plain', 'utf-8')
        msg['From'] = formataddr(['Mr.niu', 'tongyongc0m@163.com'])
        msg['To'] = formataddr(["NIma", '853499733@qq.com'])
        msg['Subject'] = "老子是主题"

        server = smtplib.SMTP('smtp.163.com', 25)
        server.login('tongyongc0m@163.com', '1qazxsw2')
        server.sendmail('tongyongc0m@163.com', ['853499733@qq.com', ], msg.as_string())
        server.quit()
    except:
        # 发送失败返回值
        return "shibai"
    else:
        # 发送成功返回值
        return "chengg"
rev = sendmail()
if rev == "chengg":
    print("cg")
else:
    print("shib")

