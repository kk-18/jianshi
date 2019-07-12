import unittest
import openpyxl
import os
import ddt
from common.forreq  import Requests
from common.forexcel import *

@ddt.ddt
class test_main(unittest.TestCase):

    def setUp(self):
        print("----------测试开始-----------")
    def test_aaa(self):
        excel_path = os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0],
                                  r'data\test_case_web.xlsx')
        print(excel_path)
        t = DoExcel(excel_path).read_cases('web')
        res=Requests(method=t['method'],url=t['url'])
        print("状态码:{0}，响应结果:{1}".format(res.get_status_code(),res.get_json()))

    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()