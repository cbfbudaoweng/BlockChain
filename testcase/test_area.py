# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/30 19:32
# @File    : test_area.py
# @Software: PyCharm
import os
import allure
import pytest
from api.area_api import AreaApi
from api.blockchain_wework import BlockChainApi
from common.getExcelData import OpenpyXl
from common.getExcelIndex import GetExcelIndex
from common.mysqlDB import MySqlDB
from common.writeTestResult import WriteTestResult

excel = OpenpyXl()
valueRow = GetExcelIndex()
writeTestResult = WriteTestResult()
mysqldb = MySqlDB()

filename = "../data/区块链平台-1.1-接口自动化.xlsx"
sheetName = "接口测试用例"
host = '192.168.5.87'
user = 'root'
password = 'root'
db = 'taas'
port = 3307


class TestArea():
    def setup_class(self):
        self.blockchain = BlockChainApi()
        self.token = self.blockchain.get_token()  # 获取token
        self.area = AreaApi()

    def teardown_class(self):
        pass

    def setup_method(self):
        # 对数据库的操作，每个方法执行完之后，需要关闭数据库重新连接,否则部分用例会查询不到数据
        mysqldb.connect_db(host, user, password, db, port)  # 连接数据库

    def teardown_methon(self):
        mysqldb.close_db()  # 关闭数据库

    @allure.feature('地市管理-新增地市-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=19, startRow=19))
    def test_create_area_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.create_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-新增地市-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=20, startRow=20))
    def test_create_area_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.create_area_notoken(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-新增地市-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=22, startRow=21))
    def test_create_area_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.create_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-新增地市-异常流-判重和空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=25, startRow=23))
    def test_create_area_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.create_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('地市管理-更新地市-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=26, startRow=26))
    def test_update_area_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.update_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-更新地市-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=27, startRow=27))
    def test_update_area_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.update_area_notoken(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-更新地市-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=31, startRow=28))
    def test_update_area_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.update_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-更新地市-异常流-判重和空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=36, startRow=32))
    def test_update_area_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.update_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('地市管理-删除地市-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=37, startRow=37))
    def test_delete_area_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.area.delete_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_results("id", inData['id'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['id']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(str(inData['id']) not in results)  # 断言删除的记录已成功从数据库中删除
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['id'], results)

    @allure.feature('地市管理-删除地市-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=38, startRow=38))
    def test_delete_area_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_area_resultsAll()  # 执行删除操作前，查询数据库，获取地市的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.area.delete_area_notoken(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_area_resultsAll()  # 执行删除操作后，查询数据库，获取地市的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)  # 断言执行删除操作前后数据库中的数据一直，即删除异常流不会操作数据库
        # 写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    @allure.feature('地市管理-删除地市-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=41, startRow=39))
    def test_delete_area_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_area_resultsAll()  # 执行删除操作前，查询数据库，获取地市的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.area.delete_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_area_resultsAll()  # 执行删除操作后，查询数据库，获取地市的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)  # 断言执行删除操作前后数据库中的数据一直，即删除异常流不会操作数据库
        # 写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    @allure.feature('地市管理-删除地市-异常流-空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=43, startRow=42))
    def test_delete_area_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.area.delete_area(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('地市管理-地市列表查询-查询所有列表')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=44, startRow=44))
    def test_list_area_all(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_area_resultsAll()  # 执行查询操作前，查询数据库，获取地市的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.area.area_list(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_area_resultsAll()  # 执行查询操作后，查询数据库，获取地市的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    @allure.feature('地市管理-地市列表查询-以名字模糊查询')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=45, startRow=45))
    def test_list_area_part(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.area.area_list(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_resultLike("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] in results)  # 断言输入的值成功存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('地市管理-地市列表查询-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=46, startRow=46))
    def test_list_area_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.area.area_list_notoken(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('地市管理-地市列表查询-查询结果为空')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=47, startRow=47))
    def test_list_area_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.area.area_list(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_area_resultLike("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)


if __name__ == '__main__':
    # pytest.main(["test_blockchain.py"])
    # 在main中执行生成测试报告，需要用python执行器执行；命令行执行不需要
    # 在测试执行期间搜集结果，把搜集的测试数据存放到../report/data目录,"--clean-alluredir"删除之前生成的结果，否则会把之前生成的结果一并生成报告
    pytest.main(["test_area.py", "-s", "-q", "--alluredir", "../report/data", "--clean-alluredir"])
    # 生成测试报告--取出../report/data目录搜集的测试数据，把其生成测试报告，并把报告存放到../report/report目录
    os.system("allure generate ../report/data -o ../report/report --clean")
    # 打开测试报告
    os.system("allure open -h 127.0.0.1 -p 8883 ../report/report")
