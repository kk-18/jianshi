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
        #读取excel中的case.data为str，应该使用双引号，单引号会报错
        datas=json.loads(case.data)
        print("用例id:{0},用例名称{1}".format(case.id,case.title))
        header={'Authorization':'0143d81d09ad4ce6aaea7beda1be28b8'}
        res=Requests(method=case.method,url=case.url,headers=header,params=datas)
        print(res.get_url())
        print("状态码:{0}，响应结果:{1}".format(res.get_status_code(),res.get_json()))
        #断言
        self.assertEqual(res.get_status_code(),200,"失败")
    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()