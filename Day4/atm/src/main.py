# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import demo


user_information = {"is_access": False,
                    "infordate": None}


def access_login():
    username = input("username:").strip()
    password = input("password:").strip()
    if demo.acc_file(username, password):
        user_information['infordate'] = demo.acc_file(username, password)
        user_information['is_access'] = True
        print(user_information)
    else:
        print("用户名或密码错误！")


def run():
    if not user_information['is_access']:
        access_login()

