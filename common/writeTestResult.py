# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/30 19:32
# @File    : writeTestResult.py
# @Software: PyCharm

from common.getExcelData import OpenpyXl
from common.mysqlDB import MySqlDB
from common.querySql import QuerySql

mysqldb = MySqlDB()
querysql = QuerySql()

class WriteTestResult(OpenpyXl):
    # 传入字典，获取字典key对应的value值
    def get_dict_value(self, **kwargs):  # 传入字典
        code = kwargs.get("code")  # 获取字典的code字段
        msg = kwargs.get("msg")  # 获取字典的msg字段
        success = kwargs.get("success")  # 获取字典的success字段
        dict = {"code": code, "msg": msg, "success": success}  # 用于存放返回的值
        return dict

    # 查询数据库，获取对应的查询结果
    def get_query_results(self, host, user, password, db, port, key, value):
        """
        :param host: 主机地市
        :param user: 用户名
        :param password: 密码
        :param db: 数据库名
        :param port: 端口号
        :param key: 以某个字段进行查询
        :param value: 该字段的查询条件
        :return:
        """
        mysqldb.connect_db(host, user, password, db, port)  # 连接数据库
        sql = querysql.area_query(key, value)  # 需执行的sql
        resulst = mysqldb.call_sql(sql)  # 执行sql获得查询结果
        mysqldb.close_db()  # 关闭数据库连接
        return str(resulst)  # 返回查询结果为tuple元组，强转为str

    # 把测试结果的实际结果、测试结果写入测试用例中，操作之后的值要入库
    def write_TestResult_inDB(self, res, expData, filename, sheetName, Row, value, results):
        """
        :param res: 实际返回结果
        :param expData: 期望返回结果
        :param filename: 文件名
        :param sheetName: 表单名
        :param Row: 用例所在的行号
        :param value: 断言的字段值
        :param results: sql查询的结果
        :return:
        """
        resdict = self.get_dict_value(**res)  # 实际返回结果
        expDatadict = self.get_dict_value(**expData)  # 预期返回结果

        # 向excel用例中回写实际返回数据和测试结果列
        if type(value) != str:
            value = str(value)  # 强转为str类型
            if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (
                    resdict["success"] == expDatadict["success"])& (value in results):
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
                # print("==========pass==========")
            else:
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
                # print("==========fail==========")
        else:
            if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (
                    resdict["success"] == expDatadict["success"]) & (value in results):
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
                # print("==========pass==========")
            else:
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
                # print("==========fail==========")

    # 把测试结果的实际结果、测试结果写入测试用例中，操作之后的值不入库
    def write_TestResult_noDB(self, res, expData, filename, sheetName, Row, value, results):
        """
        :param res: 实际返回结果
        :param expData: 期望返回结果
        :param filename: 文件名
        :param sheetName: 表单名
        :param Row: 用例所在的行号
        :param value: 断言的字段值
        :param results: sql查询的结果
        :return:
        """
        resdict = self.get_dict_value(**res)  # 实际返回结果
        expDatadict = self.get_dict_value(**expData)  # 预期返回结果

        # 向excel用例中回写实际返回数据和测试结果列
        if type(value) != str:
            value = str(value)  # 强转为str类型
            if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (
                    resdict["success"] == expDatadict["success"]) & (value not in results):
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
                # print("==========pass==========")
            else:
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
                # print("==========fail==========")
        else:
            if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (
                    resdict["success"] == expDatadict["success"]) & (value not in results):
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
                # print("==========pass==========")
            else:
                res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
                # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
                self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
                # print("==========fail==========")

    # 把测试结果的实际结果、测试结果写入测试用例中，专门针对删除接口的，比较删除前后的数据条数保持不变
    def write_TestResult_delDB(self, res, expData, filename, sheetName, Row, value, results):
        """
        :param res: 实际返回结果
        :param expData: 期望返回结果
        :param filename: 文件名
        :param sheetName: 表单名
        :param Row: 用例所在的行号
        :param value: 断言的字段值
        :param results: sql查询的结果
        :return:
        """
        resdict = self.get_dict_value(**res)  # 实际返回结果
        expDatadict = self.get_dict_value(**expData)  # 预期返回结果

        # 向excel用例中回写实际返回数据和测试结果列
        if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (
                resdict["success"] == expDatadict["success"]) & (value == results):
            res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
            # print("==========pass==========")
        else:
            res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
            # print("==========fail==========")

    # 把测试结果的实际结果、测试结果写入测试用例中，专门针对为空/不传校验的，此场景不断言数据库
    def write_TestResult_null(self, res, expData, filename, sheetName, Row):
        """
        :param res: 实际返回结果
        :param expData: 期望返回结果
        :param filename: 文件名
        :param sheetName: 表单名
        :param Row: 用例所在的行号
        :return:
        """
        resdict = self.get_dict_value(**res)  # 实际返回结果
        expDatadict = self.get_dict_value(**expData)  # 预期返回结果

        # 向excel用例中回写实际返回数据和测试结果列
        if (resdict["code"] == expDatadict["code"]) & (resdict["msg"] == expDatadict["msg"]) & (resdict["success"] == expDatadict["success"]):
            res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="pass")  # 调用写数据方法，写入测试结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="通过")  # 调用写数据方法，写入测试结果
            # print("==========pass==========")
        else:
            res = self.json_dumps(res)  # 调用json_dumps方法，表示把res转换为字符串
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=10, writeData=res)  # 调用写数据方法，写入实际结果
            # self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=11, writeData="fail")  # 调用写数据方法，写入测试结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=14, writeData=res)  # 调用写数据方法，写入实际结果
            self.write_excel_data(filename, sheetName, writeRow=Row, writeCol=15, writeData="失败")  # 调用写数据方法，写入测试结果
            # print("==========fail==========")

