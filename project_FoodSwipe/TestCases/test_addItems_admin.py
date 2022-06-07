import time

from selenium import webdriver

from Pages.FoodSwipe_homePage_admin import HomePage
from Utils.browser_Page import TestData
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import pytest


import unittest
import sys
import os
import HtmlTestRunner
import logging


logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/AddItem_Admin.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_AddItems(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()

    def test_1_login_Admin(self):
        driver=self.driver
        sip=SignInPage(driver)
        sip.do_login('nishu@deloitte.com','Foodswipe@123')
        assert driver.title=="Hasher's Food Swipe"
        logger.info('Login successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/"+"login.png")
    #Adding item

    def test_2_addItem(self):
        driver=self.driver
        hp = HomePage(driver)
        time.sleep(10)
        hp.do_clickAddItems()
        hp.do_addItems('Item002', 'Demo item for testing', '101', 'Lunch', '10')

        msg=hp.get_successLink()
        assert msg=='Item Added succesfully!'
        logger.info('Item added successfully')
        driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "itemAdded_from_Admin.png")
        hp.close_addItemScreen()


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


# python3 -m pytest test_addItems_admin.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/AddItem.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_addItems_admin.py



