#coding:utf8

import unittest
from time import sleep

from ranzhiWeekend.automate_driver import AutomateDriver
from ranzhiWeekend.ranzhi_sub_login_page import RanzhiSubLoginPage

"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""


class RanzhiTests(unittest.TestCase):
    def setUp(self):
        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = AutomateDriver()
        self.baseUrl = "http://120.25.234.145/cloud/index.php"

    def tearDown(self):
        """
        结束每个测试后的清理工作
        :return:
        """
        self.autoDriver.quitBrowser()

    def test_ranzhi_login(self):
        """
        测试用例：测试然之登录
        :return:
        """
        # 新建然之的页面对象
        loginPage = RanzhiSubLoginPage(self.autoDriver, self.baseUrl)

        # 利用然之的页面对象进行登录
        loginPage.login("463811@qq.com", "123456")
        sleep(2)
        # 断言 是否登录成功

        self.assertEqual(loginPage.getMainPage(), self.autoDriver.getUrl(), u"登录失败")