import time
import webbrowser
from selenium import webdriver
import pytest
from Config.config import TestData
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner


#unittest is a pre-build unittest framework in python
#we just have to derive it's methods
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)

    def test_login_validation(self):
        driver=self.driver
        login=LoginPage(driver)
        login.enter_username(TestData.userName)
        login.enter_password(TestData.password)
        login.click_submit_btn()
        assert driver.title=='OrangeHRM'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=='++main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/arkapdas/PycharmProjects/pythonSelProject1/Test_Result'))



#/Users/arkapdas/PycharmProjects/pythonSelProject1/TestCases/




