from Pages.locators import locators


class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.userName_textBox_xpath=locators.userName_textBox_xpath
        self.password_textBox_xpath=locators.password_textBox_xpath
        self.submit_btn_xpath=locators.submit_btn_xpath

    def enter_username(self,username):
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys(username)

    def enter_password(self, passwod):
        self.driver.find_element_by_xpath("//input[@name='txtPassword']").send_keys(passwod)


    def click_submit_btn(self):
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()