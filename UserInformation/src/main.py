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


def get_user(fun1):
    """
    装饰函数
    :param fun1:
    :return:
    """
    def demo1(*args, **kwargs):
        print(config.USERMSG)
        for item in li:
            print("  ".join(item.split(',')))
            xuhao = item[:1]
            dic[xuhao] = item
        fun1(*args, **kwargs)
    return demo1


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
            num = fi.readlines()[-1][0:1]
            u_info = ",".join([str(int(num)+1), Name, Age, Phone, Dept, Enroll])
            fi.write(u_info)
            print(config.ADDUSERMSG.format(*[str(int(num)+1), Name, Age, Phone, Dept, Enroll]))
    else:
        u_info = ",".join(['1', Name, Age, Phone, Dept, Enroll])
        with open(config.DBPATH, 'w', encoding='utf-8') as file:
            file.write(u_info + '\n')
        print(config.ADDUSERMSG.format(*['1', Name, Age, Phone, Dept, Enroll]))
    li.append(u_info)


@if_file
def select_information():
    """
    查询员工信息
    :return:
    """
    while True:
        print(config.SELECTMSG)
        # select  * from staff_table where enroll_date like "2013"
        # select name,age from staff_table where age > 22
        sel_Statement = input("输入查询语句>>：").strip()
        judgment = ''.join(sel_Statement.split()[6:7])
        iftype = ''.join(sel_Statement.split()[5:6])
        if ''.join(sel_Statement.split()[:1]) == "select":
            if judgment == ">":
                if iftype == "age":
                    pass
                else:
                    print(config.ERRMSG)
            elif judgment == "=":
                pass
            elif judgment == "like":
                pass
            else:
                print(config.ERRMSG)
        else:
            print(config.ERRMSG)


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
        with open(config.DBPATH_BAK, 'w', encoding='utf-8') as bak:
            for i in li:
                bak.write(i + '\n')
        public.back_ha(config.DBPATH_BAK, config.DBPATH)
        print("已删除！！！")


@if_file
def update_information():
    """
    更新员工信息
    :return:
    """
    print(config.UPDATEMSG)
    del_Statement = input("输入更新的语句>>：").strip()
    del_typ = ''.join((''.join(del_Statement.split('=')[:1])).split()[-1:])
    set_typ = ''.join(del_Statement.split()[-3:-2])
    new_key = ''.join(del_Statement.split('"')[1:2])
    old_key = ''.join(del_Statement.split('"')[3:4])
    if del_typ in config.TYPEMSG:
        if set_typ in config.TYPEMSG:
            with open(config.DBPATH_BAK, 'w', encoding='utf-8') as old:
                for line in li:
                    if old_key in line:
                        lin = line.split(",")
                        lin[config.TYPEMSG.index(del_typ)] = new_key
                        line = ",".join(lin)
                        old.write(line + '\n')
                        continue
                    old.write(line + '\n')
            public.back_ha(config.DBPATH_BAK, config.DBPATH)
            print("已更新！")
        else:
            print(config.ERRMSG)
    else:
        print(config.ERRMSG)


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
