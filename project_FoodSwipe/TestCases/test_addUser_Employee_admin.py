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
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/AddEmployee_admin.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_AddNewEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()


    def test_1_login(self):
        driver=self.driver
        sip=SignInPage(driver)
        sip.do_login('nishu@deloitte.com','Foodswipe@123')
        assert driver.title=="Hasher's Food Swipe"
        logger.info('Login successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/"+"login.png")

    def test_2_AddNewEmployee(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.goto_settings()
        logger.info('Inside settings frame')
        hp.click_adduser()
        time.sleep(2)
        time.sleep(2)
        hp.addUser_Employee('fname12','lname','fname006@deloitte.com','8734567330')
        try:
            msg = hp.get_successLink()
            assert msg == 'User Added succesfully!'
            logger.info('User added successfully')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "AddUser_Admin.png")
        except:
            logger.info('User not added')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "AddUser_Admin.png")



    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


# python3 -m pytest test_addUser_Employee_admin.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/AddUser_Employee.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_addUser_Employee_admin.py


