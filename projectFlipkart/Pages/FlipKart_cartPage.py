from Pages.locators import locators

class Cartpage:
    def __init__(self,driver):
        self.driver=driver

    def return_total_amount(self):
        total_ammount_we=self.driver.find_element_by_xpath(locators.total_ammount_we)
        return total_ammount_we.text

    def remove_baskert(self):
        remove_basket_link=self.driver.find_element_by_xpath(locators.remove_basket_link)
        remove_basket_link.click()
        popup_remove_basket_link=self.driver.find_element_by_xpath(locators.popup_remove_basket_link)
        popup_remove_basket_link.click()

