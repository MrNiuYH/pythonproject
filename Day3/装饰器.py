# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

# 装饰器
'''
由高阶函数(把一个函数名当作实参传递给另一个函数,返回值中包含函数名)
和
嵌套函数(函数中嵌套函数)组成
功能：在不更改原函数的代码和调用方式的前提下添加新的功能

装饰器本身就是一个函数。使用方法如

装饰器函数

1、自动执行装饰器函数login并且被装饰的函数名（index）当做参数传递给函数（fun = index）
2、将装饰函数login的返回值auto重新赋值给被装饰的函数
'''


def login(fun):
    def auto():
        print("add new Function")
        fun()
    return auto


@login
def index():
    print("in the index")

index()

# 如果被装饰的函数带参数
# *args, **kwargs 万能参数, *args 传位置参数并将参数转换成为一个元组格式， **kwargs 传关键字参数，并转换成字典格式


def login(fun):
    def auto(*args, **kwargs):
        print("add new Function")
        fun(*args, **kwargs)
    return auto


@login
def admin(name):
    print("the admin user name is {_name}".format(_name=name))

admin("babi")


# 场景应用，三个页面（index，admin，information）进入首页不用登录，进入后台和用户信息页面需要登录
name, pwd = "jian", "0325"

def login(fun):
    def demo(*args, **kwargs):
        usname = input("Username:").strip()
        passwd = input("Password:").strip()
        if usname == name and passwd == pwd:
            print("welcome to shopping car!")
            return fun(*args, **kwargs)
        else:
            print("Input error")
    return demo


def index():
    print("in the index...........")


@login
def admin():
    print("in the admin===================")
    return "admin"


@login
def information(fuck):
    print("in the information-----------------{fa}".format(fa=fuck))


index()

admin()

information('fuck fuck fuck')