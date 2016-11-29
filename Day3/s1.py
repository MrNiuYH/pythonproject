# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

# import a1
#
# ret = a1.ss1('amen')
#
# a1.ss1(12)
# # a1.ss2()
# # a1.ss3()
#
#
# print("返回值", ret)
# print('------------------')
#
# a1.ss2(3, 4)

# s = "ss %s %%" % ('sb')
# tpl = "i am %(pp).2f %%" % {"pp": 123.425556, }
# print(tpl)
# # i am 123.43 %
# print(s)
# def f1():
#     print(123)
#
# def f2(xxx):
#     xxx()
#
# f2(f1)
#
# f1 = "my-name-is-{name:s}=age=is={age:f}".format(name='niubai', age=24.1)
# print(f1)
#
# f2 = "{:-^s} is {:-d}".format("name", -30)
# print(f2)
# s2 = "----{:*^20s}====={:+d}===== {:x}".format('alex', 123, 15)
# print(s2)

# s1 = "sdasdasd{:.2%}".format(23.444)
# print(s1)
# s2 = "name is {} age is {}".format(*["niu", 23])
# print(s2)

# li = (1, 2, 44, 22, 3)
# def fi(a):
#     if a < 20:
#         return True
# print(list(filter(fi, li)))
# sb = 'aassbsacc'
# print(list(filter(lambda a: a != 's', sb)))
# # map 可用于批量的统一对某个可迭代的对象做操作
# print(list(map(lambda a: a.upper(), sb)))
#
# za = [23,33,4,12,434,33,0]
# aa = list(filter(lambda b: b > 23, za))
# print(aa)
# bb = set(map(lambda b: b+1, za))
# print(bb)

# s = "money is {:^ 20,d}".format(1000000000)
# print(s)
# s = "this is {}".format("string")
# s = "{:-<20d}".format(20)
# s = "{:d} this is Numbers".format(-20)
# s = "this {:20d} lenth".format(10)
# s = "{:-^20d}".format(20)
# s = "{:,d}".format(2000000000)
# s = "{:.2f}".format(12.2323)
# s = "{:#0o}".format(213)
# s = "{:b}".format(23)
# print(s)
# s = "{:o}".format(23)
# print(s)
# s = "{:.2%}".format(0.23)
#
# s = "my name is {},age is {}".format(*["niu", 25])
# s = "my name is {name}, age is {age}".format(**{"name": "niu", "age": 25})
# s = "{:.2%}".format(0.1234)
# print(s)

# li = [23, 43, 100, 34]
#
#
# def fun(i):
#     if i > 29:
#         return True
# print(list(filter(fun, li)))
#
# print(list(filter(lambda i: i > 29, li)))
#
# # s = lambda 参数: 表达式
# a = lambda j: j > 30

# # 生成器   关键词 yield
# '''特点
#         1、找到yield 通过__next__() 方法获取后面的值
#         2、依次从上到下获取，不能回退
#         3、用于循环较大的数据集合，节省内存
# '''
#
#
# def fun1():
#     yield 111
#     yield 222
#
# f = fun1()
# f1 = f.__next__()   # 进入函数，找到yield 并获取yield后面的值
# print(f1)
# f2 = f.__next__()
# print(f2)


# # 递归
# str = "1*2*3*4*5*6*7*8"

# def digui(n):
#     if n == 1:
#         return 1
#     else:
#         return n * digui(n-1)
# result = digui(9)
# print(result)

# import json
# # 序列化 反序列化
# # 1.json
# li = [11, 22, 33, 44]
# st1 = "[12,23,34]"
# l1 = json.loads(st1)

# print(l1)
# print(json.loads(st1), type(json.loads(st1)))
# print(json.dumps(li), type(json.dumps(li)))

# # 自定义模块导入
#
# '''
# 如果在同一级目录下
#     import xxx
# 如果在其他目录下
#     from xxx import xxx
#     from xxx import xxx as xxx
# '''
#
# import sys
# import os
# print(sys.path)
#
# print(os.path.abspath(__file__))
# print(os.path.abspath('a1.py'))
#
# print(os.path.dirname(os.path.abspath('a1.py')))
#
#
# print(os.path.dirname(os.path.dirname(os.path.abspath('a1.py'))))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('a1.py'))))
# for i in sys.path:
#    print(i)
#
import json
import os
# from lib import public as pu
# # json.dump([1, 2, 3], open(os.path.join()))
# print(os.path.abspath(__file__))
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ATM', 'db', 'admin'))
#
# json.dump([1, 2, 3], open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                                        'ATM', 'db', 'admin', 'test'), 'w'))

# print(os.path.join('D:\pythonproject\Day3\ATM', 'db', 'admin', 'test'))
# print(os.path.isfile(os.path.join('D:\pythonproject\Day3\ATM', 'db', 'admin', 'test')))


# di = {'role': 'user', 'phone': '12312312311', 'status': '0', 'card': '6222021415855153',
#       'passwd': 'e10adc3949ba59abbe56e057f20f883e', 'quota': '9000', 'uname': 'wang'}
#
# li = di.items()
#
# print(li)
# for i in li:
#     print(i)







