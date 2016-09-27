# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

'''
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
'''
'''
# 普通参数
def get_v(b):
    a = b + 2
    return a
print(get_v(6))

# 默认参数
def get_a_b(a, b, c = "didi"):
    print(a, b, c)
get_a_b(5, 21)
get_a_b(5, 21, "baba")

# 指定参数
get_a_b(b=21, a=5, c="lili")

# * 可接收动态参数
def get_all_v(*value):
    print(value)

get_all_v(23)   # (23,)
li = [23, 445, 66, "dsad"]
get_all_v(li)   # ([23, 445, 66, 'dsad'],)
get_all_v(li, 34)   # ([23, 445, 66, 'dsad'], 34)
men = {"key1": "v1", "k2": "v2"}
get_all_v(*li)   # (23, 445, 66, 'dsad')
get_all_v(*li, 34)  # (23, 445, 66, 'dsad', 34)
get_all_v(*men)     # ('k2', 'key1')


def get_all_w(**value):
    print(value)
v2 = [23, 543, 66]
get_all_w(k1="v1")  # {'k1': 'v1'}
get_all_w(k2=v2)    # {'k2': [23, 543, 66]}

dic = {"k1": "v1", "k2": "v2"}
get_all_w(**dic)    # {'k1': 'v1', 'k2': 'v2'}

def get_all_a(*v, **v1):
    print(v)
    print(v1)
get_all_a(11, 2, 33, k1="v1", k2="v2")  # (11, 2, 33) {'k1': 'v1', 'k2': 'v2'}


li = ["niu", 20]
dic = {"name": "niu", "age": 28}
s1 = "name is {0}, age is {1}".format("niu", 20)
print(s1)
s1 = "name is {0}, age is {1}".format(*li)
print(s1)
s2 = "name is {name}, age is {age}".format(
    name="niu",
    age=28
)
print(s2)
s2 = "name is {name}, age is {age}".format(**dic)
print(s2)
'''
def li_append(li):
    li.append("ddd")
lis = [11, 22, 33, 44]
li_append(lis)
print(lis)  # [11, 22, 33, 44, 'ddd']

