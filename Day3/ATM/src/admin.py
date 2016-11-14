# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import admin_config as ad
from lib import public as pu
from lib import variable as var
import json


pp = pu.get_path()


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
        json.dump(dic, open(os.path.join(pp, 'db', 'admin', dic['uname'])))
    elif dic["role"] == "user":
        json.dump(dic, open(os.path.join(pp, 'db', 'admin', dic['uname'])))
    else:
        print("input error")


def freeze_user():
    """
    冻结用户
    :return:
    """
    pass


def update_user():
    """
    修改用户信息
    :return:
    """
    pass


def count():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """
    AD_MENU_SEL = {
        '1': add_user,
        '2': freeze_user,
        '3': update_user
    }
    print(var.AD_MENU)
    user_option = input("选择操作序号：").strip()
    if user_option in AD_MENU_SEL:
        var.OPERATION.format()
        AD_MENU_SEL[user_option]()
    else:
        print("序号不存在")


def login():
    """
    登录
    :return:
    """
    while True:
        uname = input("please input username:")
        pwd = input("please input password:")
        if os.path.isfile(os.path.join(pp, 'db', 'admin', uname)):
            print('welcome')
            return True
        else:
            print("不存在")


def run():
    if login():
        count()



