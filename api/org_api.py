# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/29 10:28
# @File    : org_api.py
# @Software: PyCharm

from common.baseapi import BaseApi
from config.blockchain_url import BlockChainUrl


class OrgApi(BaseApi):
    # 机构管理-新增机构-鉴权
    def create_org(self, inToken, inData):
        url = BlockChainUrl.create_org_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8", "X-Access-Token": inToken}  # 2-请求头
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 3-发送请求体
        return r.json()  # 返回字典

    # 机构管理-新增机构-非鉴权
    def create_org_token(self, inData):
        url = BlockChainUrl.create_org_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8"}  # 2-请求头
        req = {
            "url": url,
            "method": "post",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 3-发送请求体
        return r.json()  # 返回字典

    # 机构管理-更新机构-鉴权
    def update_org(self, inToken, inData):
        url = BlockChainUrl.update_org_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8", "X-Access-Token": inToken}  # 请求头
        req = {
            "url": url,
            "method": "put",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 发送请求体
        return r.json()  # 返回字典

    # 机构管理-更新机构-非鉴权
    def update_org_token(self, inData):
        url = BlockChainUrl.update_org_url.value  # 1-url
        header = {"Content-Type": "application/json", "charset": "UTF-8"}  # 请求头
        req = {
            "url": url,
            "method": "put",
            "headers": header,
            "json": inData
        }
        r = self.send_requests(req)  # 发送请求体
        return r.json()  # 返回字典

    # 机构管理-删除机构-鉴权
    def delete_org(self, inToken, inData):
        url = BlockChainUrl.delete_org_url.value  # url
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "UTF-8", "X-Access-Token": inToken}  # 请求头
        req = {
            "url": url,
            "method": "delete",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)  # 发送请求体
        return r.json()  # 返回字典

    # 机构管理-删除机构-非鉴权
    def delete_org_token(self, inData):
        url = BlockChainUrl.delete_org_url.value  # url
        header = {"Content-Type": "application/x-www-form-urlencoded", "charset": "UTF-8"}  # 请求头
        req = {
            "url": url,
            "method": "delete",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)  # 发送请求体
        return r.json()  # 返回字典

    # 机构管理-机构列表查询-鉴权
    def org_list(self, inToken, inData):
        url = BlockChainUrl.list_org_url.value
        header = {"charset": "UTF-8", "X-Access-Token": inToken}
        req = {
            "url": url,
            "method": "get",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()

    # 机构管理-机构列表查询-非鉴权
    def org_list_notoken(self, inData):
        url = BlockChainUrl.list_org_url.value
        header = {"charset": "UTF-8"}
        req = {
            "url": url,
            "method": "get",
            "headers": header,
            "data": inData
        }
        r = self.send_requests(req)
        return r.json()