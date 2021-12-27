# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/19 20:22
# @File    : blockchain_wework.py
# @Software: PyCharm

from common.baseapi import BaseApi
from config.blockchain_url import BlockChainUrl


class BlockChainApi(BaseApi):
    # 获取Token
    def get_token(self):
        url = BlockChainUrl.get_token_url.value  # url
        req = {
            "method": "get",
            "url": url
        }  # 请求体
        r = self.send_requests(req)
        return r.json()['data']
