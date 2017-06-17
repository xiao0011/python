#coding:utf8

import smtplib
import unittest
import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from ranzhiWeekend.ranzhi_tests import RanzhiTests


class RanzhiTestRunner():

    def runTest(self):
        """
        运行测试用例
        :return:
        """

        # 声明一个测试套件
        suite = unittest.TestSuite()
        # 添加测试用例到测试套件
        suite.addTest(RanzhiTests("test_ranzhi_login"))

        # 创建一个新的测试结果文件
        buf = open("./result.html", "wb")

        # 声明测试运行的对象
        runner = HTMLTestRunner.HTMLTestRunner(stream=buf,
                                               title="Ranzhi Test Result",
                                               description="Test Case Run Result")
        # 运行测试，并且将结果生成为HTML
        runner.run(suite)

        # 关闭文件输出
        buf.close()

    def sendEmail(self, targetEmail):
        """
        发送邮件
        :param targetEmail:
        :return:
        """

        # 打开测试报告结果
        f = open("./result.html", "rb")

        # 将测试结果放到邮件的主体中
        mailBody = f.read()
        # 关闭测试结果的文件
        f.close()

        # 声明一个邮件对象，用刚刚得到的邮件主体
        msg = MIMEText(mailBody, "html", "utf-8")
        # 设置邮件的主题
        msg["subject"] = Header("Automation Test Result", "utf-8")

        # 创建一个SMTP服务对象
        # simple message transfer protocol
        # 简单的消息转移协议
        smtpMail = smtplib.SMTP()

        # 连接SMTP的服务器
        smtpMail.connect("***.******.com")

        # 登录SMTP的服务器
        smtpMail.login("*******@*****.com", "*********")

        # 使用SMTP的服务器发送邮件
        smtpMail.sendmail("*******@********.com", targetEmail, msg.as_string())

        # 退出SMTP对象
        smtpMail.quit()