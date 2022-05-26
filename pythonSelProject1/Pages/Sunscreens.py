from Pages.locators import locators

class Sunscreems():
    def __init__(self,driver):
        self.driver=driver
    def add_Sunscreems(self):
        self.driver.find_element_by_xpath(locators.add_akibaAmazingSPF50_btn).click()
    def click_cart(self):
        self.driver.find_element_by_xpath(locators.cart_button).click()

