#coding:utf8

from ranzhiWeekend.ranzhi_base_page import RanzhiBasePage


class RanzhiSubLoginPage(RanzhiBasePage):
    def __init__(self, driver, baseUrl):
        """

        :param driver:
        :param baseUrl:
        """
        # 调用其 基类 RanzhiBasePage的 构造函数
        # 实现 基类 的构造函数的功能
        super(RanzhiSubLoginPage, self).__init__(driver, baseUrl)
        self.loginPageUrl = "/Login/Login/index"
        self.mainPageUrl = "/Manage/BenchWork/index"
        self.driver.clearCookies()

    def login(self, userName, password):
        self.openPage(self.loginPageUrl)
        # self.driver.clearCookies()
        self.driver.implicitlyWait(5)
        self.driver.type("id,username", userName)
        self.driver.type("id,userpwd", password)
        self.driver.click("c,login-btn")

    def getMainPage(self):
        return self.baseUrl + self.mainPageUrl