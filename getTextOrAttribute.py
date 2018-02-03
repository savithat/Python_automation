'''
Created on Dec 25, 2017

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://travelingtony.weebly.com/")
        driver.maximize_window()
        


    def tearDown(self):
        pass
        #driver.quit()


    def testgetAttribute(self):
        photoButtonLocator = ".wsite-button-inner "
        photoButtonElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_css_selector(photoButtonLocator))
        text = photoButtonElement.text
        classAttribute=photoButtonElement.get_attribute("class")
        print(classAttribute)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()