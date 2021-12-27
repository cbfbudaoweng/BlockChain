# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/8 10:28
# @File    : baseapi.py
# @Software: PyCharm

import json
import os
import requests

class BaseApi:

    def send_requests(self, req: dict):
        return requests.request(**req)

    # 把字符串转换成json，即基于string将string转成dict
    def json_loads(self, string):
        return json.loads(string)

    # 把字典转为字符串
    def json_dumps(self, dict):
        return json.dumps(dict,ensure_ascii=False)


    # # 创建txt文件
    # def create_file(self, file):
    #     if os.path.exists(file):  # 如果file文件已存在
    #         os.remove(file)  # 则先移除该文件
    #     return open(file, mode='w', encoding='utf-8')  # 创建文件，并向文件中写入内容
    #
    # # 读取txt文件
    # def read_file(self, file):
    #     f = open(file, mode='r', encoding='utf-8')  # 打开并读取文件
    #     return f.read()
    #
    # # 读取本地txt文件
    # def readtxt(self, file):
    #     with open(file, 'r', encoding='utf-8') as f:
    #         while True:
    #             line = f.readline()
    #             if line:
    #                 return line
    #             else:
    #                 break

    # # 把文件打开，把里面的字符转换成数据类型
    # def json_load(self, file):
    #     return json.load(file)
    #


