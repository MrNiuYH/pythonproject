#!/usr/bin/env python
# -*- coding: utf-8 -*-


# name = ["niu", "ki", "wang", "zhu", [5, 6, 7, 3], 3, 4, 223, 4553, 554, "wang", 7, "张", 3, 9, 3]
# name2 = [3, 4, 45]

# name1 = name.copy()
# # 找出有多少个3 改成301
# for i in range(name.count(3)):
#     NameIndex = name.index(3)
#     name[NameIndex] = 301
# print(name)
# # 找出所有wang 删除掉
#
# for j in range(name.count("wang")):
#     name.remove("wang")
#     # Windex = name.index("wang")
#     # name.pop(Windex)  #
# print(name)
#
# print("name", len(name))  # 查看列表长度

# name.reverse()
# name1.pop()
# print(name)
# print(name1)
# print("-------------")
# InDex = name1.index("zhu")
# print(InDex)
# del name[3]
# print(name)
# print(name.count(3))
# name.remove(3)
# print(name)

# 元组
# dictionary = (1, 2, 3, 4)
# print(dictionary.count(1))
# print(dictionary.index(2))

#字符串操作
#去掉空格  strip () 括号内可指定 默认是空格
username = input("username:")
if username.strip('-') == "zhang":
    print(username.strip('-'))
    print("welcome %s to beijing" % username)

# 分割 split 可指定根据什么分割
list11 = "welcome to beijing"
list2 = list11.split()
print(list2)  # ['welcome', 'to', 'beijing']
# 合并 join 可指定根据什么合并
list3 = ":".join(list2) + '\n'  # welcome:to:beijing
list4 = " ".join(list2)  # welcome to beijing
print(list3, list4)

# 判断有没有空格\切片
name = "mr,niu"
print("," in name)
name1 = "mr niu"
print(" " in name1)
print(name[2:4])

# format 字符串格式化

men = "my name is {name}, age is {age}"
all = men.format(name="niu", age=23)

men1 = "my name is {0}, age is {1}"
all1 = men1.format("niu", 23)
print(all1)

fill = "niu"
fill.isdigit()  # 判断是不是数字
fill.endswith('')  # 判断是不是以指定字符串结尾
fill.startswith('')  # 判断是不是以指定字符串开头
print(fill.upper())  # 改大写
print(fill.lower())  # 改小写
print(fill.center(20, '='))

