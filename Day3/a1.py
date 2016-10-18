# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu


def Adecorato(fun):
    def inpu():
        print("log")
        return fun()
    return inpu

# 装饰器
# @+函数名
# 功能
#    1、自动执行函数（Adecorato）并且将‘@函数名’（@Adecorato）下面的函数名（ss1）当做参数传递给函数
#    2、将函数Adecorato的返回值inpu重新赋值给‘@函数名’@Adecorato下面的函数名ss1
@Adecorato
def ss1():
    print("ss1")


@Adecorato
def ss2():
    print("ss2")


@Adecorato
def ss3():
    print("ss3")