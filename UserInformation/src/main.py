# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import config
from lib import public
import time

li = public.get_userinfo()
dic = {}


def get_user(fun1):
    def demo1(*args, **kwargs):
        print(config.USERMSG)
        for item in li:
            print("  ".join(item.split(',')))
            xuhao = item[:1]
            dic[xuhao] = item
        fun1(*args, **kwargs)
    return demo1


def if_file(fun):
    """
    装饰函数
    :return:
    """
    def demo(*args, **kwargs):
        if not public.get_file():
            print("现在还没有员工信息，请先添加员工信息！！！")
        else:
            fun(*args, **kwargs)
    return demo


def add_information():
    """
    添加员工信息
    :return:
    """
    Name = input("用户名：").strip()
    Age = input("年 龄：").strip()
    Phone = input("手机号：").strip()
    Dept = input("职 业：").strip()
    Enroll = time.strftime('%Y-%m-%d', time.localtime())
    if public.get_file():
        with open(config.DBPATH, 'r+', encoding='utf-8') as fi:
            num = fi.read(-1)[:1]
            u_info = ",".join([str(int(num)+1), Name, Age, Phone, Dept, Enroll])
            fi.write('\n' + u_info)
    else:
        u_info = ",".join(['1', Name, Age, Phone, Dept, Enroll])
        with open(config.DBPATH, 'w', encoding='utf-8') as file:
            file.write(u_info)


@if_file
def select_information():
    """
    查询员工信息
    :return:
    """
    pass


@get_user
@if_file
def del_information():
    """
    删除员工信息
    :return:
    """
    del_num = input("输入相应的序号：").strip()
    if del_num.isdigit() and del_num in dic:
        li.remove(dic[del_num])
        with open(config.DBPATH_BAk, 'w', encoding='utf-8') as bak:
            bak.write(",".join(li))
        public.back_ha(config.DBPATH_BAk, config.DBPATH)
        print("已删除！！！")


@get_user
@if_file
def update_information():
    """
    更新员工信息
    :return:
    """
    print(public.PRINTMSG)
    del_type = input("输入更新的语句：").strip()
    old_key = ''.join(del_type.split('"')[1:2])
    new_key = ''.join(del_type.split('"')[3:4])
    if old_key in li:
        pass
    else:
        print("none")




def exit_item():
    """
    退出
    :return:
    """
    exit("GoodBay!")


info = {
'1': select_information,
'2': add_information,
'3': del_information,
'4': update_information,
'5': exit_item
}


def fun():
    """
    程序入口
    :return:
    """
    while True:
        print(config.LISTMSG)
        user_sel = input("please select a number:").strip()
        if user_sel.isdigit and user_sel in info:
            info[user_sel]()
