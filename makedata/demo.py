# -*- coding: UTF-8 -*-
# @Author  : cbf
# @time    : 2021/11/2 16:12
# @File    : demo.py

class Demo():
    def aa(self):
        list=['1','2','3']
        return list


    def bb(self):
        # sql = "insert into performance_person(name, id_number, phone) value("+self.aa()[0]+","+self.aa()[1]+","+self.aa()[2])
        # sql = "insert into performance_person(name, id_number, phone) value("+self.aa()[0]+",+self.aa()[1]+,+self.aa()[2])"
        # sql = "insert into performance_person(name, id_number, phone) value("+self.aa()[0]+","+self.aa()[1]+","+self.aa()[2]+"),("+self.aa()[0]+","+self.aa()[1]+","+self.aa()[2]+")"
        sql = "insert into performance_person(name, id_number, phone) values"
        for i in range (0,1000):
            a=self.aa()
            sql+="("+a[0]+","+a[1]+","+a[2]+"),"
        # 去掉最后一位逗号，采用切片 a[:-1]，取到最后一位前面一位
        sql=sql[:-1]
        print(sql)
        # print(self.aa())

demo=Demo()
demo.bb()
print(demo.aa()[0])
print(demo.aa()[1])
print(demo.aa()[2])