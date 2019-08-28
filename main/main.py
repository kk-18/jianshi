import unittest
import openpyxl
import os
from ddt import ddt,data
import json
from common.forreq import Requests
from common.forexcel import *

@ddt
class test_main(unittest.TestCase):
    # 获取文件路径
    excel_path = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0],
                              r'data\test_case_web.xlsx')
    tt = DoExcel(excel_path).read_cases('web')

    def setUp(self):
        print("----------测试开始-----------")

    @data(*tt)#装饰测试方法，拿到几个数据数据就执行几条用例
    def test_aaa(self,case):

        #数据转换， json.loads()用于将str类型的数据转成dict
        # data=json.loads(case.data)
        res=Requests(method=case.method,url=case.url)
        print("状态码:{0}，响应结果:{1}".format(res.get_status_code(),res.get_json()))
    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()