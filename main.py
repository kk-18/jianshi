import unittest
import os
import sys
from BeautifulReport import BeautifulReport
from common.Email import SendEmail


# 当前脚本所在文件真实路径
#  os.path.dirname(path) 获取当前文件绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))

#os.path.join()在路径后追加
start_dir=os.path.join(cur_path,'case')
print(start_dir)

discover=unittest.defaultTestLoader.discover(start_dir,#要测试的模块名或者测试用例目录名称
                                            pattern="test_*.py",#标识用例文件名的匹配原则
                                             top_level_dir=None)#测试模块的顶层目录，若没有则为None
report_path=os.path.join(cur_path,'report\\result.html')
fp = open(report_path, "wb")
# 执行测试用例并输出html报告
runners = BeautifulReport(discover)
runners.report(filename='result', description='web端部分接口', log_path='F:\\python\\jianshi\\report\\')
fp.close()

#发送邮件
SendEmail().Sendemail()
