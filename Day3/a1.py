# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu


def auto(fun):
    def inpu(*args, **kwargs):  # 万能参数
        print("open")    # 函数前添加功能
        r = fun(*args, **kwargs)   # 原函数有返回值，接收并返回
        print("end")    # 函数后添加功能
        return r
    return inpu

# 装饰器
# @+函数名
# 功能
#    1、自动执行函数（auto）并且将‘@函数名’（@auto）下面的函数名（ss1）[函数名ss1代表一个整体]当做参数传递给函数
#    2、将函数auto的返回值inpu重新赋值给‘@函数名’@auto下面的函数名ss1


# @auto
# def ss1():    # 无参数
#     print("ss1")
#     return 'fan'


@auto
def ss1(k):     # 有参数
    print(k)
    return 'fan'


@auto
def ss2(s1, s2):
    print(s1 + s2)
