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

driver = wd.Firefox()
print "Here"
driver.get("file:///C:/Users/hitarthdoctor/Documents/GitHub/KiwiQA-Services-Project/Tests/my_report_Fail.html")
print "Here"

elem = driver.find_element_by_xpath("//*[@id=\"ft1.1\"]/td[2]/a")
elem.click()
print "Here"

driver.save_screenshot(str(driver.title) + ".png")
print "HTMLTestRunner"
