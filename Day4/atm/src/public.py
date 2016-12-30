# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

import os


def get_file_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


bb = get_file_path()
print(bb)