import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities.XLUtils import XLUtils
import time


class Test_002_DDT_login:
    baseurl = Readconfig.getApplicationURL()
    path = "./TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******** test_002_DDt_Login ********")
        self.logger.info("******** Verifying Login DDT test ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)
        lst_status = []            ## Empty list variable

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    print("***** Passed ****")
                    self.lp.clicklogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    print("***** Failed ****")
                    # lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    print("***** failed ****")
                    self.lp.clicklogout()
                    lst_status.append("fail")
                elif self.exp == "fail":
                    print("***** Passed ***")
                    lst_status.append("pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test Failed ****")
            self.driver.close()
            assert False

        self.logger.info("****** End of login DDT test *******")
        self.logger.info("****** Complete TC login DDT *******")









