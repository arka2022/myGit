from Pages.locators import locators

class checkout():
    def __init__(self,driver):
        self.driver = driver
    def click_payWithCard(self):
        self.driver.find_element_by_xpath(locators.payWithCard_button).click()
    def exampleCharge_email(self,email,cardNum,date1,cvc):
        self.driver.find_element_by_xpath(locators.email_textbox).click()
        self.driver.find_element_by_xpath(locators.email_textbox).send_keys(email)
        self.driver.find_element_by_xpath(locators.cardNumber_textbox).send_keys(cardNum)
        self.driver.find_element_by_xpath(locators.monthYear_textbox).send_keys(date1)
        self.driver.find_element_by_xpath(locators.cvc_textbox).send_keys(cvc)
        self.driver.find_element_by_xpath(locators.pay_button).click()



