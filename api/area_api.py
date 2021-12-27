# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/20 14:22
# @File    : area_api.py
# @Software: PyCharm

from common.baseapi import BaseApi
from config.blockchain_url import BlockChainUrl


class AreaApi(BaseApi):
    # 地市管理-新增地市-鉴权
    def create_area(self, inToken, inData):
        url = BlockChainUrl.create_area_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8", "X-Access-Token": inToken}  # 2-请求头
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 3-发送请求体
        return r.json()  # 返回字典

    # 地市管理-新增地市-非鉴权
    def create_area_notoken(self, inData):
        url = BlockChainUrl.create_area_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8"}  # 2-请求头
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 3-发送请求体
        return r.json()  # 返回字典

    # 地市管理-更新地市-鉴权
    def update_area(self, inToken, inData):
        url = BlockChainUrl.update_area_url.value
        header = {"Content-Type": "application/json", "charset": "UTF-8", "X-Access-Token": inToken}
        req = {
            "url": url,
            "method": "put",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 地市管理-更新地市-非鉴权
    def update_area_notoken(self, inData):
        url = BlockChainUrl.update_area_url.value
        header = {"Content-Type": "application/json", "charset": "UTF-8"}
        req = {
            "url": url,
            "method": "put",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 地市管理-删除地市-鉴权
    def delete_area(self, inToken, inData):
        url = BlockChainUrl.delete_area_url.value
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "UTF-8", "X-Access-Token": inToken}
        req = {
            "url": url,
            "method": "delete",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 地市管理-删除地市-非鉴权
    def delete_area_notoken(self, inData):
        url = BlockChainUrl.delete_area_url.value
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "UTF-8"}
        req = {
            "url": url,
            "method": "delete",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 地市管理-地市列表查询-鉴权
    def area_list(self, inToken, inData):
        url = BlockChainUrl.list_area_url.value
        header = {"charset": "UTF-8", "X-Access-Token": inToken}
        req = {
            "url": url,
            "method": "get",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 地市管理-地市列表查询-非鉴权
    def area_list_notoken(self, inData):
        url = BlockChainUrl.list_area_url.value
        header = {"charset": "UTF-8"}
        req = {
            "url": url,
            "method": "get",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()