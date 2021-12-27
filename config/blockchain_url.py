# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/30 19:32
# @File    : blockchain_url.py
# @Software: PyCharm
from enum import Enum

# blockchain_host = "http://192.168.5.87:5100"  # 区块链管理平台url-开发环境
blockchain_host = "http://192.168.5.87:5200"  # 区块链管理平台url-测试环境



class BlockChainUrl(Enum):  # 设置枚举
    get_token_url = blockchain_host + "/test/getToken"  # 获取Token

    create_area_url = f"{blockchain_host}/area/add"  # 地市管理-新增地市
    update_area_url = f"{blockchain_host}/area/update"  # 地市管理-更新地市
    delete_area_url = f"{blockchain_host}/area/delete"  # 地市管理-删除地市
    list_area_url = f"{blockchain_host}/area/list"  # 地市管理-地市列表查询

    create_org_url = f"{blockchain_host}/orgnization/add"  # 机构管理-新增机构
    update_org_url = f"{blockchain_host}/orgnization/update"  # 机构管理-更新机构
    delete_org_url = f"{blockchain_host}/orgnization/delete"  # 机构管理-删除机构
    list_org_url = f"{blockchain_host}/orgnization/list"  # 机构管理-机构列表查询

    data_save_url = f"{blockchain_host}/rest/data/save"  # 数据上链
    data_query_url = f"{blockchain_host}/rest/data/query"  # 数据查询
    data_check_url = f"{blockchain_host}/rest/data/check"  # 数据核验

