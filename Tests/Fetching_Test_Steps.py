import os, sys
from TestCase_1 import TestCase_1

class Fetching_Test_Steps(object):

    def __init__(self, List_Of_Objectives, path_Of_Excel):

        super(Fetching_Test_Steps, self).__init__()

        for i in List_Of_Objectives:
            self.Test_Case_1_Ref = TestCase_1(path_Of_Excel, i)

            self.test_Cases_To_Execute = self.Test_Case_1_Ref.create_Test_Steps()


    def Run_Test_Steps(self):

        for test_Cases_To_Execute in self.test_Cases_To_Execute:

            if "on_LOGIN" in test_Cases_To_Execute:
                print os.system("python ./Test_Steps/" + test_Cases_To_Execute + ".py")

            # os.system("python ")


a = Fetching_Test_Steps(["Name on Events Page"], "../SocialTables_tBlocks Test cases sheet V1.0.xlsx")

print a.test_Cases_To_Execute

a.Run_Test_Steps()
