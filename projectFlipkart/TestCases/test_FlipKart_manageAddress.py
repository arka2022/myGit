import time
import webbrowser
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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

from Pages.FlipKart_myProfile_page import MyProfile
from Pages.Flipkart_HomePage import HomePage


class Flipkart_LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        time.sleep(1)

    def test_edit_PersonalInfo(self):
        driver = self.driver
        hp = HomePage(driver)
        #Login
        hp.do_login(xlData.user,xlData.password)
        time.sleep(3)
        assert driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        logger.info('Login successful')
        #Navigate to My Profile
        hp.goto_myProfile(driver)
        logger.info("Navigate to my profile page")
        time.sleep(3)

        #Add/Edit Personal Information
        mp=MyProfile(driver)
        mp.add_personalInfo_female(xlData.F_name,xlData.L_name)
        logger.info('Personal Information edited')

        #Click manage addresses link
        mp.click_manage_addresses()
        logger.info('Navigate to manage addresses')

        #Add new home address
        mp.add_new_address_home(xlData.name,xlData.mobile,xlData.pin,xlData.locality,xlData.address)
        logger.info('New address added successfully')
        driver.save_screenshot("/Users/arkapdas/PycharmProjects/projectFlipkart/Screenshot/" + "address_page.png")



    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()
