# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import pickle, os
'''Menus = {
    'mobile_phone': {
        'iphone': {
            'iphone7': {"6500", "64G"},
            'iphone6': {"5500", "64G"},
            'iphone3gs': {"停产", "无"}
        },
        '三星': {
            'C5': {"2500", "8G"},
            'S7': {"5688", "16G"},
            'A8': {"1588", "2G"}
        },
        '华为': {
            '荣耀8': {"2200", "4G"},
            'Note': {"1099", "无"},
            '畅玩5A': {"799", "无"}
        }
    },
    'computer': {},
    'car': {}
}'''

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
to_or_fal_1 = True
to_or_fal_2 = True
to_or_fal_3 = True
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

def Get_List(menu):
        for j, k in enumerate(menu):
            print(j + 1, '.', k)
            select_list1.append(k)
# *********************************

# 获取菜单
Menus = Get_File_Content(Menus, 'information.pkl')

while True:
    for i, ke in enumerate(Menus):
        print(i+1, '.', ke)
        select_list.append(ke)
    print(OPTION_MSG_NO_B)
    _add1 = input(INPUT_MSG)
    if _add1.isdigit() and int(_add1) in (range(1, 4)):  # 判断是否在字典的key中
        to_or_fal_1 = True
        while to_or_fal_1:
            nu = int(_add1) - 1
            Get_List(Menus[select_list[nu]])
            print(OPTION_MSG)
            _mob_type = input(INPUT_MSG)
            if _mob_type.isdigit() and int(_mob_type) in (range(1, 4)):
                to_or_fal_2 = True
                while to_or_fal_2:
                    nu1 = int(_mob_type) - 1
                    Get_List(Menus[select_list[nu]][select_list1[nu1]])
                    print(OPTION_MSG)
                    _price = input(INPUT_MSG)
                    if _price.isdigit() and int(_price) in (range(1, 4)):
                        to_or_fal_3 = True
                        while to_or_fal_3:
                            nu2 = int(_price) - 1
                            print(Menus[select_list[nu]][select_list1[nu1]][select_list2[nu2]])
                            print(LAST_OPTION)
                            Back = input(INPUT_MSG)
                            if Back == "b":
                                to_or_fal_3 = False
                            elif Back == "q":
                                exit(OUT_MSG)
                            else:
                                print(ERR_MSG)
                    elif _price == "b":
                        to_or_fal_2 = False
                        to_or_fal_3 = True
                    else:
                        print(ERR_MSG)
                    if _price == "q":
                        exit(OUT_MSG)
            elif _mob_type == "b":
                to_or_fal_1 = False
                to_or_fal_2 = True
            else:
                print(ERR_MSG)
            if _mob_type == "q":     # 判断是否退出
                exit(OUT_MSG)
    elif _add1 == "q":
        exit(OUT_MSG)
    else:
        print(ERR_MSG)
