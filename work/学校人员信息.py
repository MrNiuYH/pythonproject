# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
# Date: 2018/8/7


class SchoolPersonalInformation(object):
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        """注册"""
        print("%s is registered successfully..." % self.name)
        SchoolPersonalInformation.member += 1

    def tell(self):
        """打印个人信息"""
        print("-------info:%s" % self.name)
        for k, v in self.__dict__.items():
            print(k, v)

    def __del__(self):
        """析构函数:Python垃圾回收的时候会被调用"""
        SchoolPersonalInformation.member -= 1


class Tearcher(SchoolPersonalInformation):
    """讲师类"""
    def __init__(self, name, age, sex, salary):
        """构造函数"""
        SchoolPersonalInformation.__init__(self, name, age, sex)    # 经典类写法
        super(Tearcher, self).__init__(name, age, sex)      # 新式类写法
        self.salary = salary

    def teach(self):
        """授课功能"""
        print("The teacher %s is teaching in the classroom, salary is %s " % (self.name, self.salary))


class Student(SchoolPersonalInformation):
    """学生类"""
    def __init__(self, name, age, sex, tuition):
        SchoolPersonalInformation.__init__(self, name, age, sex)
        self.tuition = tuition

    def pay_tuition(self):
        print("student %s has just paied %s" % (self.name, self.tuition))


t1 = Tearcher("laoli", 34, 'nan', "python")


s1 = Student("xiaoliu", 21, "nv", 3000)

print(SchoolPersonalInformation.member)
print(t1.__dict__)
print(t1.tell())

