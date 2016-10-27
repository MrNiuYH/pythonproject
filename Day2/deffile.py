# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

'''
def sendmail():
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText('邮件正文，我不想和你啪啪啪', 'plain', 'utf-8')
        msg['From'] = formataddr(['Mr.niu', 'tongyongc0m@163.com'])
        msg['To'] = formataddr(["NIma", '853499733@qq.com'])
        msg['Subject'] = "老子是主题"

        server = smtplib.SMTP('smtp.163.com', 25)
        server.login('tongyongc0m@163.com', '1qazxsw2')
        server.sendmail('tongyongc0m@163.com', ['853499733@qq.com', ], msg.as_string())
        server.quit()
    except:
        # 发送失败返回值
        return "shibai"
    else:
        # 发送成功返回值
        return "chengg"
rev = sendmail()
if rev == "chengg":
    print("cg")
else:
    print("shib")
'''
'''
# 普通参数
def get_v(b):
    a = b + 2
    return a
print(get_v(6))

# 默认参数
def get_a_b(a, b, c = "didi"):
    print(a, b, c)
get_a_b(5, 21)
get_a_b(5, 21, "baba")

# 指定参数
get_a_b(b=21, a=5, c="lili")

# * 可接收动态参数
def get_all_v(*value):
    print(value)

get_all_v(23)   # (23,)
li = [23, 445, 66, "dsad"]
get_all_v(li)   # ([23, 445, 66, 'dsad'],)
get_all_v(li, 34)   # ([23, 445, 66, 'dsad'], 34)
men = {"key1": "v1", "k2": "v2"}
get_all_v(*li)   # (23, 445, 66, 'dsad')
get_all_v(*li, 34)  # (23, 445, 66, 'dsad', 34)
get_all_v(*men)     # ('k2', 'key1')


def get_all_w(**value):
    print(value)
v2 = [23, 543, 66]
get_all_w(k1="v1")  # {'k1': 'v1'}
get_all_w(k2=v2)    # {'k2': [23, 543, 66]}

dic = {"k1": "v1", "k2": "v2"}
get_all_w(**dic)    # {'k1': 'v1', 'k2': 'v2'}

def get_all_a(*v, **v1):
    print(v)
    print(v1)
get_all_a(11, 2, 33, k1="v1", k2="v2")  # (11, 2, 33) {'k1': 'v1', 'k2': 'v2'}


li = ["niu", 20]
dic = {"name": "niu", "age": 28}
s1 = "name is {0}, age is {1}".format("niu", 20)
print(s1)
s1 = "name is {0}, age is {1}".format(*li)
print(s1)
s2 = "name is {name}, age is {age}".format(
    name="niu",
    age=28
)
print(s2)
s2 = "name is {name}, age is {age}".format(**dic)
print(s2)
'''
# def li_append(li):
#     li.append("ddd")
# lis = [11, 22, 33, 44]
# li_append(lis)
# print(lis)  # [11, 22, 33, 44, 'ddd']
'''
# 文件操作

# 打开文件，
# 操作文件，
# 关闭文件

# 打开文件 （加b 表示以字节方式进行读写 rb、wb、xb、ab）

# 单独的 只读只写模式
f = open('file', 'r')  # 只读
f = open('file', 'w')  # 只写，清空文件写入
f = open('file', 'x')  # 如果文件存在，报错，不存在 创建并写入
f = open('file', 'a')  # 追加

# 文件操作
# + 表示可以同时读写文件
f = open('file', 'w+')  # 清空文件后读写
f = open('file', 'x+')  # 如果文件存在，报错，不存在 创建并写入
f = open('file', 'a+')  # 读写
f = open('file', 'r+', encoding='utf-8')  # 读写 常用
# 如果没有b 读取则按照 字符来读取，如果包含字符串，写入时可能会乱码
print(f.read(2))    # read 无参数，读全部  有参数 读取有b就按照字节读取，无则按照字符读取
f.readline()    # 读取一行
# 获取当前指针的位置（根据字节获取）
f.tell()
# 调整指针的位置（根据字节调整）
f.seek(7)
# 截断，只保留指针前面的文件
f.truncate()
# 根据指针位置 向后覆盖，不会改变总体长度
f.write("sss")
f.flush()   # 强制写入

f.close()   # 关闭文件
with open('file') as f:     # pass 代码块，结束后自动关闭
    pass
'''
'''
# 三元运算  如果表达式成立 name就赋值为前面的值，不成立就赋值为后面的值
name = "niu" if 1 > 3 else "wang"
print(name)

# lambda 表达式
def lam(a):
    return a + 1

t = lambda a: a+1
# t 函数名   a 为参数  a+1 表达式
print(t(6))     # 7

# 内置函数
# abs() 取绝对值
print(abs(-1))  # 1
# all() 函数内部参数全部为真则为真
print(all([1, -1, 2, -2, 3]))   # true
print(all([1, -1, 2, -2, 0]))   # false
print(all([1, -1, "", {}, (), []]))    # false
# any  一个为真便为真
print(any((1, 0, "", {}, (), [], None)))    # true
# bool 判断真假。返回true or false
print(bool(1))  # true
# bin() 数字十进制转2进制
print(bin(8))   # 0b1000
# oct() 数字十进制转八进制
print(oct(9))   # 0o11
# hex() 数字十进制转十六进制
print(hex(10))  # 0xa

# utf-8  一个汉字 占三个字节
# gbk 一个汉字 占两个字节
# 字符串转换成字节
print(bytes('汉字', encoding='utf-8'))
print(bytes('汉字', encoding='gbk'))
# 字节转换成字符串
s = str(bytes('字符串转换成字节', encoding='utf-8'), encoding='utf-8')
print(s)
'''

