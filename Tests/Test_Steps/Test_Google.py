import random
import os, sys

import unittest
import HTMLTestRunner

import exceptions

import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


fp = file('my_report_google.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )


class Test_google(unittest.TestCase):
    """ Test Description and Steps Optional. """

    def setUp(self):
        self.__name__ = "Test_google"

    def test_Demo(self):
        """ Open URL and Search in Search Box """

        # print "Here"
        self.driver = wd.Firefox()
        self.driver.get("http://www.google.com/")
        self.element = WebDriverWait(self.driver, 15).until( EC.title_contains("abcd") )


# if __name__ == "__main__":
#     HTMLTestRunner.main()

runner.run(Test_google)
