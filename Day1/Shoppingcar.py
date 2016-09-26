# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import os, pickle, time

Bool = bool(True)
'''获取已存在的用户，如不存在 赋值为空'''
if os.path.exists(r'user_mess.pkl'):
    pkl_file = open('user_mess.pkl', 'rb')
    reg_user = pickle.load(pkl_file)
    pkl_file.close()
else:
    reg_user = {}
'''获取用户的历史购物列表'''
if os.path.exists(r'usershoplist.pkl'):
    dirc = open('usershoplist.pkl', 'rb')
    hist_dic = pickle.load(dirc)
    dirc.close()
else:
    hist_dic = {}
shopping_car = {
    "iphone": {1: ["iphone", 6888, 5], 2: ["ipad", 4000, 8], 3: ["Samsung", 3000, 3]},
    "variety": {1: ["headset", 50, 5], 2: ["usb_cable", 18, 8], 3: ["teacup", 60, 30]},
    "clothing": {1: ["coat", 900, 5], 2: ["pants", 110, 8], 3: ["shoes", 300, 3]}
    }
shop_history = {}
temporary_list = []
dict1 = {}
print("欢迎来到购物商城".center(50, '*'))
count = 0
True_False = 'True'
input_value = input("登录输入1，注册输入2，退出输入q:")

if input_value.isdigit():   # 判断输入的是否是数字
    if int(input_value) == 1:   # 登录流程
        while True_False:
            register_name = input("用户名：")
            register_pwd = input("密  码：")
            if register_name in reg_user.keys() and register_pwd == reg_user[register_name]['pwd']:
                print("登录成功".center(40, '-'))
                True_False = False
            else:
                count += 1
                if count == 3:
                    exit("多次输入错误，退出程序")
                else:
                    print("******************************")
                    print("用户名或者密码错误！请重新输入.")
                    print("******************************")
    elif int(input_value) == 2:     # 注册流程
        while True_False:
            register_name = input("用户名：")
            register_pwd = input("密  码：")
            register_sal = input("存入金额：")
            if register_name in reg_user.keys():    # 判断用户名是否存在，存在重新输入，不存在注册成功，进入商城
                print("用户已存在！重新输入")
            else:
                if register_sal.isdigit():
                    reg_user[register_name] = {"pwd": register_pwd, "money": register_sal}
                    user_val = open('user_mess.pkl', 'wb')
                    pickle.dump(reg_user, user_val)
                    user_val.close()
                    print("注册成功！".center(50, '-'))
                    True_False = False
                else:
                    count += 1
                    if count == 3:
                        exit("多次输入错误，退出程序")
                    else:
                        print("存钱失败！输入正确的数字")
    else:
        exit("输入错误！")
elif input_value == "q":
    if temporary_list:
        for i in temporary_list:
            print(i)
    else:
        print("本次没有购买任何商品哦！")
    exit("谢谢您的光顾，欢迎再来")
else:
    exit("Please enter the Numbers")
'''打印用户历史购物列表'''
if register_name in hist_dic.keys():
    print("上次的购物列表")
    for i in hist_dic[register_name]:
        print(i)
'''更新用户信息'''
def update_usermessage(Salary):
    reg_user[register_name]["money"] = Salary
    user_val = open('user_mess.pkl', 'wb')
    pickle.dump(reg_user, user_val)
    user_val.close()

'''更新用户已购列表'''
def update_shophist(hist_list):
    if temporary_list:
        shop_history[register_name] = temporary_list
        file_obj = open('usershoplist.pkl', 'wb')
        pickle.dump(shop_history, file_obj)
        file_obj.close()
'''充值'''
def Recharge(Salary, Money):
    if Money.isdigit():
        Salary += Money  # 更新用户金额
        print("充值成功，现在余额为\033[31;1m [s] \033[0m" % Salary)
        update_usermessage(Salary)
    else:
        print("充值失败")

'''打印已购商品'''
def print_list():
    if temporary_list:
        print("已购买的商品".center(50, '='))
        print("商品名    数量  金额      购买时间")
        for i in temporary_list:
            print(i)
        print("".center(50, '='))
    else:
        print("本次没有购买任何商品哦！")

