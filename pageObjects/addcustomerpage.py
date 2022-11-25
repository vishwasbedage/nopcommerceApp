import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
        customer_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
        sub_customers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
        add_button_xpath = "//a[@class='btn btn-primary']"
        text_email_id = "//input[@id='Email']"
        text_password_id = "//input[@id='Password']"
        text_first_name = "//input[@id='FirstName']"
        text_last_name = "//input[@id='LastName']"
        redio_button_male = "//input[@id='Gender_Male']"
        redio_button_female = "//input[@id='Gender_Female']"
        text_dob_id = "//input[@id='DateOfBirth']"
        text_company_name = "//input[@id='Company']"
        checkbox_tax_except = "//input[@id='IsTaxExempt']"
        select_news_letter = "//div[@class='input-group-append']//div[@role='listbox']"
        select_news_letter_your_store_name = "//div[@class='input-group-append']//div[@role='listbox']"
        select_news_letter_your_teststore2 = "//span[normalize-space()='Test store 2']"
        select_customer_role = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
        select_customer_Adminstrator = "//span[normalize-space()='Administrators']"
        select_customer_Forum_Moderator = "//span[normalize-space()='Forum Moderators']"
        select_customer_Guests = "//span[normalize-space()='Guests']"
        select_customer_Vendors =  "// li[contains(text(), 'Vendors')]"
        select_customer_Register = "//span[normalize-space()='Registered']"
        select_manager_vendor_id = "//select[@id='VendorId']"
        checkbox_active_id = "//input[@id='Active']"
        text_admin_comment_box = "//textarea[@id='AdminComment']"
        button_save = "//button[@name='save']"

        def __int__(self,driver):
                self.driver = driver

        def clickoncustomermenu(self):
                self.driver.find_element(By.XPATH,self.customer_xpath).click()

        def clickoncustomermenuitem(self):
                self.driver.find_element(By.XPATH,self.sub_customers_xpath).click()

        def clickonAddNew(self):
                self.driver.find_element(By.XPATH,self.add_button_xpath).click()

        def setEmail(self,email):
                self.driver.find_element(By.ID,self.text_email_id).clear()
                self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

        def setPassword(self,password):
                self.driver.find_element(By.ID,self.text_password_id).clear()
                self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

        def setFirstName(self,firstName):
                self.driver.find_element(By.ID, self.text_first_name).clear()
                self.driver.find_element(By.ID,self.text_first_name).send_keys(firstName)

        def setLastName(self,lastName):
                self.driver.find_element(By.ID,self.text_last_name).clear()
                self.driver.find_element(By.ID,self.text_last_name).send_keys(lastName)

        def selectGender(self,gender):
                if gender == "Male":
                        self.driver.find_element(By.ID,self.redio_button_male).click()
                elif gender == "Female":
                        self.driver.find_element(By.ID, self.redio_button_female).click()
                else:
                        self.driver.find_element(By.ID, self.redio_button_male).click()

        def setDOBirth(self,dob):
                self.driver.find_element(By.ID,self.setDOBirth()).send_keys(dob)

        def setCompanyName(self,companyName):
                self.driver.find_element(By.XPATH,self.text_company_name).send_keys(companyName)

        def taxAttempt(self):
                self.driver.find_element(By.XPATH,self.taxAttempt()).click()

        def selectNewsletter(self,news):
                self.driver.find_element(By.XPATH,self.select_news_letter).click()
                if news == "Your store name":
                        self.driver.find_element(By.XPATH,self.select_news_letter_your_store_name).click()
                elif news == "Test store 2":
                        self.driver.find_element(By.XPATH,self.select_news_letter_your_teststore2).click()
                else:
                        self.driver.find_element(By.XPATH, self.select_news_letter_your_store_name).click()

        def mangerRole(self,value):
            self.driver.find_element(By.XPATH,self.mangerRole()).click()
            if value == "Administrators":
                    self.select_customer_Adminstrator = self.driver.find_element(By.XPATH,self.select_customer_Adminstrator).click()
            elif value == "Forum Moderators":
                    self.select_customer_Forum_Moderator=self.driver.find_element(By.XPATH,self.select_customer_Adminstrator).click()
            elif value == "Guests":
                    self.select_customer_Guests=self.driver.find_element(By.XPATH,self.select_customer_Guests).click()
            elif value == "Register":
                    self.select_customer_Register=self.driver.find_element(By.XPATH, self.select_customer_Register).click()
            elif value == "vendors":
                    self.select_customer_Vendors=self.driver.find_element(By.XPATH, self.select_customer_Vendors).click()
            else:
                    self.select_customer_Vendors = self.driver.find_element(By.XPATH, self.select_customer_Vendors).click()

            time.sleep(5)
            # self.mangerRole().click()
            self.driver.execute_script('argument[0].click();',self.mangerRole())


        def managerVendor(self,vendor):
                ele = Select(self.driver.find_element(By.ID,self.select_manager_vendor_id))
                ele.select_by_visible_text(vendor)

        def selectActive(self):
                self.driver.find_element(By.ID,self.checkbox_active_id).click()

        def admin_Comment(self,comment):
                self.driver.find_element(By.ID,self.text_admin_comment_box).send_keys(comment)

        def saveData(self):
                self.driver.find_element(By.XPATH,self.button_save).click()








