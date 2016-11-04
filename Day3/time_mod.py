# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import time
print(time.time())  # 时间戳
print(time.gmtime())    # 将时间戳格式转换成 struct时间对象格式
print(time.mktime(time.localtime()))    # 将struct时间对象格式转换成时间戳格式
print(time.localtime())     # struct时间对象格式
print(time.asctime())   # 时间  Fri Nov  4 16:26:26 2016  格式
print(time.asctime(time.localtime()))   # Fri Nov  4 16:26:26 2016
print(time.ctime())     # Fri Nov  4 16:26:26 2016
str_to_struct = time.strptime('2016-11-04', '%Y-%m-%d')  # 将字符串格式日期转换成struct时间对象格式
print(str_to_struct)
struct_to_str = time.strftime('%Y/%m/%d', str_to_struct)    # 将struct时间对象格式转换成字符串格式
print(struct_to_str, type(struct_to_str))   # 2016/11/04 <class 'str'>
print(time.strftime('%Y-%m-%d %H:%M'))    # 2016-11-04  默认当前时间

import datetime
'''
datetime.date   # 表示日期的类  Y-m-d
datetime.time   # 表示时间的类  H-M-S
datetime.datetime   # 表示日期时间 格式
datetime.timedelta  # 表示时间间隔
datetime.timedelta() 参数可以是 days hours minutes 正数表示在当前的时间上减去这个值，负数表示在当前的时间上加这个值
'''
print(datetime.datetime.now())  # 2016-11-04 16:45:34.198335
print(datetime.datetime.now()-datetime.timedelta(days=1))   # 2016-11-03 16:45:34.198335
print(datetime.datetime.now()-datetime.timedelta(days=-1))   # 2016-11-05 16:47:40.853278
print(datetime.datetime.now()-datetime.timedelta(hours=1))   # 2016-11-04 15:47:40.853278
print(datetime.datetime.now().replace(2016, 12, 2))     # 更改时间 时间替换


