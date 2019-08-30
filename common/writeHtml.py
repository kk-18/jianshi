from HTMLTestRunner import HTMLTestRunner
import unittest
from case import test_main

class WriteHtml():

    report_path="F:\\python\\jianshi\\report\\result.html"
    fp=open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,#报告写入文件的存储区域
                title='<Demo Test>',#报告主题
                description='This demonstrates the report output by HTMLTestRunner.'#报告描述
                )
    runner.run()
    fp.close()