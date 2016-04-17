import random
import os, sys

import unittest
import HTMLTestRunner

import selenium

# fp = file('my_report.html', 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(
#                 stream=fp,
#                 title='My unit test',
#                 description='This demonstrates the report output by HTMLTestRunner.'
#                 )


class Test_Click_on_LOGIN(unittest.TestCase):
    """ Start staging.socialtables.com, enter Valid Credentials and Login.
email id: piyush.patel@kiwiqa.com
password: patel22781 """
    # def __init__(self):
        # super(Click_on_LOGIN, self).__init__()
        # self.arg = arg
        # self.Demo_Function()

    def  startUp(self):
        pass

    def test_Demo(self):
        # print "Here"
        self.assertTrue( random.random() > 0.5)


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
