import requests
import unittest

class test_main(unittest.TestCase):

    def setUp(self):
        print("----------测试开始-----------")
    def test_aaa(self):
        res=requests.get('https://www.weseepro.com/api/v1/message/discovery/v1')
        print("响应结果:{0}，状态码:{1}".format(res.json(),res.status_code))


    def tearDown(self):
        print("----------测试清除-------------")

if __name__ == '__main__':
    unittest.main()