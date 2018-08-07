# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
# Date: 2018/8/3


"""
面向对象：
类
object 对象

 特性： 封装
 继承
 多态
"""


# class Dog (object):
#     print("hello")
#
#
# class Sayhi (object):
#     def shuo(self):
#         print("say hello")
#
#
# d = Sayhi
# print(d)    # 内存地址
#
# d.shuo()    # say hello

# # 类的定义
# class Women(object):
#     naf = "China"    # 公有属性，在类里面直接定义
#
#     def __init__(self, name):   # 构造函数
#         self.Name = name    # 成员属性
#         self.__heart = "ok"     # 私有属性,类内部访问，如需要外部可以访问，可以用个方法return出去，只读
#
#     def rut(self):
#         return self.__heart
#
#     def Spee(self):
#         print("hello, my name is", self.Name)
#
#     def Eat(self, food):
#         print("%s eat food is %s status is %s" % (self.Name, food, self.__heart))
#         print('''name:{_name},food:{_food},heart:{_heart}'''.format(_name=self.Name, _food=food, _heart=self.__heart))
#         print("{0},{1}".format(self.Name, food))
#         print("{},{}".format(*[self.Name, food]))
#         print("{name},{fd}".format(**{"name": self.Name, "fd": food}))
#
#
#
# d = Women
# print(d)
#
# r1 = Women("zhang")     # 实例化
# r2 = Women("li")
# r1.Spee()
# r2.Eat("appale")
# print(r1.rut())
#
# print(r1._Women__heart)     # 强制访问私有属性
# Women.naf = "CN"    # 更改公有属性


# 封装
# 析构方法(析构函数)


# 继承
# # 1、继承不传参

print("---------------------继承不传参-----------------------")


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.eys = "big"

    def seleep(self):
        print("person need to sleep....")

    def eat(self):
        print("person need to eat....")

    def speek(self):
        print("person will talk")


class YelloPerson(Person):  # 继承父类
    def walk(self):
        print("person....")


yp = YelloPerson("zhang", 23)    # 实例化子类

print(yp.age)
yp.seleep()     # 子类可以调用父类的方法及参数，也可以调用自己的方法
yp.walk()


# # 2、继承传参
print("---------------------继承传参-----------------------")


class WritePerson(Person):
    def __init__(self, name, age, sex):     # 先继承 再重构
        Person.__init__(self, name, age)
        self.sex = sex


wp = WritePerson("ba", 23, "good")
print(wp.sex, wp.eys)
wp.seleep()

# 多态

