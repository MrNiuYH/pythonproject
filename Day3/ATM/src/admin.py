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

login_user_cid = ""


def input_msg():
    while True:
        name = input("用户名:").strip()
        pwd = input("密 码:").strip()
        mobile = input("手机号:").strip()
        print(var.QUOTA_MSG.format(ad.QUOTA))
        quota = input("可透支额度:").strip()
        print(var.USER_MSG)
        role = input("用户类型:").strip()
        num = pu.rand()
        card = "622202" + num
        p = pu.md5(bytes(pwd, encoding='utf-8'))

        ad.user_info["card"] = card
        ad.user_info["uname"] = name
        ad.user_info["passwd"] = p
        if mobile.isdigit and len(mobile) == 11:
            ad.user_info["phone"] = mobile
        else:
            print("手机号格式错误，重新输入吧！！")
            continue
        if quota == "":
            ad.user_info["quota"] = ad.QUOTA
        else:
            ad.user_info["quota"] = quota
        if role == "user" or role == "admin" or role == "":
            if role == "":
                ad.user_info["role"] = "user"
            else:
                ad.user_info["role"] = role
        else:
            print("用户类型输入错误，重新输入吧！！")
            continue
        ad.user_info["status"] = "1"
        return ad.user_info


def add_user():
    """
    添加用户
    :return:
    """
    dic = input_msg()
    if dic["role"] == "admin":
        json.dump(dic, open(os.path.join(pu.mkdir('admin', dic["card"]), 'userinfo'), 'w'))
    elif dic["role"] == "user":
        json.dump(dic, open(os.path.join(pu.mkdir('userinfo', dic["card"]), 'userinfo'), 'w'))
        print(var.REGISTER.format(cid=dic['card']))
    else:
        print("Please select admin or user")


def freeze_user():
    """
    冻结用户
    :return:
    """
    cid = input("Please enter a card number to freeze!!!")
    if os.path.isdir(os.path.join(pp, 'db', 'userinfo', cid)):
        uu = pu.get_userinfo(cid)
        uu['status'] = '0'
        pu.input_user(uu, cid, 'userinfo')
        print("The user account is frozen")
    else:
        print("Card number does not exist")


def update_user():
    """
    修改用户信息
    :return:
    """
    pass


def list_user():
    """
    打印用户列表
    :return:
    """
    li = os.listdir(os.path.join(pp, 'db', 'userinfo'))
    for i in enumerate(li):
        print(i[0], ',', i[1])


def count():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """
    AD_MENU_SEL = {
        '1': add_user,
        '2': list_user,
    }
    print(var.AD_MENU)
    user_option = input("选择操作序号：").strip()
    if user_option in AD_MENU_SEL:
        AD_MENU_SEL[user_option]()
    else:
        print("序号不存在")


def run():
    login_user_cid = pu.login('admin')
    if login_user_cid:
        count()
