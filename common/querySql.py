# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/28 19:32
# @File    : querySql.py
# @Software: PyCharm

class QuerySql():
    # 查询地市，以某个字段进行查询，eg：select * from bc_area where name = '0706area001'
    def area_query(self, key, value):
        areasql = f"select * from bc_area where {key} = '{value}' "
        return areasql

    # 查询所有的地市
    def area_query_all(self):
        areasql = "select count(*) from bc_area"
        return areasql

    # 查询地市，模糊查询，eg：select * from bc_area where name like '%area%'
    def area_query_like(self, key, value):
        areasql = f"select * from bc_area where {key} like '%{value}%' "
        return areasql

    # 查询机构，以某个字段进行查询
    def org_query(self, key, value):
        orgsql = f"select * from bc_orgnization where {key} = '{value}' "
        return orgsql

    # 查询所有机构
    def org_query_all(self):
        orgsql = f"select * from bc_orgnization"
        return orgsql