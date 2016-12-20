# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import os
import sys

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

USERMSG = '''
以下是员工详细信息，请输入对应的序号进行相应操作
-------------------------------------------
id name   age phone        dept enroll_date'''

PRINTMSG = '''表名为tab_name 格式如：UPDATE tab_name SET dept="Market" WHERE where dept = "IT"'''

DBPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'userinfor')
DBPATH_BAk = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'userinfor.bak')

