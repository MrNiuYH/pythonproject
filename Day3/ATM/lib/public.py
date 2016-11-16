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
    gpath = get_path()
    while True:
        cid = input("please input card:")
        pwd = input("please input password:")
        md_pwd = md5(bytes(pwd, encoding='utf-8'))
        if os.path.isdir(os.path.join(gpath, 'db', file, cid)):
            if md_pwd == json.load(open(os.path.join(gpath, 'db', file, cid, 'userinfo'), 'r'))['passwd']:
                return cid
            else:
                print('password error')
        else:
            print("卡号错误，请认真输入哦！！！")


def mkdir(file1, file2):
    gpath = get_path()
    os.chdir(os.path.join(gpath, 'db', file1))
    os.mkdir(file2)
    os.chdir(os.path.join(gpath, 'db', file1, file2))
    current = os.getcwd()
    return current


def get_userinfo(cid):
    """
    获取用户信息
    :param cid:
    :return:
    """
    gpath = get_path()
    if os.path.isdir(os.path.join(gpath, 'db', 'userinfo', cid)):
        umsg = json.load(open(os.path.join(gpath, 'db', 'userinfo', cid, 'userinfo'), 'r'))
        return umsg


def input_user(dic, cid, filename):
    """
    写入文件
    :param dic:
    :return:
    """
    gpath = get_path()
    json.dump(dic, open(os.path.join(gpath, 'db', 'userinfo', cid, filename), 'w'))
