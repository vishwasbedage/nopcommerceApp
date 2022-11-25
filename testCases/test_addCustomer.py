import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.addcustomerpage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addcustomer(self,setup):
        self.logger.info("********** Test_003_AddCustomer ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*********** Login successful ************* ")

        self.logger.info("********** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)           # add_customer  = page object class
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomermenuitem()
        self.addcust.clickonAddNew()

        self.logger.info("********* Providing customer info **********")

        self.email = random_generator()+"@gmail.com"      ##we can generate random email ids
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("123456")
        self.addcust.setFirstName("ABC")
        self.addcust.setLastName("XYZ")
        self.addcust.selectGender("Male")
        self.addcust.setDOBirth("10/31/1996")
        self.addcust.setCompanyName("Amdocs")
        self.addcust.taxAttempt()
        # self.addcust.selectnewslatter("Your store name")
        self.addcust.selectActive()
        self.addcust.admin_Comment("Random comment")
        self.addcust.saveData()

        self.logger.info("******** Saving customer info **********")
        self.logger.info("********* Add customer validation ********")

        self.msg = self.driver.find_element(By.NAME,"body").text
        print(self.msg)

        if 'customer has been added succsefully.' in self.msg:
            assert True == True
            self.logger.info("******* Add customer test passed******")
        else:
            self.driver.save_screenshot("..\\Screenshots\\"+ "test_addcustomer_scr.png")
            self.logger.error("****** Add customer Test failed ******")
            assert True == False

        self.driver.close()
        self.logger.info(("****** Ending add_customer test ****** "))


# this code generate random 8 char for email address
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))