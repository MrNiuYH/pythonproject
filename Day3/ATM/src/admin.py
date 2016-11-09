# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import admin_config as ad
from lib import public as pu


def add_user():
    """
    添加用户
    :return:
    """
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
    print(ad.user_info)


def freeze_user():
    """
    冻结用户
    :return:
    """
    pass


def main():
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
    print("login admin")


def run():
    if login():
        main()


add_user()