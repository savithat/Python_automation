'''
Created on Dec 25, 2017

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://travelingtony.weebly.com/")
        driver.maximize_window()


    def tearDown(self):
        pass


    def testExcercise(self):
        searchLocate = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_name('q'))
        searchLocate.send_keys("leatherback")
        searchLocate.submit()
               
               
        """
        instead of send key if u want use click
        searchButtonLocate = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath("//*[@id='wsite-header-search-form']/span"))
        searchButtonLocate.click()
         """
         
        leatherBackPicLocator = "//*[@id='wsite-search-product-results']/li/a/div"
        leatherBackPicElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(leatherBackPicLocator))
        leatherBackPicElement.click()
        
        
        quantity3Locator = "//*[@id='wsite-com-product-option-Quantity']"
        quantity3Element = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(quantity3Locator))
        Select(quantity3Element).select_by_visible_text("3")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testExcercise']
    unittest.main()