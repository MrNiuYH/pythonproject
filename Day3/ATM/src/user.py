# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import admin_config as ac


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


def main():
    """
    主题函数，根据用户选择进行分类操作
    :return:
    """


def login():
    """
    登录
    :return:
    """
    print("login user")


def run():
    if login():
        main()