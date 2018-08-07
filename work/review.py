# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
# Date: 2018/8/2


import subprocess

# print(subprocess.run(["ipconfig", "/all"]))

recode = subprocess.Popen(["ipconfig|grep 192"], shell=True, stdout=subprocess.PIPE)
print(recode)

da = {
    "name": 1,
    "age": 2
}
print(da["age"])


