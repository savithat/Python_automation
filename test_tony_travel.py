'''
Created on Dec 23, 2017

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pdb

class Test1(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://travelingtony.weebly.com/")
        driver.maximize_window()


    def tearDown(self):
        pass
        #driver.quit()


    def test_BasicAction(self):
        contactMenuLocator = "//*[.='Contact']"
        nameFieldLocator = "//*[contains(@name,'first')]"
        contactMenuElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(contactMenuLocator))
        pdb.set_trace()
        contactMenuElement.click()
        nameFieldElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(nameFieldLocator))
        nameFieldElement.send_keys("savi")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()