import time

from Pages.locators import locators

class MyProfile:
    def __init__(self,driver):
        self.driver=driver

    def add_personalInfo_female(self,fname,lname):
        personalInfo_edit_button=self.driver.find_element_by_xpath(locators.personalInfo_edit_button)
        myProfile_button = self.driver.find_element_by_xpath(locators.my_profile_link1)
        myProfile_button.click()
        time.sleep(3)
        #driver.execute_script("arguments[0].scrollIntoView();",personalInfo_edit_button )
        personalInfo_edit_button.click()
        personalInfo_FirstName_textbox = self.driver.find_element_by_xpath(locators.personalInfo_FirstName_textbox)
        personalInfo_FirstName_textbox.clear()
        personalInfo_FirstName_textbox.send_keys(fname)
        personalInfo_LastName_textbox  = self.driver.find_element_by_xpath(locators.personalInfo_LastName_textbox)
        personalInfo_LastName_textbox.clear()
        personalInfo_LastName_textbox.send_keys(lname)
        personalInfo_female_checkbox = self.driver.find_element_by_xpath(locators.personalInfo_female_checkbox)
        personalInfo_female_checkbox.click()
        personalInfo_save_button=self.driver.find_element_by_xpath(locators.personalInfo_save_button)
        personalInfo_save_button.click()

    def click_manage_addresses(self):
        manageAddress_link=self.driver.find_element_by_xpath(locators.manageAddress_link)
        manageAddress_link.click()
    def add_new_address_home(self,name,ph,pin,locality,address):
        manageAddress_AddNewAddress_link = self.driver.find_element_by_xpath(locators.manageAddress_AddNewAddress_link)
        manageAddress_AddNewAddress_link.click()
        manageAddress_name_textbox = self.driver.find_element_by_xpath(locators.manageAddress_name_textbox)
        manageAddress_name_textbox.send_keys(name)
        manageAddress_mobileNumber_textbox = self.driver.find_element_by_xpath(locators.manageAddress_mobileNumber_textbox)
        manageAddress_mobileNumber_textbox.send_keys(ph)
        manageAddress_pincode_textbox = self.driver.find_element_by_xpath(locators.manageAddress_pincode_textbox)
        manageAddress_pincode_textbox.send_keys(pin)
        manageAddress_locality_textbox = self.driver.find_element_by_xpath(locators.manageAddress_locality_textbox)
        manageAddress_locality_textbox.send_keys(locality)
        manageAddress_address_textbox = self.driver.find_element_by_xpath(locators.manageAddress_address_textbox)
        manageAddress_address_textbox.send_keys(address)
        manageAddress_home_checkbox = self.driver.find_element_by_xpath(locators.manageAddress_home_checkbox)
        manageAddress_home_checkbox.click()
        manageAddress_save_button = self.driver.find_element_by_xpath(locators.manageAddress_save_button)
        #driver.execute_script("arguments[0].scrollIntoView();",manageAddress_save_button )
        manageAddress_save_button.click()




