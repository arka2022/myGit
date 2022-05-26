import time
import webbrowser
from selenium import webdriver
import pytest
from Config.config import TestData
import unittest
import sys
import os
import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/arkapdas/PycharmProjects/pythonSelProject1/Log/mylog.txt', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

from Pages.Checkout_CartItems import checkout
from Pages.Moisturizers import Moisturizers
from Pages.Sunscreens import Sunscreems
from Pages.weatherShopper_homepage import weatherShopper_homepage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner


#unittest is a pre-build unittest framework in python
#we just have to derive it's methods

logging.basicConfig(filename="newfile.txt",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url1)


    def test_weatherShoping(self):


        driver=self.driver
        ws=weatherShopper_homepage(driver)
        ts=ws.check_temperature()
        ts_num=''
        for i in ts:
            if i.isdigit():
                ts_num+=i
        logger.info("Temperature is %s"%(int(ts_num)))
        if int(ts_num) > 30:
            logger.info("Enter to sunscreen page ")
            ws.buy_sunscreems()
            assert driver.title=="The Best Sunscreens in the World!"
            sc=Sunscreems(driver)
            sc.add_Sunscreems()
            logger.info("Adding item to cart")
            sc.click_cart()
            logger.info("Click button to enter the cart")
            co = checkout(driver)
            co.click_payWithCard()
            logger.info("Click on Pay with Card button")
            time.sleep(4)
            co.exampleCharge(TestData.email, TestData.cardNum, TestData.date1, TestData.cvc)
            time.sleep(10)


        else:
            ws.buy_moisturizers()
            logger.info("Login to Moisturizer page")
            assert driver.title=="The Best Moisturizers in the World!"
            mo=Moisturizers(driver)
            sc1 = Sunscreems(driver)
            mo.add_moisturizers()
            logger.info("Adding item to cart")
            sc1.click_cart()
            logger.info("Click button to enter the cart")
            co = checkout(driver)
            co.click_payWithCard()
            logger.info("Click on Pay with Card button")
            time.sleep(4)
            co.exampleCharge_email(TestData.email, TestData.cardNum, TestData.date1, TestData.cvc)
            time.sleep(10)





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=='++main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/arkapdas/PycharmProjects/pythonSelProject1/Test_Result'))



#/Users/arkapdas/PycharmProjects/pythonSelProject1/TestCases/




