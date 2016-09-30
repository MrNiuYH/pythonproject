# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
FILENAME = "haproxy.cfg"
SERLIST = []
POPUPMSG = '''
\033[31;1m--------------------------\033[0m
1、查看
2、增加
3、删除
4、修改
\033[31;1m--------------------------\033[0m
'''
SELMSG = '请输入你的选择：'
ERRMSG = '输入错误！！！'
BANSEL = '输入你想看的backend:'

def Back_ha(filename):   # 备份配置文件
    oldfile = filename + ".back"
    print(oldfile)
    with open(filename, 'r', encoding='utf-8') as old,\
            open(oldfile, 'w', encoding='utf-8') as new:
        for i in old:
            new.write(i)


def Sel_backend(balist,file,backendname):   # 查询backend 及server信息
    To = False
    with open(file, 'r', encoding='utf-8') as f:
        for fi in f:
            if fi.strip().startswith('backend') and fi.strip() == "backend  " + backendname:
                To = True
                continue
            if To and fi.strip().startswith('backend'):
                break
            if To and fi.strip():
                balist.append(fi.split())
    return balist


def Add_backend():  # 添加 backend 及 server信息
    pass


def Modif_backend():   # 修改 backend 及 server信息
    pass


def Del_backend():   # 删除 backend 及 server信息
    pass

# if os.path.exists(FILENAME):
#     Back_ha(FILENAME)
#
# aa = Sel_backend(SERLIST, FILENAME, 'server.xiju.com')
# print(aa)

while True:
    print(POPUPMSG)
    selectid = input(SELMSG)
    if selectid == "1" or selectid == "查看":
        banid = input(BANSEL)
        SERLIST = Sel_backend(SERLIST, FILENAME, banid)
        if SERLIST:
            for j in SERLIST:
                print(j)
        else:
            print("wu")
    elif selectid == "2" or selectid == "增加":
        pass
    elif selectid == "3" or selectid == "删除":
        pass
    elif selectid == "4" or selectid == "修改":
        pass
    else:
        print(ERRMSG)
