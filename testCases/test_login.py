from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import pytest
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseurl = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()
    # baseurl = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    # @pytest.mark.sanity
    # @pytest.mark.regrassion

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("**************** Test_001_login *********************")
        self.logger.info("**************** verifying home page title *********************")
        self.driver = setup                 ## webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("****************** HOME PAGE TITLE TEST PASS *********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** HOME PAGE TITLE TEST FAILED ***********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*************** Verifying Login test ***************")
        self.driver = setup              ## webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******************  Login Test passed **************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**********************  LOGIN TEST Failed ***************************")
            assert False