'''20161009'''
# Ascii码对照值
c = chr(77)
print(c)
o = ord("c")
print(o)

# Ascii码应用生成5位随机验证码
'''
import random   # random 生成随机数
# li = []
# for i in range(1, 6):
#     c = random.randrange(97, 123)
#     letter = chr(c)
#     li.append(letter)
# ls = "".join(li)
# 生成5位随机验证码 优化版
li = []
for i in range(1, 6):
    ran = random.randrange(0, 5)
    if ran == 1 or ran == 2:
        c = random.randrange(0, 10)
        li.append(str(c))
    else:
        c = random.randrange(65, 91)
        letter = chr(c)
        li.append(letter)
ls = "".join(li)
print(ls)
'''

# compile() 将字符串转换成python代码
# 例如
s = "print('abc')"
py = compile(s, '<string>', 'exec')
print(py)   # abc
exec(py)

# exec() 执行python代码，可接收字符串(会先内部转换成python代码再执行)或者python代码，没有返回值
exec(s)     # abc

# eval()    # 执行 表达式 并有返回值
ev = eval("1+2")
print(ev)   # 3

# dir()  查看对象提供了哪些功能
# help() 查看对象提供的功能及源码
# divmod() 取商及余数
di1, di2 = divmod(10, 3)
print(di1, di2)
# enumerate() 多用于循环中，
list1 = ["这", "是", "一个", "测试"]
for i in enumerate(list1):
    print(i[0], i[1])
# isinstance() 判断定义的对象是否是指定类的实例
isi = isinstance([11, 22, 33], list)
isi1 = isinstance([11, 22, 33], dict)
print(isi, isi1)

# filter 筛选
# filter(函数，可迭代的对象(可以for循环))  内部做循环，循环第二个可迭代的对象，传给第一个函数执行，
# 返回true则
li = (1, 2, 44, 22, 3)
def fi(a):
    if a < 20:
        return True
print(list(filter(fi, li)))
s = 'aassbsacc'
print(list(filter(lambda a: a != 's', s)))
# map 可用于批量的统一对某个可迭代的对象做操作
print(list(map(lambda a: a.upper(), s)))

# globals()   获取所有的全局变量
# locals()    获取所有的局部变量

# hash() 把给定的值转换成一个hash值
# max()最大值   min()最小值   sum()求和  pow()求次方  round()四舍五入
# reversed() 反转

