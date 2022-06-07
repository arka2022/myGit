import time

from selenium import webdriver

from Pages.FoodSwipe_SignUP_page import SignUP_Page
from Pages.FoodSwipe_homePage_admin import HomePage
from Utils.browser_Page import TestData
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import unittest
import sys
import pytest

import HtmlTestRunner
import logging


logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/RegisterUser.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class UserRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()

    def test_doRegistration(self):
        driver = self.driver
        dsu=SignUP_Page(driver)
        logger.info("Moved to signUp page")
        dsu.goto_signUp()
        dsu.do_signUp('arka101','das','arka101@deloitte.com','7524178009','Test@1234','Test@1234')
        logger.info("SignUp Done")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


# python3 -m pytest test_registerUser.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/RegisterUser.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_registerUser.py




