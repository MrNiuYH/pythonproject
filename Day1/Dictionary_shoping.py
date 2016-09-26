# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

'''
PersonalFile = {
    123233423554353: {
    'name': "niuniu",
    'old': 23
    },
    3223233423554353: {
    'name': "zhang",
    'old': 24
    },
    555553324324452: {
    'name': "li",
    'old': 34
    }
}

print(PersonalFile[123233423554353])  # 查看
PersonalFile.get(123233423554353)  # 一般用get获取value
PersonalFile[123233423554353]['name'] = "shanPao"  # 修改
print(PersonalFile)
PersonalFile[34235235345634] = {'name': "luozi", 'old': 54}  # 增加
print(PersonalFile)
# del PersonalFile[34235235345634]    # 删除
# PersonalFile.pop(34235235345634)
PersonalFile[34235235345634].pop("old")
print(PersonalFile[34235235345634])

Per1 = {
    'name': "wang",
    555553324324452: {
    'name': "lizai",
    'old': 34
    }
}
print(PersonalFile)
PersonalFile.update(Per1)   # 更新，当新的字典里有和老字典有一样key 的话，就更新老的字典里的value
print(PersonalFile)
print(PersonalFile.keys())
print(PersonalFile.values())

PersonalFile.has_key(555553324324452)   # 判断key是否存在 2.0 版本使用
555553324324452 in PersonalFile    # 2.0 3.0 版本通用

print(Per1.setdefault(555553324324452, {'name': "liangzai"}))   # 判断key是否存在，存在返回v值，不存在设置new的k，v 值
Per1.popitem()  # 随机删除，慎用

for i in PersonalFile:    # 打印字典的key value值
    print(i, PersonalFile[i])
'''
# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# shopping_car = {
#     1: ["iphone", 6888, 5],
#     2: ["ipad", 4000, 8],
#     3: ["LeTV", 3920, 1],
#     4: ["car", 200000, 2],
#     5: ["cup", 10, 15],
#     6: ["Nokia", 250, 4]
# }
# num = 1
# print(type(num))
# print(shopping_car.get(num)[2])
#
# for i in enumerate(shopping_car):
#     print(i[0] + 1, '.', i[1])
# aa = input("输入选择")
#
# print(shopping_car[aa].get(1)[1])
# print(len(shopping_car[aa]))
# for j in shopping_car[aa]:
#     print(j, ':', shopping_car[aa][j])
# import pickle,os
# #
# print(os.path.exists(r'user_mess.pkl'))
#
# if os.path.exists(r'user_mess.pkl') == bool(True):
#     pkl_file = open('user_mess.pkl', 'rb')
#     reg_user = pickle.load(pkl_file)
#     pkl_file.close()
# else:
#     reg_user = {}
#
# print(reg_user)
#
# register_name = input("用户名：")
# register_pwd = input("密  码：")
# print(register_name,register_pwd)
# print(reg_user.keys(), reg_user[register_name])
# if register_name in reg_user.keys() and register_pwd == reg_user[register_name]['pwd']:
#     print("登录成功".center(40, '-'))
#     True_False = False
# else:
#     print("1111")
#
# dd['zhou']["money"] = 500
# user_val = open('user_mess.pkl', 'wb')
# pickle.dump('zhou', user_val)
# user_val.close()
#
# print(dd)
# if "niuyh" in dd:
#     for i in dd["niuyh"]:
#         print(i)
# dict1 = {}
# shopping_car = {
#     "iphone": {1: ["iphone", 6888, 5], 2: ["ipad", 4000, 8], 3: ["Samsung", 3000, 3]},
#     "variety": {1: ["headset", 50, 5], 2: ["usb_cable", 18, 8], 3: ["teacup", 60, 30]},
#     "clothing": {1: ["coat", 900, 5], 2: ["pants", 110, 8], 3: ["shoes", 300, 3]}
#     }
# for i, va in enumerate(shopping_car):  # 打印商品列表
#     print(i +1 , va)
#   dict1[i[0]] = i[1]
# print(dict1)
# print(dict1[1])
# print("------------")
# print(shopping_car[dict1[1]])
# print("------------")
# select_type = input("1111:")
#
#
# for j in shopping_car[dict1[int(select_type)]]:
#     print(j, ':', shopping_car[dict1[int(select_type)]][j])

# if int(select_type) in (1, 2, 3):
#     for j in shopping_car[select_type]:
#         print(j, ':', shopping_car[select_type][j])

# lis1 = [['ipad', 4000, 8], ['222', 4000, 8], ['111', 4000, 8]]
# print()
# for i in lis1:
#     print(i)
# import pickle
# Menus = {
#     'mobile_phone': {
#         'iphone': {
#             'iphone7': {"6500", "64G"},
#             'iphone6': {"5500", "64G"},
#             'iphone3gs': {"停产", "无"}
#         },
#         '三星': {
#             'C5': {"2500", "8G"},
#             'S7': {"5688", "16G"},
#             'A8': {"1588", "2G"}
#         },
#         '华为': {
#             '荣耀8': {"2200", "4G"},
#             'Note': {"1099", "无"},
#             '畅玩5A': {"799", "无"}
#         }
#     },
#     'computer': {
#         '联想': {
#             'lianx1': {"6500", "64G"},
#             'lianx2': {"5500", "64G"},
#             'lianx3': {"停产", "无"}
#         },
#         '华硕': {
#             'huas1': {"6500", "64G"},
#             'huas2': {"5500", "64G"},
#             'huas3': {"停产", "无"}
#         },
#         '苹果': {
#             'pingguo1': {"6500", "64G"},
#             'pingguo2': {"5500", "64G"},
#             'pingguo3': {"停产", "无"}
#         }
#     },
#     'car': {
#         '奥迪': {
#             'aodi1': {"6500", "64G"},
#             'aodi2': {"5500", "64G"},
#             'aodi3': {"停产", "无"}
#         },
#         '宝马': {
#             'baoma1': {"6500", "64G"},
#             'baoma2': {"5500", "64G"},
#             'baoma3': {"停产", "无"}
#         },
#         '奔驰': {
#             'benc1': {"6500", "64G"},
#             'benc2': {"5500", "64G"},
#             'benc3': {"停产", "无"}
#         }
#     }
# }
# file_obj = open('information.pkl', 'wb')
# pickle.dump(Menus, file_obj)
# file_obj.close()
# lo = "nolock"
# menu = {}
# 读取文件
# file = open('userine.txt')
# for i in file.readlines():
#     li = i.split()
#     menu[li[0]] = [li[1], li[2]]
# print(menu)
#
# menu['niu'][1] = "lock"
# print(menu)
# file = open('userine.txt', 'w')
#
# for j in menu:
#     cc = j + " " + " ".join(menu[j])
#     file.writelines(cc)
#     file.write('\n')
# file.close()
#
# print(menu)


# 注册写入
# uname = input("Uname:")
# pwd = input("Pwd:")
# li = [uname, pwd, lo]
# newli = " ".join(li)
# file = open('userine.txt','a+')
# file.writelines(newli)
# file.write('\n')
# file.close()