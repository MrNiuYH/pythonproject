# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os
FILENAME = "haproxy.cfg"
NEWFILE = "new.cfg"
SERLIST = []
SELMSG = '请输入你的选择：'
ERRMSG = '输入错误！！！'
BANSEL = '请输入backend:'
HINTMSG = "\033[46;1m!!!如果输入多条server 则以','间隔\033[0m"
SERVER = '请输入servers:'
NOHAVE = '无此backend'
MODIFMSGERR = "修改失败，\033[31;1mbackend\033[0m不存在"
MODIFMSG = "修改成功"
SHOWMSG = '''******************************
{_bak}的server信息如下:
******************************'''
TR_OR_FA = True
POPUPMSG = '''
\033[31;1m--------------------------\033[0m
1、查看
2、增加
3、删除
4、修改
5、退出
\033[31;1m--------------------------\033[0m
'''
SERMSG = '''
------------------------------------------------------------------------------------------------------
\033[46;1m请输入要修改的整个servers信息。以','间隔
例如：server 192.168.1.1 192.168.1.1 weight 4 maxconn 50,server 192.168.1.2 192.168.1.2 weight 4 maxconn 50\033[0m
------------------------------------------------------------------------------------------------------
'''
UPMSG = '''
\033[31;1mIP已经存在，已更新server信息，并写入文件中\033[0m
'''
INSMSG = '''
\033[31;1mBackend 存在，新的server已添加到末尾，并更新到文件\033[0m
'''
NOBACKMSG = '''
\033[31;1m新的backend及server已添加到末尾，并更新到文件中\033[0m
'''
DELMSG = '''\033[31;1m
    1、删除 整个 backend
    2、删除 单条server信息\033[0m
    '''
DELSUEE = '删除成功'
DELERRMSG = '删除失败'
OUTMOD = "\033[31;1m已退出对当前文件的操作\033[0m"
SELNUM = "请输入你要删除server信息前面的序号:"
FILEERR = "文件不存在！"


def Back_ha(filename, oldfile):   # 复制配置文件
    with open(filename, 'r', encoding='utf-8') as old,\
            open(oldfile, 'w', encoding='utf-8') as new:
        for i in old:
            new.write(i)


def Write_file(id, lists):     # 更新并写入文件
    with open(FILENAME, 'r', encoding='utf-8') as old, \
            open(NEWFILE, 'w', encoding='utf-8') as new:
        To = False
        for i in old:
            if i.startswith('backend') and To:
                new.write(i)
                To = False
                continue
            if i.startswith('backend') and i.strip().endswith(id):
                To = True
                new.write(i)
                for j in lists:
                    new.write(' ' * 4 + j + '\n')
                new.write('\n')
            if not To:
                new.write(i)
    Back_ha(NEWFILE, FILENAME)


def Sel_backend(backend):   # 查询backend 及server信息
    To = False
    li = []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for fi in f:
            if fi.strip().startswith('backend') and fi.strip() == "backend  " + backend:
                To = True
                continue
            if To and fi.strip().startswith('backend'):
                break
            if To and fi.strip():
                li.append(fi.strip())
    return li


def Add_backend(backid, servers):  # 添加 backend 及 server信息
    li = Sel_backend(backid)
    if li:    # backend 存在
        if servers in li:   # server 存在
            return True
        else:   # server 不存在
            newip = servers.split()[1:2][0]
            if newip in "".join(li):    # 判断是否有相同的ip ，有则更改 并写入文件
                for se in li:
                    if newip in se:     # 获取ip存在server的索引，并替换成新的server
                        inde = li.index(se)
                        li[inde] = servers
                        Write_file(backid, li)
                        print(UPMSG)

            else:   # 没有相同ip 则添加一行 并写入文件
                li.append(servers)
                Write_file(backid, li)
                print(INSMSG)
                # with open(FILENAME, 'r', encoding='utf-8') as old, \
                #         open(NEWFILE, 'w', encoding='utf-8') as new:
                #     To = False
                #     for i in old:
                #         if i.startswith('backend') and To:
                #             new.write(i)
                #             To = False
                #             continue
                #         if i.startswith('backend') and i.strip().endswith(backid):
                #             To = True
                #             new.write(i)
                #             for j in li:
                #                 new.write(' ' * 4 + j + '\n')
                #             new.write('\n')
                #         if not To:
                #             new.write(i)
    else:   # backend 不存在 则直接 尾部添加
        with open(FILENAME, 'r', encoding='utf-8') as old, \
                open(NEWFILE, 'w', encoding='utf-8') as new:
            for i in old:
                new.write(i)
            new.write('\n')
            new.write('backend  {_bid}'.format(_bid=backid))
            serli = servers.split(',')
            for ser in serli:
                new.write('\n'+' '*4 + ser)
        Back_ha(NEWFILE, FILENAME)
        print(NOBACKMSG)


