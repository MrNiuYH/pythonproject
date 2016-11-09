# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import random
import hashlib


def rand():
    li = []
    for i in range(5):
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