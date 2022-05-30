import time
import webbrowser
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from TestData_read.ReadExcel import xlData
from TestData_read.browser_Page import TestData
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

from Pages.FlipKart_cartPage import Cartpage
from Pages.FlipKart_groceryPage import Grocerypage
from Pages.Flipkart_HomePage import HomePage


class Flipkart_LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        time.sleep(1)

    def test_check_Cart_functionality(self):
        driver=self.driver
        hp=HomePage(driver)
        hp.do_login(xlData.user,xlData.password)
        time.sleep(3)
        assert driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        logger.info('Login successful')
        #Goto Grocery
        hp.goto_grocery()
        time.sleep(5)
        logger.info('Navigate to grocery page')
        assert driver.title=="Flipkart Grocery Store - Buy Groceries Online & Get Rs.1 Deals at Flipkart.com"

        #Add 3 item on cart
        gp=Grocerypage(driver)


        gp.add_Three_random_item(driver)
        logger.info('Item added to Cart')
        time.sleep(3)

        #Goto Cart
        hp.goto_cart()
        logger.info('Navigate to cart')

        cp=Cartpage(driver)
        amount=cp.return_total_amount()
        logger.info('Total ammount is %s'%(amount))
        driver.save_screenshot("/Users/arkapdas/PycharmProjects/projectFlipkart/Screenshot/" + "cart.png")
        print(amount)
        time.sleep(5)
        cp.remove_baskert()
        logger.warning('Cart is empty')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


