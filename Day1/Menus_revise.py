# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import pickle, os

'''  写入文件
file_obj = open('information.pkl', 'wb')
pickle.dump(Menus, file_obj)
file_obj.close()
'''
'''获取文件内容'''

# ************常量定义**************
WEL_MSG = "欢迎来到三级菜单".center(40, '*')
OPTION_MSG = '''(1)输入序号进入下一栏.(2)输入 \033[31;1mb \033[0m返回上一层.(3)输入 \033[31;1mq \033[0m结束查看菜单.
====================================================================='''
OPTION_MSG_NO_B = '''(1)输入序号进入下一栏.(2)输入 \033[31;1mq \033[0m结束查看菜单.
====================================================================='''
LAST_OPTION = '''(1)最后一栏.2)输入 \033[31;1mb \033[0m返回上一层.(3)输入 \033[31;1mq \033[0m结束查看菜单.
====================================================================='''
INPUT_MSG = "请输入你的选择："
ERR_MSG = "\033[31;1m输入错误！\033[0m"
OUT_MSG = "Bye Bye!"
# *********************************


# ***********变量定义*************
select_list = []
select_list1 = []
select_list2 = []
Menus = {}
True_False = True
# *********************************

# ****************函数定义*****************
'''获取文件内容'''


def Get_File_Content(Mefile, filename):
    if os.path.exists(filename):
        pkl_file = open(filename, 'rb')
        Mefile = pickle.load(pkl_file)   # 获取文件中的字典并赋值
        pkl_file.close()
        return Mefile
    else:
        return {}
'''get true or false'''


def Get_Input(input_num):
    if input_num.isdigit() and int(input_num) in (range(1, 4)):
        return True
    else:
        return False
# *********************************

# 获取菜单
Menus = Get_File_Content(Menus, 'information.pkl')

while True_False:
    for i, ke in enumerate(Menus):  # 打印第一层菜单，并把kv添加到新的列表
        print(i + 1, '.', ke)
        select_list.append(ke)
    print(OPTION_MSG_NO_B)
    _add1 = input(INPUT_MSG)

    if Get_Input(_add1):  # 判断是否在字典的key中
        while True_False:
            nu = int(_add1) - 1
            for j, k in enumerate(Menus[select_list[nu]]):  # 打印第二层菜单，并把kv添加到新的列表
                print(j + 1, '.', k)
                select_list1.append(k)
            print(OPTION_MSG)
            _mob_type = input(INPUT_MSG)
            if _mob_type == "q":  # 判断是否退出
                exit(OUT_MSG)
            if Get_Input(_mob_type):  # 判断是否在字典的key中
                while True_False:
                    nu1 = int(_mob_type) - 1
                    # 打印第三层菜单，并把kv添加到新的列表
                    for m, v in enumerate(Menus[select_list[nu]][select_list1[nu1]]):
                        print(m + 1, '.', v)
                        select_list2.append(v)
                    print(OPTION_MSG)
                    _price = input(INPUT_MSG)
                    if _price == "q":
                        exit(OUT_MSG)
                    if Get_Input(_price):
                        nu2 = int(_price) - 1
                        print(Menus[select_list[nu]][select_list1[nu1]][select_list2[nu2]])
                        print(LAST_OPTION)

                        while True_False:
                            Back = input(INPUT_MSG)
                            if Back == "b":
                                break
                            elif Back == "q":
                                exit(OUT_MSG)
                            else:
                                print("只有输入b才能返回上一层哦!")
                    elif _price == "b":
                         break
                    else:
                        print(ERR_MSG)
            elif _mob_type == "b":
                break
            else:
                print(ERR_MSG)
    else:
        print(ERR_MSG)
