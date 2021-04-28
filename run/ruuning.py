#encoding:utf-8
import unittest
import os,sys,ddt
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import warnings
from common.login import Login
from util.data.writeexcel import runn
from config.allpath import *
from config.log.mylog import log
from case.community import m
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from BeautifulReport import BeautifulReport
warnings.filterwarnings("ignore")
result_path=data_debug


@ddt.ddt
class Testcase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('******************** 测试开始 ********************')
        Login.login()
    @classmethod
    def tearDownClass(cls):
        log.info('********************  测试结束  ********************')
    e=runn(result_path,['sheet'])
    #获取excel表里的url,datas,headers
    @ddt.data(*e)
    @ddt.unpack
    def testcase01(self,method,url,datas,headers):
        '''帖子维护'''
        result = m.man(method,url,datas,headers)
        self.assertIn(result,'success',"测试失败")
        log.info(result)

    def testcase02(self):
        pass




if __name__=='__main__':
    unittest.main()
    suite=unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # Name = ['帖子管理']
    # now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    # report_title = '游戏社区接口测试报告' + now + '.html'
    # testcases = unittest.TestLoader().loadTestsFromTestCase(Testcase_station)
    # suite.addTest(testcases)
    #
    # BeautifulReport(testcases).report(filename=report_title, description=Name,report_dir=result_path,theme="theme_candy")

