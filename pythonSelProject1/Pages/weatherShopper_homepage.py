from Pages.locators import locators

class weatherShopper_homepage():
    def __init__(self, driver):
        self.driver=driver
        self.temp_webElement_xpath=locators.temp_webElement_xpath

    def check_temperature(self):
        t=self.driver.find_element_by_xpath(locators.temp_webElement_xpath).text
        return t
    def buy_moisturizers(self):
        self.driver.find_element_by_xpath(locators.buyMoist_button_xpath).click()

    def buy_sunscreems(self):
        self.driver.find_element_by_xpath(locators.buySunscre_button_xpath).click()


