# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Mr.Niu

# ========================================================================
import logging

# 输入到文件中，不显示在屏幕上
logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H%M:%S')

# logging 日志记录的几个等级，从低到高
logging.debug('debug')
logging.info('info')
logging.warning("user [niu] 66666")
logging.error('error')
logging.critical("66666666")
# ========================================================================



# 自定义输出日志文件到文本或者当前屏幕

'''
    1、先定义一个logging
    2、定义一个handler
    3、定义一个formatter
    4、添加formatter格式到handler
    5、添加handler 到 logging
'''

import logging

# logger 提供可以直接使用的接口
# handler 将logger创建 的日志记录发送到指定的地方
# formatter 决定日志记录的最终输出格式

# 创建一个logger      一个logger可以附加多个handler
logger = logging.getLogger('errlog')
logger.setLevel(logging.DEBUG)  # 定义一个logger接口的全局日志等级


# 创建一个 handler 并定义handler的日志等级  streamhandler 输出到 屏幕
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.WARNING)

# 创建一个 handler  并定义日志等级       filehandler  输出到日志文件
f_handler = logging.FileHandler('error1.log')
f_handler.setLevel(logging.INFO)


# 创建一个formatter  定义日志输出格式
formatter = logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
f_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 添加 formatter 日志格式到handler
s_handler.setFormatter(formatter)
f_handler.setFormatter(f_formatter)

# 将 handler 添加到 logger
logger.addHandler(s_handler)
logger.addHandler(f_handler)


# 自定义的日志输出
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


