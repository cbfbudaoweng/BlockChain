# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/7/14 20:22
# @File    : OpenAPI.py
# @Software: PyCharm

from common.baseapi import BaseApi
from config.blockchain_url import BlockChainUrl


class OpenAPI(BaseApi):
    # 数据上链
    def data_save(self, inData):
        url = BlockChainUrl.data_save_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8"}  # 2-请求头
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 3-发送请求体
        return r.json()  # 返回字典

    # 数据查询
    def data_query(self, inData):
        url = BlockChainUrl.data_query_url.value
        header = {"Content-Type": "application/json", "charset": "UTF-8"}
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 数据核验
    def data_check(self, inData):
        url = BlockChainUrl.data_check_url.value
        header = {"Content-Type": "application/json", "charset": "UTF-8"}
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)
        return r.json()