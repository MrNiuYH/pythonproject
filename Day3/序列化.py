# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

# 序列化 反序列化
#  json pickle 差异
'''
 json 适合跨语言序列化，只支持字符串 与 基本类型的序列化转换
 pickle 只适用于python，更适合所有类型的序列化
'''

# 1.json

import json
li = [11, 22, 33, 44]
st1 = "[12,23,34]"

# json.loads() loads 将字符串转换为py基本格式类型
print(json.loads(st1), type(json.loads(st1)))
# json.dumps() dumps 将py基本类型转换为字符串类型
print(json.dumps(li), type(json.dumps(li)))

# json.dump dump 1、将基本数据类型转换为字符串类型 2、把转换的字符串写入到文件
json.dump(li, open('db', 'w'))
# json.load load 1、读取文件内容 2、转换成py的基本格式类型
lo = json.load(open('db', 'r'))
print(lo, type(lo))

# 获取天气
# requests 模块 类型linux的wget
import requests
re = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
re.encoding = 'utf-8'

dic = json.loads(re.text)
print(dic, type(dic))


# 2.pickle
import pickle

l2 = [2, 3, 3, 4]
s2 = pickle.dumps(l2)
print(s2, type(s2))     # b'\x80\x03]q\x00(K\x02K\x03K\x03K\x04e.' <class 'bytes'>  转换为字节类型
li2 = pickle.loads(s2)
print(li2, type(li2))

pickle.dump(l2, open('db', 'wb'))   # 将源类型转换成字节类型，并写入到文件
pickle.load(open('db', 'rb'))   # 读取文本内容，并将字节转换成源类型
