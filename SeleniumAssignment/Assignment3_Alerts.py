import time
import webbrowser

import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import service

from selenium.webdriver.common.by import By


driver= webdriver.Chrome("/Users/arkapdas/PycharmProjects/pythonProject/drivers/chromedriver")
driver.get("https://the-internet.herokuapp.com/ ")
jsa_we=driver.find_element(By.XPATH,"//a[contains(text(),'JavaScript Alerts')]")
jsa_we.click()
time.sleep(2)
btn=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
btn.click()
a=Alert(driver)
print(a.text)
a.send_keys("arka")
a.accept()
time.sleep(2)

op=driver.find_element(By.XPATH,"//p[@id]")
print(op.text)
