# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/7/12 19:32
# @File    : make_data.py
# @Software: PyCharm

from common.getNowTime import getNowTime
from common.mysqlDB import MySqlDB

host = '192.168.5.87'
user = 'root'
password = 'root'
db = 'taas'
port = 3307

gettime = getNowTime()

class MakeData(MySqlDB):
    # 以传参的方式，向地市表中插入数据
    def make_test_data(self, name, created_by, created_at, updated_by, updated_at):
        # 连接打开数据库
        self.connect_db(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        # 需要执行的sql
        sql = "INSERT INTO `taas`.`bc_area` (`name`, `revision`, `created_by`, `created_at`, `updated_by`, `updated_at`) VALUES (%s, 0, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (name, created_by, created_at, updated_by, updated_at))  # 执行sql语句
            self.connect.commit()  # 提交到数据库执行
        except:
            self.connect.rollback()  # 发生错误时回滚
        self.connect.close()  # 关闭数据库连接


if __name__ == '__main__':
    make_area = MakeData()  # 创建实例化对象
    # 循环10次，插入10条数据
    for i in range(93, 95):
        data = {
            "name": f"测试地市{i}",
            "created_by": "06016557342f55616e8a0f20d3a5358b",
            "created_at": gettime.get_now_time(),  # 获取当前时间
            "updated_by": "",
            "updated_at": gettime.get_now_time()  # 获取当前时间
        }
        make_area.make_test_data(**data)  # 使用变量向SQL语句中传递参数
