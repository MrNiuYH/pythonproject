# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
# import time
# print(time.localtime())
# print(time.localtime(time.time()))
# print(time.strftime('%Y-%m-%d', time.localtime()))
# print("2,Alex Li,22,13651054608,IT,2013-04-01"[0:1])
# u_info = ",".join(['1', 'Name'])
# for i in range(1, 5):
#     print(i)
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from conf import config
# li = []
# if os.path.exists(config.DBPATH):
#     with open(config.DBPATH, 'r', encoding='utf-8') as info:
#         for i in info:
#             li.append(i.strip())
#
# for i in li:
#     print(i, i[:1])
# import string
#
# li = ['1,Mr Niu,23,1000000000,运维,2016-12-20']
# ss = ",".join(li)
# print(ss,type(ss))
# li = [(67, 67), (568, 551), (567, 567), (56, 589), (569, 568), (700, 55), (701, 56)]
# lis = []
# for i in li:
#     print(i,type(i))
# print(lis)
# str = 'UPDATE staff_table SET dept="Market" WHERE where dept = "IT"'
# print(''.join(str.split('"')[3:4]))
#
# li = [11, 2, 3, 4]
# li[li.index(2)] = 3
# print(li)
#
#
# def fun():
#     li.append(11)
#
#
# fun()
# print(li)


# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from conf import config
#
# with open(config.DBPATH, 'r+', encoding='utf-8') as fi:
#     print(fi.readlines()[-1][0:1])
#     # num = fi.read[-1][:1]


# str = 'UPDATE tab_name SET dept="c" WHERE where dept = "IT"'
# print(''.join(str.split('"')[1:2]))
# li = '7,qing,20,99999999999,c,2016-12-21'
# lis = li.split(',')
# print(lis,type(lis))
# lis[lis.index('c')] = 'aa'
# print(''.join(str.split('"')[1:2]))
# print(lis)
# li = ",".join(lis)
# print(li)

# str = 'select  name,age from staff_table where dept = "IT"'
# print(''.join(str.split()[-1:]).strip('"'))
# print(str.split()[1:2])
# print(len(str.split()[1:2]))
li = [1, 33, 55, 6]

print(list(filter(lambda a: a > 22, li)))