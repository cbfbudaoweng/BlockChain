# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/7/2 10:18
# @File    : test_org.py
# @Software: PyCharm
import allure
import pytest

from api.blockchain_wework import BlockChainApi
from api.org_api import OrgApi
from common.getExcelData import OpenpyXl
from common.getExcelIndex import GetExcelIndex
from common.mysqlDB import MySqlDB
from common.writeTestResult import WriteTestResult

mysqldb = MySqlDB()
valueRow = GetExcelIndex()
excel = OpenpyXl()
writeTestResult = WriteTestResult()

filename = "../data/区块链平台-1.1-接口自动化.xlsx"
sheetName = "接口测试用例"
host = '192.168.5.87'
user = 'root'
password = 'root'
db = 'taas'
port = 3307

class TestOrganization():
    def setup_class(self):
        self.blockchain = BlockChainApi()
        self.token = self.blockchain.get_token()  # 获取token
        self.org = OrgApi()

    def teardown_class(self):
        pass

    def setup_method(self):
        # 对数据库的操作，每个方法执行完之后，需要关闭数据库重新连接,否则部分用例会查询不到数据
        mysqldb.connect_db(host, user, password, db, port)  # 连接数据库

    def teardown_methon(self):
        mysqldb.close_db()  # 关闭数据库

    @allure.feature('机构管理-新增机构-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=52, startRow=48))
    def test_create_org_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.org.create_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] in results)  # 断言输入的值成功存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-新增机构-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData',excel.read_excel_data(filename, sheetName, endRow=53, startRow=53))
    def test_create_org_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.org.create_org_token(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-新增机构-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=63, startRow=54))
    def test_create_org_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
        print(f"请求体{inData}")
        res = self.org.create_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 查询数据库，获取地市的查询结果
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-新增机构-异常流-判重和空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=72, startRow=64))
    def test_create_org_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号获取该行用例所在的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.create_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")
        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)


    @allure.feature('机构管理-更新机构-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=73, startRow=73))
    def test_update_org_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号，获取该行用例的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.update_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 以机构名称查询机构
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        pytest.assume(inData['name'] in results)  # 断言更正的值存入数据库中
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-更新机构-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData',excel.read_excel_data(filename, sheetName, endRow=74, startRow=74))
    def test_update_org_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号，获取该行用例的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.update_org_token(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 以机构名称查询机构
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        pytest.assume(inData['name'] not in results)  # 断言更新异常流的数据不入库
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-更新机构-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=86, startRow=75))
    def test_update_org_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号，获取该行用例的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.update_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results("name", inData['name'])  # 以机构名称查询机构
        print(f"查询的值：{inData['name']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        pytest.assume(inData['name'] not in results)  # 断言更新异常流的数据不入库
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-更新机构-异常流-判重和空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=95, startRow=87))
    def test_update_org_null(self, caseNum, inData, expData):
        # 空了补充
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号，获取该行用例的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.update_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")
        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('机构管理-删除机构-正常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=96, startRow=96))
    def test_delete_org_right(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 根据用例编号，获取该行用例的行号
        inData = self.org.json_loads(inData)  # 转为字典
        expData = self.org.json_loads(expData)  # 转为字典
        print(f"请求体{inData}")
        res = self.org.delete_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        results = mysqldb.get_org_results('id', inData['id'])  # 以id查询机构
        print(f"查询的值：{inData['id']}")
        print(f"sql查询结果：{results}")

        # 断言
        pytest.assume(res['code'] == expData['code'])  # int
        pytest.assume(res['msg'] == expData['msg'])  # str
        pytest.assume(res['success'] == expData['success'])  # bool
        pytest.assume(str(inData['id']) not in results)  # 断言删除的记录已成功从数据库中删除
        # 写入测试结果
        writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['id'], results)

    @allure.feature('机构管理-删除机构-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=97, startRow=97))
    def test_delete_org_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_org_resultsAll()  # 执行删除操作前，查询数据库，获取机构的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.org.delete_org_token(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_org_resultsAll()  # 执行删除操作后，查询数据库，获取机构的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)  # 断言执行删除操作前后数据库中的数据一直，即删除异常流不会操作数据库
        # 写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    @allure.feature('机构管理-删除机构-异常流')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=101, startRow=98))
    def test_delete_org_error(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_org_resultsAll()  # 执行删除操作前，查询数据库，获取机构的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.org.delete_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_org_resultsAll()  # 执行删除操作后，查询数据库，获取机构的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)  # 断言执行删除操作前后数据库中的数据一直，即删除异常流不会操作数据库
        # 写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    @allure.feature('机构管理-删除机构-异常流-空校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=103, startRow=102))
    def test_delete_area_null(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.org.delete_org(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    @allure.feature('机构管理-机构列表查询-查询所有列表')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=104, startRow=104))
    def test_list_area_all(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        pre_results = mysqldb.get_org_resultsAll()  # 执行查询操作前，查询数据库，获取地市的查询结果
        print(f"删除请求前sql查询结果：{pre_results}")

        print(f"请求体{inData}")
        res = self.org.org_list(self.token, inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        end_results = mysqldb.get_org_resultsAll()  # 执行查询操作后，查询数据库，获取地市的查询结果
        print(f"删除请求后sql查询结果：{end_results}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        pytest.assume(pre_results == end_results)
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_delDB(res, expData, filename, sheetName, Row, pre_results, end_results)

    # @allure.feature('地市管理-地市列表查询-以名字模糊查询')
    # @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=45, startRow=45))
    # def test_list_area_part(self, caseNum, inData, expData):
    #     Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
    #     inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
    #     expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
    #
    #     print(f"请求体{inData}")
    #     res = self.area.area_list(self.token, inData)  # 发送请求
    #     print(f"实际输出{res}")
    #     print(f"预期输出{expData}")
    #
    #     results = mysqldb.get_area_resultLike("name", inData['name'])  # 查询数据库，获取地市的查询结果
    #     print(f"查询的值：{inData['name']}")
    #     print(f"sql查询结果：{results}")
    #
    #     # 断言
    #     pytest.assume(res["code"] == expData["code"])  # int
    #     pytest.assume(res["msg"] == expData["msg"])  # str
    #     pytest.assume(res["success"] == expData["success"])  # bool
    #     pytest.assume(inData['name'] in results)  # 断言输入的值成功存入数据库中
    #     # 调用write_testResult方法，写入测试结果
    #     writeTestResult.write_TestResult_inDB(res, expData, filename, sheetName, Row, inData['name'], results)

    @allure.feature('机构管理-机构列表查询-鉴权校验')
    @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=110, startRow=110))
    def test_list_org_token(self, caseNum, inData, expData):
        Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
        inData = self.org.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
        expData = self.org.json_loads(expData)  # 调用json_loads方法，把expData转化为字典

        print(f"请求体{inData}")
        res = self.org.org_list_notoken(inData)  # 发送请求
        print(f"实际输出{res}")
        print(f"预期输出{expData}")

        # 断言
        pytest.assume(res["code"] == expData["code"])  # int
        pytest.assume(res["msg"] == expData["msg"])  # str
        pytest.assume(res["success"] == expData["success"])  # bool
        # 调用write_testResult方法，写入测试结果
        writeTestResult.write_TestResult_null(res, expData, filename, sheetName, Row)

    # @allure.feature('地市管理-地市列表查询-查询结果为空')
    # @pytest.mark.parametrize('caseNum,inData,expData', excel.read_excel_data(filename, sheetName, endRow=47, startRow=47))
    # def test_list_area_null(self, caseNum, inData, expData):
    #     Row = valueRow.find_row(filename, sheetName, caseNum)  # 获取参数传入的每组值中，用例编号所在的行号
    #     inData = self.area.json_loads(inData)  # 调用json_loads方法，把inData转化为字典
    #     expData = self.area.json_loads(expData)  # 调用json_loads方法，把expData转化为字典
    #
    #     print(f"请求体{inData}")
    #     res = self.area.area_list(self.token, inData)  # 发送请求
    #     print(f"实际输出{res}")
    #     print(f"预期输出{expData}")
    #
    #     results = mysqldb.get_area_resultLike("name", inData['name'])  # 查询数据库，获取地市的查询结果
    #     print(f"查询的值：{inData['name']}")
    #     print(f"sql查询结果：{results}")
    #
    #     # 断言
    #     pytest.assume(res["code"] == expData["code"])  # int
    #     pytest.assume(res["msg"] == expData["msg"])  # str
    #     pytest.assume(res["success"] == expData["success"])  # bool
    #     pytest.assume(inData['name'] not in results)  # 断言输入的值成功存入数据库中
    #     # 调用write_testResult方法，写入测试结果
    #     writeTestResult.write_TestResult_noDB(res, expData, filename, sheetName, Row, inData['name'], results)
