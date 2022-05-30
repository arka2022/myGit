import time

from Pages.locators import locators

class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.loginButton=driver.find_element_by_xpath(locators.login_button)
        #Objects of login pop-up screen
        self.username_popup=driver.find_element_by_xpath(locators.login_popup_email_textbox)
        self.paswrd_popup=driver.find_element_by_xpath(locators.login_popup_password_textbox)
        self.login_btn_popup=driver.find_element_by_xpath(locators.login_popup_login_button)



    def do_login(self,uname,password):
        #self.username_popup.click()
        self.username_popup.send_keys(uname)
        #self.paswrd_popup.click()
        self.paswrd_popup.send_keys(password)
        self.login_btn_popup.click()

    def click_login(self):
        self.loginButton.click()

    def goto_myProfile(self,driver):
        myProfile_button= self.driver.find_element_by_xpath(locators.my_profile_link1)
        myProfile_button.click()
        time.sleep(5)
        myProfile_button.click()
        myProfile_button2= self.driver.find_element_by_xpath(locators.my_profile_link2)
        myProfile_button2.click()

    def goto_grocery(self):
        grocery_link=self.driver.find_element_by_xpath(locators.grocery_link)
        grocery_link.click()

    def goto_cart(self):
        cart_button=self.driver.find_element_by_xpath(locators.cart_button)
        cart_button.click()
    def goto_fashon(self):
        fashon_link=self.driver.find_element_by_xpath(locators.fashion_link)
        #driver.execute_script("arguments[0].scrollIntoView();", fashon_link)
        #fashon_link.click()
        fashon_all_link=self.driver.find_element_by_xpath(locators.fashon_all_link)
        #river.execute_script("arguments[0].scrollIntoView();", fashon_all_link)
        fashon_all_link.click()
        time.sleep(3)
        fashon_all_link.click()

    def goto_logout(self,driver):
        myProfile_button= self.driver.find_element_by_xpath(locators.my_profile_link1)
        myProfile_button.click()
        time.sleep(5)
        myProfile_button.click()
        logout_button= self.driver.find_element_by_xpath(locators.logout)
        logout_button.click()


















