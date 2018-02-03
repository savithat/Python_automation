'''
Created on Dec 30, 2017

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()



    def tearDown(self):
        pass


    def testSwitchToFrame(self):
        iFrameid ="iframeResult"
        tryItLocatorXpath = "/html/body/button"
        iFrameElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id(iFrameid))
        driver.switch_to_frame(iFrameElement)
        tryItLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(tryItLocatorXpath))
        tryItLocatorElement.click()
        alert = driver.switch_to_alert()
        alert.dismiss()
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSwitchToFrame']
    unittest.main()