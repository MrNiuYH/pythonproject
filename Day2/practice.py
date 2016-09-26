# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

# # set集合    无序，不重复序列
#
# li = [11, 22, 33, 11, 22, 33]
# # 类后面加个（） 就会执行类内部的一个_init_ 方法
# # list(), str(), dict(), set()
# # 创建集合
# se = {11, 22, 33}
# print(type(se))
#
# s = set()  # 创建一个空的集合
# s3 = set(li)  # 转换出一个集合
# print(s3)   # {33, 11, 22}
#
# # 操作集合
# s = set()
# s.add(123)
# print(s)
# s.clear()
# print(s)
#
# s1 = {11, 22, 33}
# s2 = {22, 33, 44}
#
# s3 = s1.difference(s2)   # A中存在，B中不存在
# print(s3)   # 11
# s4 = s1.symmetric_difference(s2)    # A中存在，B中不存在的值和 B中存在，A中不存在的值
# print(s4)   # {11, 44}
#
# s1.difference_update(s2)   # A中存在，B中不存在的值更新到新的集合中
# print(s1)   # {11}
# s2.symmetric_difference_update(s1)     # 差集更新到s2
# s3 = s1.intersection(s2)    # 交集
# s1.intersection_update(s2)  # 交集更新到s1
# s5 = s1.union(s2)   # 并集
# print(s5)
# print(s2)   # {11, 44}
# s1.discard(2222)    # 移除指定元素，不存在不报错
# s1.remove(222)  # 移除指定元素， 不存在报错
# new = s1.pop()    # 无参数，随机移除,并返回移除的值
# lis = [1, 3, 4, 6, 6]
# s1.update(lis)     # 迭代更新，相当于多次添加
# print(s1)
# old_dict = {
#     "1": 8,
#     "2": 4,
#     "4": 2
# }
# new_dict = {
#     "1": 4,
#     "2": 4,
#     "3": 2
# }
# old_set = set(old_dict.keys())
# new_set = set(new_dict.keys())
#
# remove_set = old_set.difference(new_dict)   # 应该删除的
# add_set = new_set.difference(old_set)   # 应该增加的
# update_set = new_set.intersection(old_set)  # 应该更新的
#
# print(remove_set,add_set,update_set)
#
# for i in remove_set:
#     old_dict.pop(i)
#     # del old_dict[i]
#
# print(old_dict['2'])
# print(new_set)
# for i in add_set:
#     old_dict[i] = new_dict[i]
#
# for i in update_set:
#     old_dict[i] = new_dict[i]
#
# print(old_dict)
