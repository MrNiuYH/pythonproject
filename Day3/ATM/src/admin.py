# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import admin_config as ad
from lib import public as pu
import json


def input_msg():
    name = input("用户名:").strip()
    pwd = input("密 码:").strip()
    mobile = input("手机号:").strip()
    quota = input("额 度:").strip()
    role = input("user/admin:").strip()
    num = pu.rand()
    card = "622202" + num
    p = pu.md5(bytes(pwd, encoding='utf-8'))

    ad.user_info["card"] = card
    ad.user_info["uname"] = name
    ad.user_info["passwd"] = p
    ad.user_info["phone"] = mobile
    ad.user_info["quota"] = quota
    ad.user_info["role"] = role
    return ad.user_info


def add_user():
    """
    添加用户
    :return:
    """
    dic = input_msg()
    if dic["role"] == "admin":
        json.dump(dic, open(os.path.join(pu.get_path, 'db', 'admin', dic['uname'])))
    elif dic["role"] == "user":
        json.dump(dic, open(os.path.join(pu.get_path, 'db', 'admin', dic['uname'])))
    else:
        print("input error")


def freeze_user():
    """
    冻结用户
    :return:
    """
    pass


def count():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """
    pass


def login():
    """
    登录
    :return:
    """
    while True:
        uname = input("    please input you name:".format())
        pwd = input("please input you password:")
        if uname == "niu":
            add_user()


def run():
    if login():
        count()
