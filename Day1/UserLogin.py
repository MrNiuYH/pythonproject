#!  /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Mr Niu"
import os
# 常量
LOCK_MSG = "\033[31;1m账户已被锁定，请联系管理员解锁！！！\033[0m"
TELL_MSG = "\033[31;1m已输错三次，账户被锁定！请联系管理员解锁！！\033[0m"
ERR_MSG = "\033[31;1m用户名或者密码错误，请重新输入！！！\033[0m"
WEL_MSG = "Welcome %s to the new world"
NO_USER_MSG = "用户 %s 不存在"
K = 3
LOCK = "lock"
UFILENAME = 'userine.txt'
# 变量
count = 0
# 获取用户列表
def Get_User(file):
    menu = {}
    if os.path.exists(file):
        ufile = open(file)
        for n in ufile.readlines():
            li = n.split()
            menu[li[0]] = [li[1], li[2]]
        ufile.close()
    else:
        menu = {}
    return menu
# 更新写入到文件
def Update_User(dic, filename):
    file = open(filename, 'w')
    for j in dic:
        cc = j + " " + " ".join(dic[j])
        file.writelines(cc)
        file.write('\n')
    file.close()

# 注册 写入到 文件
# def Set_User(u_name, u_pwd, lo):
#     li = [u_name, u_pwd, lo]
#     newli = " ".join(li)
#     file = open('userine.txt', 'a+')
#     file.writelines(newli)
#     file.write('\n')
#     file.close()
# 读取文件内容转换成字典并赋值
user_int = Get_User(UFILENAME)

for i in range(3):
    u_name = input("please input your Name:")
    u_pass = input("please input your passwd:")
    if u_name in user_int:  # 判断用户在不在字典中
        passwd = user_int[u_name][0]    # 获取用户的密码
        if user_int[u_name][1] == LOCK:
            exit(LOCK_MSG)
        else:
            count += 1
            if u_pass == passwd:  # 对比 密码，相同进入欢迎页面
                exit((WEL_MSG % u_name).center(40, '='))
            else:
                if count == K:  # 判断是否输错三次
                    user_int[u_name][1] = 'lock'
                    Update_User(user_int, UFILENAME)
                    print(TELL_MSG)
                else:
                    print(ERR_MSG)
    else:
        exit(NO_USER_MSG % u_name)
