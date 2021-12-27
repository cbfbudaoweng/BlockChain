# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/12 20:32
# @File    : getExcelIndex.py
# @Software: PyCharm

import pandas as pd


class GetExcelIndex:
    # 获取某单元格值的行号
    def find_row(self, file_name, sheet_name, cell_value):
        demo_df = pd.read_excel(file_name, sheet_name)  # 读取某文件的某sheet表格
        for indexs in demo_df.index:
            for i in range(len(demo_df.loc[indexs].values)):
                if (str(demo_df.loc[indexs].values[i]) == cell_value):
                    row = str(indexs + 2).rstrip('L')
                    return int(row)  # 这里的row的str型，强转为int型

    # 获取某单元格值的坐标
    def find_index(self, filename, sheet_name, num_value):
        data = pd.read_excel(filename, sheet_name)  # 读取某文件的某sheet表格
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                # print(data.iloc[i,j])
                if data.iloc[i, j] == num_value:
                    print("坐标是iloc(%d,%d)" % (i + 2, j + 1))  # i+2是因为还需要加上表头一行
                    return i + 2, j + 1  # 返回行号和列号,返回的就是int型
                    break

