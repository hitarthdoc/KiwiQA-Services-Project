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

# fp = file('my_report.html', 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(
#                 stream=fp,
#                 title='My unit test',
#                 description='This demonstrates the report output by HTMLTestRunner.'
#                 )


class Test_Click_on_LOGIN(unittest.TestCase):
    """ Test Description and Steps Optional. """
    # def __init__(self):
        # super(Click_on_LOGIN, self).__init__()
        # self.arg = arg
        # self.Demo_Function()
    #def start():

    def setUp(self):
        self.__name__ = "Test_Click_on_LOGIN"

    def test_Demo(self):
        """ Open URL and Search in Search Box """

        # print "Here"
        self.driver = wd.Firefox()
        self.driver.get("http://unity3d.com/learn/live-training")
        self.element = WebDriverWait(self.driver, 15).until( EC.title_contains("Unity - Learn") )
        # assert "unity" in self.driver.title.lower()

        # self.assertTrue( random.random() > 0.5)

        self.elem = self.driver.find_element_by_xpath("//html/body/div[1]/div/header/div/nav[1]/div/div[4]")
        self.elem.click()
        self.elem = self.driver.find_element_by_xpath("//html/body/div[1]/div/header/div/nav[1]/div/div[5]/div/div/div/form/table[1]/tbody/tr/td[1]/div/table/tbody/tr/td[1]/input")
        self.elem.send_keys("physics")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.element = WebDriverWait(self.driver, 15).until( EC.title_contains("Unity - Search") )
        try:
            assert "fghj" in self.driver.page_source
        except:
            self.driver.save_screenshot(str(self.driver.title) + ".png")
            raise exceptions.AssertionError
        self.driver.close()

        # else:
        #     os.system("pause")
            # return False

# a = Click_on_LOGIN(1)

# ts = unittest.TestCase()
# # a = Click_on_LOGIN()
# ts.addTest(Click_on_LOGIN)

# # a.Demo_Function()
# # print "Login Succesfull! :-)"
# # a = Click_on_LOGIN()

# # print a.__class__
# ts.run()

if __name__ == "__main__":
    HTMLTestRunner.main()
