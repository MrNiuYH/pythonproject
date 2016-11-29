# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import public as pu
from lib import variable as var

uid = ""
user_dic = ""


def deposit():
    """
    存款
    :return:
    """
    deposid_m = input("Please enter the deposit amount:").strip()
    if deposid_m != "" or deposid_m.isdigit():
        m = user_dic['balance']
        user_dic['balance'] = int(m) + int(deposid_m)
        pu.input_user(user_dic)
        print("已存款成功，您的余额为：{}".format(user_dic['balance']))
    else:
        print("Input Error")


def freeze_user():
    """
    取款
    :return:
    """
    withdrawal_a = input("Please enter the withdrawal amount:").strip()
    if withdrawal_a != "" or withdrawal_a.isdigit():
        n = user_dic['balance']
        q = user_dic['quota']
        m_sum = int(n) + int(q)
        if m_sum < int(withdrawal_a):
            print("Sorry, your credit is running low")
        else:
            if int(n) < int(withdrawal_a):
                new_withd = int(withdrawal_a) - int(user_dic['balance'])
                user_dic['balance'] = 0
                user_dic['quota'] = int(user_dic['quota']) - (int(withdrawal_a) - new_withd)
            else:
                user_dic['balance'] = int(n) - int(withdrawal_a)
            pu.input_user(user_dic)
            print("已取款成功，您的余额为：{}".format(user_dic['balance']))
    else:
        print("Input Error")


def transfer():
    """
    转账
    :return:
    """
    pass


def balance():
    """
    查看账户信息
    :return:
    """
    print(var.USERMSG.format(_name=user_dic["uname"],
                             _card=user_dic["card"],
                             _phone=user_dic["phone"],
                             _balance=user_dic["balance"],
                             _quota=user_dic["quota"]
                             ))


def repayment():
    """
    还款
    :return:
    """
    pass


def logout():
    """
    退出
    :return:
    """
    exit()


def count():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """
    US_MENU_SEL = {
        '1': deposit,
        '2': freeze_user,
        '3': transfer,
        '4': balance,
        '5': repayment,
        '6': logout
    }
    while True:
        print(var.USER_MENU)
        user_option = input("选择操作序号：").strip()
        if user_option in US_MENU_SEL:
            US_MENU_SEL[user_option]()
        else:
            print("序号不存在")


def run():
    global uid
    uid = pu.login('userinfo')
    if uid:
        global user_dic
        user_dic = pu.get_userinfo(uid)
        count()
