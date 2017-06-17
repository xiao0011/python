#coding:utf8

class RanzhiBasePage(object):
    def __init__(self, driver, baseUrl):
        """
        构造方法
        :param driver: 封装好的webdriver
        :param baseUrl: 然之系统的基本url http://【localhost:808】/ranzhi/www
        """

        self.baseUrl = baseUrl
        self.driver = driver

    def openPage(self, url):
        """
        打开然之系统的页面，通过拼接URL的方式
        :param url: /sys/index.html
        :return:
        """
        self.driver.navigate(self.baseUrl + url)