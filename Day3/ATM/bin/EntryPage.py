# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import user
from src import admin

PMSG = '''
    1.用户登录
    2.管理员登录
'''
print(PMSG)

re = input("please input a number!:").strip()

if re == "1":
    user.run()
elif re == "2":
    admin.run()
else:
    print("Input Error")

    