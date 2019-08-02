import unittest
import openpyxl
import os
import ddt
import json
from common.forreq import Requests
from common.forexcel import *


class test_main(unittest.TestCase):

    def setUp(self):
        print("----------测试开始-----------")
    def test_aaa(self):
        #获取文件路径
        excel_path=os.path.join(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0],
                                           r'data\test_case_web.xlsx')
        tt=DoExcel(excel_path).read_cases('web')
        #数据转换， json.loads()用于将str类型的数据转成dict
        print(tt[1])

        '''
        res=Requests(method=tt['method'],url=tt['url'])
        print("状态码:{0}，响应结果:{1}".format(res.get_status_code(),res.get_json()))
        '''
    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()