def Modif_backend(backid, servers):   # 修改 backend 及 server信息
    SERLIST = Sel_backend(backid)     # 获取server信息
    if SERLIST:
        ser = servers.split(',')
        Write_file(backid, ser)
        # with open(FILENAME, 'r', encoding='utf-8') as old, \
        #         open(NEWFILE, 'w', encoding='utf-8') as new:
        #     To = False
        #     for i in old:
        #         if i.startswith('backend') and To:
        #             new.write(i)
        #             To = False
        #             continue
        #         if i.startswith('backend') and i.strip().endswith(backid):
        #             To = True
        #             new.write(i)
        #             for j in ser:
        #                 new.write(' ' * 4 + j + '\n')
        #             new.write('\n')
        #         if not To:
        #             new.write(i)
        return True
    else:
        return False


def Del_backend(back, liss):   # 删除 backend 及 server信息
    print(DELMSG)
    num = input("Please select a number:")
    if num.isdigit():
        if num == "1":  # 删除整个backend信息
            with open("haproxy.cfg", 'r', encoding='utf-8') as old, \
                    open('new.cfg', 'w', encoding='utf-8') as new:
                To = False
                for i in old:
                    if i.startswith('backend') and To:
                        new.write(i)
                        To = False
                        continue
                    if i.startswith('backend') and i.strip().endswith(back):
                        To = True
                    if not To:
                        new.write(i)
            Back_ha(NEWFILE, FILENAME)  # 更新的新文件替换老的文件
            return True
        elif num == "2":    # 删除选择的server信息
            for nu in enumerate(liss):
                print(nu[0], '.', nu[1])
            selnu = input(SELNUM)
            if selnu.isdigit() and int(selnu) in range(len(liss)):
                liss.pop(int(selnu))
                Write_file(back, liss)
                return True
            else:
                return False
        else:
            return False
    else:
        print(ERRMSG)


while TR_OR_FA:
    if os.path.exists(FILENAME):
        Back_ha(FILENAME, FILENAME+'.back')
        print(POPUPMSG)
        selectid = input(SELMSG)
        if selectid == "1":     # 调用查看函数 Sel_backend
            banid = input(BANSEL)
            SERLIST = Sel_backend(banid)
            if SERLIST:
                print(SHOWMSG.format(_bak=banid))
                for j in SERLIST:
                    print(j)
            else:
                print(NOHAVE)
        elif selectid == "2":   # 调用增加函数 Add_backend
            banid = input(BANSEL)
            print(HINTMSG)
            servers = input(SERVER)
            Add_backend(banid, servers)
        elif selectid == "3":   # 调用删除函数 Del_backend
            banid = input(BANSEL)
            SERLIST = Sel_backend(banid)
            if SERLIST:
                print(SHOWMSG.format(_bak=banid))
                for j in SERLIST:
                    print(j)
                if Del_backend(banid, SERLIST):
                    print(DELSUEE)
                else:
                    print(DELERRMSG)
            else:
                print(NOHAVE)

        elif selectid == "4":   # 调用修改函数 Modif_backend
            banid = input(BANSEL)
            servers = input(SERMSG)
            if Modif_backend(banid, servers):
                print(MODIFMSG)
            else:
                print(MODIFMSGERR)
        elif selectid == "5":   # 退出
            print(OUTMOD)
            TR_OR_FA = False
        else:
            print(ERRMSG)
    else:
        TR_OR_FA = False
        print(FILEERR)
