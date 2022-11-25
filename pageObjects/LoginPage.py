##### This is page object class ####

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    testbox_UserName_id = "Email"
    testbox_Password_id = "Password"
    button_Login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktest = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.testbox_UserName_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.testbox_UserName_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.testbox_Password_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.testbox_Password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_Login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktest).click()











