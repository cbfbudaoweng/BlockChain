# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/11/2 16:05
# @File    : create_more_datas.py
import faker
import pymysql

faker_data = faker.Faker(locale='zh_CN')

host = "10.194.188.77"
port = 30562
user = "root"
password = "Bmsoft1234"
database = "test_cbf_kg"

class MakeDatas():
    # 连接数据库
    db_con = pymysql.connect(host=host, port=port, user=user, password=password, db=database, charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cur = db_con.cursor()

    def made_datas(self):
        """制造随机数据，存放到列表中"""
        # 模拟姓名
        # female_name = faker_data.name_female()
        # male_name = faker_data.name_male()
        name = faker_data.name()
        # 模拟身份证号码 18-50岁
        id_number = faker_data.ssn(min_age=18,max_age=50)
        # 模拟手机号码
        phone = faker_data.phone_number()
        # 模拟银行卡
        card_number=faker_data.credit_card_number()
        # 模拟公司名称
        company=faker_data.company()
        # 模拟城市位置
        city=faker_data.city()
        # # 模拟具体街道
        # address=faker_data.address()
        # 模拟IP地址
        ip=faker_data.ipv4_private()
        # 模拟随机url地址
        url=faker_data.url()
        # 模拟邮政编码
        postcode=faker_data.postcode()
        # 把生成的随机数据，依次存放到列表中
        list=[name, id_number, phone, card_number, company, city, ip, url, postcode]
        return list

    def data_update(self):
        # 拼接sql，一次性插入多条数据
        sql = "insert into double_person(name, id_number, phone, card_number, company, city, ip, url, postcode) values"
        # 循环10000次，一次性插入10000条数据
        for i in range (1,10001):
            # 调用生成数据的方法，把得到的值赋值给变量a
            a=self.made_datas()
            sql+="('"+a[0]+"','"+a[1]+"','"+a[2]+"','"+a[3]+"','"+a[4]+"','"+a[5]+"','"+a[6]+"','"+a[7]+"','"+a[8]+"'),"
        # 去掉最后一位逗号，采用切片 a[:-1]，取到最后一位前面一位；到此sql拼接完成
        sql=sql[:-1]
        # print(sql)
        try:
            # 执行sql
            self.cur.execute(sql)
            # 提交数据
            self.db_con.commit()
        except:
            # 检查连接是否断开，如果断开就进行重连
            self.db_con.ping()
            # self.db_con.ping(reconnect=True)
            # 创建游标
            cur=self.db_con.cursor()
            cur.execute(sql)
            self.db_con.commit()


if __name__ == "__main__":
    # 创建实例化对象
    db = MakeDatas()
    # 循环30次，合计插入300次*10000=3000000条数据
    for record in range(1, 601):
        # 调用方法
        db.data_update()
    # 关闭游标
    db.cur.close()
    # 关闭数据库连接
    db.db_con.close()