Salary = int(reg_user[register_name]["money"])
print("购物车欢迎你 %s ,你的账户余额为%s" % (register_name, Salary))
print("============================================")
while not True_False:
    for i in enumerate(shopping_car):  # 打印商品列表
        print(i[0] + 1, '.', i[1])
        dict1[i[0]] = i[1]
    print("============================================")
    print("(1)退出输入 \033[31;1m q\033[0m")
    print("(2)充值输入 \033[31;1m r\033[0m")
    print("(3)查看详细商品输入类型编号")
    select_type = input("请输入:")
    if select_type == "q":   # 退出并更新 用户信息
        update_usermessage(Salary)
        print_list()
        exit("欢迎下次光临")
    if select_type == "r":
        top_up = input("输入充值金额：")
        if top_up.isdigit():
            Salary += int(top_up)  # 更新用户金额
            print("充值成功，现在余额为\033[31;1m [%s] \033[0m" % Salary)
            update_usermessage(Salary)
        else:
            print("充值失败")
        continue
    if select_type.isdigit():
        if int(select_type) in (1, 2, 3):
            BIAN = int(select_type) - 1
            for j in shopping_car[dict1[BIAN]]:
                print(j, ':', shopping_car[dict1[BIAN]][j])
            print("********************************")
            print("(1)输入\033[31;1m b\033[0m 返回上一层")
            print("(2)输入\033[31;1m s\033[0m 查询已购列表")
            print("(3)输入\033[31;1m q\033[0m 退出")
            print("(4)输入商品对应的序号，自动购买商品！")
            print('-------------------------------')
            Num = input("请输入:")
            if Num == "b":
                continue
            if Num == "q":  # 如果选择退出，则判断购物车是否为空，不为空就写入到文件
                print_list()
                update_usermessage(Salary)
                exit("谢谢您的光顾，欢迎再来")
            if Num == "s":  # 选择查询，列表不为空就打印，空就提示
                if temporary_list:
                    print("已购买的商品%s,余额为%s" % (temporary_list, Salary))
                else:
                    print("购入车空空如也！赶紧去购物吧！")
            elif Num.isdigit() and int(Num) <= len(shopping_car[dict1[BIAN]]) and int(Num) != 0:  # 购物
                shop_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                Get_num = shopping_car[dict1[BIAN]].get(int(Num))[2]  # 获取剩余件数
                Select_Digit = input("本商品一共 %s 件,你想要购买几件:" % Get_num)  # 选择输入几件
                if Select_Digit.isdigit() and Get_num >= int(Select_Digit):
                    price = shopping_car[dict1[BIAN]].get(int(Num))[1]
                    price_sum = price * int(Select_Digit)
                    if price_sum <= int(Salary):  # 判断剩余金额是否足够
                        Salary = int(Salary) - price_sum  # 更新余额
                        shopping_car[dict1[BIAN]][int(Num)][2] = int(Get_num) - int(Select_Digit)
                        temporary_list.append((shopping_car[dict1[BIAN]].get(int(Num))[0], Select_Digit,
                                               price_sum, shop_time))  # 购物信息插入列表，供查询
                        print("购买成功")
                        update_shophist(temporary_list)
                        sel_con = input("继续购物输\033[31;1m c \033[0m，退出输\033[31;1m q \033[0m，"
                                        "充值按\033[31;1m r \033[0m，""查看已购列表输 \033[31;1m s \033[0m:")
                        if sel_con == "c":
                            pass
                        if sel_con == "q":
                            update_usermessage(Salary)
                            print_list()
                            print("谢谢您的光顾，欢迎再来")
                            True_False = True
                        if sel_con == "r":
                            top_up = input("输入充值金额：")
                            if top_up.isdigit():
                                Salary += int(top_up)  # 更新用户金额
                                print("充值成功，现在余额为\033[31;1m [%s] \033[0m" % Salary)
                                update_usermessage(Salary)
                            else:
                                print("充值失败")
                        if sel_con == 's':
                            print_list()
                    else:
                        print('-------------------------------------')
                        print("你的余额为 \033[31m;%s\033[0m，余额不足，请充值后再购买！也可以选择价格便宜的购买" % Salary)
                        print('-------------------------------------')
                        if_top_up = input("是否充值？充值输入1，不充值按任意键")
                        if if_top_up == "1":
                            top_up = input("输入充值金额：")
                            if top_up.isdigit():
                                Salary += int(top_up)  # 更新用户金额
                                print("充值成功，现在余额为\033[31;1m [%s] \033[0m" % Salary)
                                update_usermessage(Salary)
                            else:
                                print("充值失败")
                else:
                    print("请输入正确的件数，并且最大不能超过库存的商品件数！")
            else:
                print("请输入正确的商品序号！")
        else:
            print("无此编号")
    else:
        print("输入错误")




