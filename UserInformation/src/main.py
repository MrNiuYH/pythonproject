# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import config


def select_information():
    """
    查询员工信息
    :return:
    """
    pass


def add_information():
    """
    添加员工信息
    :return:
    """
    print("pass")


def del_information():
    """
    删除员工信息
    :return:
    """
    pass


def update_information():
    """
    更新员工信息
    :return:
    """
    pass


info = {
'1': select_information,
'2': add_information,
'3': del_information,
'4': update_information
}


def fun():
    print(config.LISTMSG)
    user_sel = input("please select a number:").strip()
    if user_sel.isdigit and user_sel in info:
        info[user_sel]()
