# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
FILENAME = "haproxy.cfg"
NEWFILE = "new.cfg"
SERLIST = []
POPUPMSG = '''
\033[31;1m--------------------------\033[0m
1、查看
2、增加
3、删除
4、修改
5、退出
\033[31;1m--------------------------\033[0m
'''
SELMSG = '请输入你的选择：'
ERRMSG = '输入错误！！！'
BANSEL = '请输入backend:'
SERVER = '请输入servers:'
NOHAVE = '无此backend'
SERMSG = '''请输入要修改的整个servers信息。以，间隔
例如：server 192.168.1.1 192.168.1.1 weight 4 maxconn 50，server 192.168.1.1 192.168.1.1 weight 4 maxconn 50
'''


def Back_ha(filename, oldfile):   # 复制配置文件
    with open(filename, 'r', encoding='utf-8') as old,\
            open(oldfile, 'w', encoding='utf-8') as new:
        for i in old:
            new.write(i)


def Sel_backend(file, backendname):   # 查询backend 及server信息
    To = False
    li = []
    with open(file, 'r', encoding='utf-8') as f:
        for fi in f:
            if fi.strip().startswith('backend') and fi.strip() == "backend  " + backendname:
                To = True
                continue
            if To and fi.strip().startswith('backend'):
                break
            if To and fi.strip():
                li.append(fi.strip())
    return li


def Add_backend(backid,servers):  # 添加 backend 及 server信息
    li = Sel_backend(FILENAME, backid)
    if li:    # backend 存在
        if servers in li:
            return True
        else:
            newip = servers.split()[1:2][0]
            if newip in "".join(li):
                print("xiugai")
            else:
                li.append(servers)
                with open(FILENAME, 'r', encoding='utf-8') as old, \
                        open(NEWFILE, 'w', encoding='utf-8') as new:
                    To = False
                    for i in old:
                        if i.startswith('backend') and To:
                            new.write(i)
                            To = False
                            continue
                        if i.startswith('backend') and i.strip().endswith(backid):
                            To = True
                            new.write(i)
                            for j in li:
                                new.write(' ' * 4 + j + '\n')
                            new.write('\n')
                        if not To:
                            new.write(i)
    else:   # backend 不存在 则直接 尾部添加
        with open(FILENAME, 'r', encoding='utf-8') as old, \
                open(NEWFILE, 'w', encoding='utf-8') as new:
            for i in old:
                new.write(i)
            new.write('\nbackend  {_bid}'.format(_bid=backid))
            new.write('\n'+' '*4 + servers)
            Back_ha(NEWFILE, FILENAME)


def Modif_backend(backid,servers):   # 修改 backend 及 server信息
    SERLIST = Sel_backend(FILENAME, backid)
    if SERLIST:
        ser = servers.split(',')
    else:
        print(NOHAVE)
    pass


def Del_backend():   # 删除 backend 及 server信息
    pass


while True:
    print(POPUPMSG)
    selectid = input(SELMSG)
    if selectid == "1" or selectid == "查看":
        banid = input(BANSEL)
        SERLIST = Sel_backend(FILENAME, banid)
        if SERLIST:
            for j in SERLIST:
                print(j)
        else:
            print(NOHAVE)
    elif selectid == "2" or selectid == "增加":
        banid = input(BANSEL)
        servers = input(SERVER)
        Add_backend(banid, servers)
    elif selectid == "3" or selectid == "删除":
        pass
    elif selectid == "4" or selectid == "修改":
        pass
    elif selectid == "5" or selectid == "退出":
        exit("退出")
    else:
        print(ERRMSG)
