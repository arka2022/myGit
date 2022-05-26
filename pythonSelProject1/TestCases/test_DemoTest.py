import time
import webbrowser
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/arkapdas/PycharmProjects/pythonSelProject1/Log/mylog.txt', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

driver= webdriver.Chrome("/Users/arkapdas/PycharmProjects/pythonProject/drivers/chromedriver")
#implicit wait
driver.implicitly_wait(5) #seconds
driver.get("https://weathershopper.pythonanywhere.com/cart")
#print(driver.current_window_handle)
driver.find_element_by_xpath("//button[@class='stripe-button-el']").click()
logger.warning("Click to checkout button")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='emailInput input']").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='emailInput input']").send_keys("abc@qwe.com")


