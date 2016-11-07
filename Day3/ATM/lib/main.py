# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import adminlogin as admin
import userlogin as user

PMSG = '''
    1.用户登录
    2.管理员登录
'''

print(PMSG)
re = input("please input a number!:").strip()

if re == "1":
    user.login()
elif re == "2":
    admin.login()
else:
    print("input error!")