# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/7/14 20:32
# @File    : test_openApi.py
# @Software: PyCharm

import os
import allure
import pytest
from api.OpenAPI import OpenAPI
from common.getExcelData import OpenpyXl
from common.getExcelIndex import GetExcelIndex
from common.mysqlDB import MySqlDB
from common.writeTestResult import WriteTestResult

excel = OpenpyXl()
valueRow = GetExcelIndex()
writeTestResult = WriteTestResult()
mysqldb = MySqlDB()

filename = "../data/区块链平台-1.1-接口自动化.xlsx"
sheetName = "OpenAPI"
host = '192.168.5.87'
user = 'root'
password = 'root'
db = 'taas'
port = 3307


class TestOpenAPI():
    def setup_class(self):
        self.openapi = OpenAPI()

    def teardown_class(self):
        pass

    def setup_method(self):
        # 对数据库的操作，每个方法执行完之后，需要关闭数据库重新连接,否则部分用例会查询不到数据
        mysqldb.connect_db(host, user, password, db, port)  # 连接数据库

    def teardown_methon(self):
        mysqldb.close_db()  # 关闭数据库

    @allure.feature('数据上链-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=9, startRow=2))
    def test_data_save_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_save(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('数据上链-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=43, startRow=10))
    def test_data_save_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_save(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('数据查询-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=54, startRow=45))
    def test_data_query_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_query(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('数据查询-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=88, startRow=55))
    def test_data_query_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_query(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('数据核验-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=99, startRow=90))
    def test_data_check_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_check(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('数据核验-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=133, startRow=100))
    def test_data_check_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.openapi.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.openapi.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.openapi.data_check(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)


if __name__ == '__main__':
    # pytest.main(["test_blockchain.py"])
    # 在main中执行生成测试报告，需要用python执行器执行；命令行执行不需要
    # 在测试执行期间搜集结果，把搜集的测试数据存放到../report/data目录,"--clean-alluredir"删除之前生成的结果，否则会把之前生成的结果一并生成报告
    pytest.main(["test_openApi.py", "-s", "-q", "--alluredir", "../report/data", "--clean-alluredir"])
    # 生成测试报告--取出../report/data目录搜集的测试数据，把其生成测试报告，并把报告存放到../report/report目录
    os.system("allure generate ../report/data -o ../report/report --clean")
    # 打开测试报告
    os.system("allure open -h 127.0.0.1 -p 8883 ../report/report")
