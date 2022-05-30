import time
import webbrowser
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import html
from Config.ReadExcel import xlData
from Config.config import TestData
import unittest
import sys
import os


import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/arkapdas/PycharmProjects/projectFlipkart/Log/ProjectLog.txt', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

from Pages.Flipkart_HomePage import HomePage


class Flipkart_LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        time.sleep(1)

    def test_login_validation(self):
        driver=self.driver
        hp=HomePage(driver)
        hp.do_login(xlData.user,xlData.password)
        time.sleep(3)
        assert driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        logger.info('Login successful')
        driver.save_screenshot("/Users/arkapdas/PycharmProjects/projectFlipkart/Screenshot/"+"login.png")



    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


#pytest -s -v --html=/Users/arkapdas/PycharmProjects/projectFlipkart/Results/LOGIN.html /Users/arkapdas/PycharmProjects/projectFlipkart/TestCases/test_FlipKart_Login.py



