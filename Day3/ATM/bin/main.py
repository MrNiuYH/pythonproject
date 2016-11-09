# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import sys
import os
import ad_login as ad
import us_login as us

PMSG = '''
    1.用户登录
    2.管理员登录
'''

print(PMSG)
re = input("please input a number!:").strip()

if re == "1":
    us.login()
elif re == "2":
    ad.login()
else:
    print("input error!")