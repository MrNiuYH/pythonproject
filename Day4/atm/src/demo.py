# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import public


def get_file():
    return json.load(open(os.path.join(public.get_file_path(), 'db', 'admin'), 'r', encoding='utf-8'))


def acc_file(*args):
    if get_file():
        da = get_file()
        if args[0] == da["name"] and args[1] == da["passwd"]:
            return da


