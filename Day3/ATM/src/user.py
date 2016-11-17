# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import public as pu
from lib import variable as var


def deposit():
    """
    存款
    :return:
    """
    pass


def freeze_user():
    """
    取款
    :return:
    """
    pass


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
    pass


def repayment():
    """
    还款
    :return:
    """
    pass


def count():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """
    US_MENU_SEL = {
        '1': deposit,
        '2': freeze_user,
        '3': transfer,
        '4': balance(),
        '5': repayment()
    }
    print(var.USER_MENU)


def run():
    if pu.login('userinfo'):
        count()
