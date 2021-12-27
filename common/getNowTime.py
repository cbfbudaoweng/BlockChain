# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/12 19:32
# @File    : getNowTime.py
# @Software: PyCharm
import time


class getNowTime():
    def get_now_time(self):
        ticks = time.time()  # 获取当前时间戳
        # 格式化成2016-03-20 11:45:39形式
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(ticks)
        # print(data_time)
        return now_time