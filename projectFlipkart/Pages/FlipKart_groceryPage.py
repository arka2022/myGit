import time

from Pages.locators import locators

class Grocerypage:
    def __init__(self,driver):
        self.driver=driver

    def add_Three_random_item(self,driver):
        #Not scrolling to the main page
        more_button=self.driver.find_element_by_xpath(locators.more_button)
        more_button.click()


        milk_link = self.driver.find_element_by_xpath(locators.milk_link)
        driver.execute_script("arguments[0].scrollIntoView();", milk_link)
        time.sleep(2)
        buscuit_link=self.driver.find_element_by_xpath(locators.buscuit_link)
        buscuit_link.click()
        time.sleep(2)
        add_button=self.driver.find_element_by_xpath(locators.addCart_randomItem_button1)
        add_button.click()






