# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import config
from lib import public

dic = {}
if public.get_userinfo():
    li = public.get_userinfo()
else:
    li = []


def if_file(fun):
    """
    装饰函数,查看文件是否存在，存在就可以进行查询删除更新等操作，否则则添加信息
    :return:
    """
    def demo(*args, **kwargs):
        if not public.get_file():
            print("现在还没有员工信息，请先添加员工信息！！！")
        else:
            if li:
                fun(*args, **kwargs)
            else:
                print("现在还没有员工信息，请先添加员工信息！！！")
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
    Enroll = time.strftime('%Y-%m-%d', time.localtime())    # 获取当前年月日
    if public.get_file():   # 文件存在就追加，不存在就创建
        with open(config.DBPATH, 'r+', encoding='utf-8') as fi:
            if li:
                num = fi.readlines()[-1][0:1]   # 读取文件最后一行获取pid，id自增
                u_info = ",".join([str(int(num)+1), Name, Age, Phone, Dept, Enroll])
            else:
                u_info = ",".join(['1', Name, Age, Phone, Dept, Enroll])
            fi.write(u_info)
            print(config.ADDUSERMSG.format(*u_info.split(',')))
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
    lia = public.get_userinfo()
    while True:
        new_li = []
        count = 0
        print(config.SELECTMSG)
        sel_Statement = input("输入查询语句>>：").strip()  # 获取查询语句，并截取相对应的字段做判断依据
        key = ''.join(sel_Statement.split()[-1:]).strip('"')
        judgment = ''.join(sel_Statement.split()[6:7])
        iftype = ''.join(sel_Statement.split()[5:6])
        sel_tp = ''.join(sel_Statement.split()[1:2])
        if ''.join(sel_Statement.split()[:1]) == "select":
            if judgment == ">":     # 如果查询语句是 > 号，获取判断的对象做对比，符合要求则添加到新的列表中
                for line in lia:
                    lin = line.split(",")
                    if int(lin[config.TYPEMSG.index(iftype)]) > int(key):
                        new_li.append(lin)
                        count += 1
            elif judgment == "=":   # 如果查询语句是 = 号，获取判断的对象做对比，符合要求则添加到新的列表中
                for line in lia:
                    lin = line.split(",")
                    if lin[config.TYPEMSG.index(iftype)] == key:
                        new_li.append(lin)
                        count += 1
            elif judgment == "like":    # 如果查询语句是 ，获取判断的对象做匹配，符合要求则添加到新的列表中
                for line in lia:
                    lin = line.split(",")
                    if key in lin[config.TYPEMSG.index(iftype)]:
                        new_li.append(lin)
                        count += 1
            else:
                print(config.ERRMSG)
            print(config.COUNTMSG.format(count))    # 打印总条数
            if sel_tp == "*":   # 判断查询条件是否为* ，* 显示全部，否则根据查询条件显示相对应的字段
                for i in new_li:
                    print(i)
            else:
                sel_list = sel_tp.split(',')
                for i in new_li:
                    print(i[config.TYPEMSG.index(sel_list[0])], i[config.TYPEMSG.index(sel_list[1])])
        else:
            print(config.ERRMSG)
        str_y = input("是否继续 y?n").strip()
        if str_y.lower() == "n":    # 判断是否 继续
            break


@if_file
def del_information():
    """
    删除员工信息
    :return:
    """
    print(config.USERMSG)
    for item in li:
        print("  ".join(item.split(',')))
        xuhao = item[:1]
        dic[xuhao] = item
    del_num = input("输入相应的序号：").strip()
    if del_num.isdigit() and del_num in dic:    # 判断序号是否存在，存在则删除列表的对应行，并更新到文件中
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
    if del_typ in config.TYPEMSG:   # 判断更新的类型是否存在
        if set_typ in config.TYPEMSG:   # 判断查询的类型是否存在
            with open(config.DBPATH_BAK, 'w', encoding='utf-8') as old:
                for line in li:
                    if old_key in line:
                        lin = line.split(",")
                        lin[config.TYPEMSG.index(del_typ)] = new_key    # 更新字段
                        line = ",".join(lin)
                        old.write(line + '\n')  # 更新的行写入到文件
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
