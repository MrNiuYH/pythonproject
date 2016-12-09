# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

from collections import Iterable
from collections import Iterator
# Iterable 迭代对象（可循环的对象）
'''
string、列表、集合、元组、字典、generator生成器
'''

# Iterator 迭代器对象 可以被next()函数调用并返回下一个值的对象 （对象有next方法就成为迭代器对象：例如：a=[1,2,3],
# dir(a)不包含next方法，就不是迭代器对象），可以用isinstance判断是否是
print(isinstance([], list))  # True
print(isinstance([], Iterator))  # False

# 迭代对象可以通过iter()函数转换为 迭代器对象
print(isinstance(iter([]), Iterator))   # True
