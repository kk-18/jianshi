import unittest
import openpyxl
import os
from common.forreq  import Requests

class test_main(unittest.TestCase):

    def setUp(self):
        print("----------测试开始-----------")
    def test_aaa(self):
        class_dir = os.path.split(os.path.realpath(__file__))[0]#获取当前.py文件路径
        excel_dir = os.path.join(class_dir + r'\test_case_web.xlsx')#excel路径

        # 第一步 定位excel
        wb = openpyxl.load_workbook(excel_dir)  # 需要传入excel路径

        # 第二步 根据打开的excel 定位excel中的表单sheet
        sheet = wb['web']  # 需要传入表单名字

        # 第三步  定位单元格实现读取
        case = sheet.cell(row=1, column=1).value  # row表示行  column表示列,这里就是读取第一行第一列
        print(case)

        res=Requests(method='get',url='https://www.weseepro.com/api/v1/message/discovery/v1')
        print("状态码:{0}，响应结果:{1}".format(res.get_status_code(),res.get_json()))

    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()