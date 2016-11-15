# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import random
import hashlib
import os
import json


def rand():
    li = []
    for i in range(10):
        new = random.randrange(1, 9)
        li.append(str(new))
    st = "".join(li)
    return st


def md5(pwd):
    """
    : hashlib.md5() 创建md5对象
    :update 生成加密串
    :hexdigest 获取加密串
    :param pwd:
    :return:
    """
    m = hashlib.md5()
    m.update(pwd)
    return m.hexdigest()


def get_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login(file):
    """
    登录
    :return:
    """
    pp = get_path()
    while True:
        uname = input("please input username:")
        cid = input("please input card:")
        pwd = input("please input password:")
        md_pwd = md5(bytes(pwd, encoding='utf-8'))
        if os.path.isfile(os.path.join(pp, 'db', file, cid)):
            if md_pwd == json.load(open(os.path.join(pp, 'db', file, uname), 'r'))['passwd']:
                return True
            else:
                print('password error')
        else:
            print("用户不存在")


def mkdir(file1, file2):
    gpath = get_path()
    os.chdir(os.path.join(gpath, 'db', file1))
    os.mkdir(file2)
    os.chdir(os.path.join(gpath, 'db', file1, file2))
    current = os.getcwd()
    return current

