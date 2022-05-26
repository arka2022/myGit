from Pages.locators import locators

class Moisturizers():
    def __init__(self,driver):
        self.driver=driver
    def add_moisturizers(self):
        self.driver.find_element_by_xpath(locators.add_tigranAloeIsolani_btn).click()
    def click_cart(self):
        self.driver.find_element_by_xpath(locators.cart_button).click()

