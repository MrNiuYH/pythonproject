# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu


# c = (x * 3 for x in range(9))
# print(c)    # <generator object <genexpr> at 0x000001DF2D992DB0>
#
# d = [y * 3 for y in range(4)]   # 列表生成式
# print(d)    # [0, 3, 6, 9]


# 生成器 generator   可以在函数执行的过程中执行其他操作
'''
生成器本身也是一个函数，加上yield就变成了一个生成器,执行只能通过next一步步执行
一般函数执行的时候都是一次性把整个函数执行完才能去执行其他的命令，而生成器是可以自由的进出函数内部，在执行过程中增加其他操作
'''
# example：

# 普通函数
def fun():
    for i in range(4):
        print(i)

fun()   # 0 1 2 3
# 生成器函数,需要调用next才能一步步执行


def test1():
    for j in range(3):
        print(j)
        yield

yi = test1()    # test1() = <generator object test1 at 0x00000272AD062DB0> 生成器对象
yi.__next__()
print("做点其他事情")
yi.__next__()


# 生成器捕获异常方法

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b     # 相当于 c = (b, a+b)  a = c[0] b=c[1]
        n += 1
    return 'done'   # 直接使用__next__函数，如果调用的次数超过应有的次数，就会抛一个异常StopIteration，return指定报异常的值

fi = fib(5)
# try except 捕获error 并自定义 error 输出的警告代码， except 后指定报错的类型（StopIteration）
while True:
    try:
        x = next(fi)
        print(x)
    except StopIteration as e:
        print('Error code return value', e.value)
        break
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())
# print(fi.__next__())


