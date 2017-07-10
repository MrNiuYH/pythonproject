# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
# Date: 2017/5/9

menu = {
    'phone': {
        'iphone': {
            'iphone7': {"6500", "64G"},
            'iphone6': {"5500", "64G"},
            'iphone3gs': {"停产", "无"}
        },
        '三星': {
            'C5': {"2500", "8G"},
            'S7': {"5688", "16G"},
            'A8': {"1588", "2G"}
        },
        '华为': {
            '荣耀8': {"2200", "4G"},
            'Note': {"1099", "无"},
            '畅玩5A': {"799", "无"}
        }
    },
    'computer': {},
    'car': {}
}
lis = []
while True:
    for key in menu:
        print(key)
    userinput = input("input>>:").strip()
    if userinput == 'b':
        if len(lis) == 0:
            break
        menu = lis[-1]
        lis.pop()
    if len(userinput) == 0 or userinput not in menu:
        continue
    lis.append(menu)
    menu = menu[userinput]
