# !/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/6/12 19:32
# @File    : mysqlDB.py
# @Software: PyCharm

import pymysql

from common.querySql import QuerySql

querysql = QuerySql()


class MySqlDB:

    # 打开数据库连接
    def connect_db(self, host: str, user: str, password: str, db: str, port: int, charset: str = "utf8"):
        """
        :param host: 数据库连接地址
        :param user: 用户名
        :param password: 密码
        :param db: 数据库名
        :param port: 端口
        :param charset: 默认 utf-8
        :return:
        """
        self.connect = pymysql.Connect(host=host, user=user, password=password, db=db, port=port, charset=charset)  # 连接数据库
        self.cursor = self.connect.cursor()  # 得到一个可以指定SQL语句的光标对象，即获取游标

    # 执行查询语句
    def call_sql(self, query_sql):
        """
        执行查询语句
        :param query_sql: 查询语句
        :return:
        """
        try:
            # 执行SQL语句
            self.cursor.execute(query_sql)
            results = self.cursor.fetchall()  # 获取查询的所有记录
            return results
        except Exception as e:
            raise e

    # 关闭数据库连接
    def close_db(self):
        if self.connect is None:
            self.connect.close()

    # 查询数据库，获取地市的查询结果，以某个字段进行查询
    def get_area_results(self, key, value):
        """
        :param key:以某个字段进行查询
        :param value: 该字段的查询条件
        :return:
        """
        sql = querysql.area_query(key, value)  # 需执行的sql
        result = self.call_sql(sql)  # 执行sql获得查询结果
        return str(result)  # 返回查询结果为tuple元组，强转为str

    # 查询数据库，获取地市的查询结果，查询所有地市
    def get_area_resultsAll(self):
        sql = querysql.area_query_all()  # 需执行的sql
        result = self.call_sql(sql)  # 执行sql获得查询结果
        return result  # 返回查询结果为tuple元组，强转为int

    # 查询数据库，模糊查询
    def get_area_resultLike(self, key, value):
        sql = querysql.area_query_like(key, value)# 需执行的sql
        result = self.call_sql(sql)  # 执行sql获得查询结果
        return str(result)  # 返回查询结果为tuple元组，强转为str

    # 查询机构,以某个字段进行查询
    def get_org_results(self, key, value):
        sql =querysql.org_query(key, value)
        result = self.call_sql(sql)
        return str(result)

    # 查询机构，查询所有机构
    def get_org_resultsAll(self):
        sql = querysql.org_query_all()
        result = self.call_sql(sql)
        return result





