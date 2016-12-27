# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import config


def get_file():
    """
    判断文件是否存在
    :return:
    """
    if os.path.exists(config.DBPATH):
        return True


def get_userinfo():
    """
    获取用户列表
    :return:
    """
    li = []
    if get_file():
        with open(config.DBPATH, 'r', encoding='utf-8') as info:
            for i in info:
                li.append(i.strip())
        return li


def back_ha(filename, oldfile):   # 复制配置文件
    """
    更新配置文件
    :param filename:
    :param oldfile:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as old,\
            open(oldfile, 'w', encoding='utf-8') as new:
        for i in old:
            new.write(i)

