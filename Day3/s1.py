# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import a1

ret = a1.ss1('amen')

print("返回值", ret)
print('------------------')

a1.ss2(3, 4)

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

li = [23, 43, 100, 34]


def fun(i):
    if i > 29:
        return True
print(list(filter(fun, li)))

print(list(filter(lambda i: i > 29, li)))

# s = lambda 参数: 表达式
a = lambda j: j > 30
