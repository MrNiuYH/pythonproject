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
        pass


def run():
    pass

