# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import os

LISTMSG = '''
---------------------------------------
请根据需求选取对应的功能序号进行详细操作哦！

1、查询员工信息
2、添加员工信息
3、删除员工信息
4、更新员工信息
5、退出
---------------------------------------
'''

ADDUSERMSG = '''
已添加成功，你添加的用户信息为,请核实:
id:{:6}  name:{:13}
age:{:6} phone:{:13}
dept:{:6}enroll_date:{:13}
'''

USERMSG = '''
以下是员工详细信息，请输入对应的序号进行相应操作
-------------------------------------------
id name   age phone        dept enroll_date'''

PRINTMSG = '''表名为tab_name 格式如：UPDATE tab_name SET dept="Market" WHERE where dept = "IT"'''

DBPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'userinfor')
DBPATH_BAK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'userinfor.bak')

TYPEMSG = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']

ERRMSG = "字段错误!!"
