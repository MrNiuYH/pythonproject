# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

dic = {}


def check_user(function):
    def inner_fun(*args, **kwargs):
        if dic.get('name'):
            fu = function(*args, **kwargs)
            return fu
        else:
            print("please login")
    return inner_fun


def check_admin(function1):
    def inner_fun1(*args, **kwargs):
        fu = function1(*args, **kwargs)
        return fu
    return inner_fun1


def userlog():
    uname = input("输入用户名：")
    pwd = input("输入密码：")
    if uname == "niu" and pwd == "123":
        dic['name'] = 'niu'
        print("ok")
    else:
        print("pass")


@check_user
def manage():
    print("欢迎{_name}来到用户管理后台".format(_name=dic['name']))


def main():
    while True:
        print('1.用户管理，2.用户登录, 3.超级管理员:')
        re = input("请输入：")
        if re == "1":
            manage()
        elif re == "2":
            userlog()
        elif re == "3":
            pass
        else:
            print('error')

main()
