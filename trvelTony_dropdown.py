'''
Created on Dec 23, 2017

@author: jagad
'''
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from select import select


class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()


    def tearDown(self):
        pass
        #driver.quit()
        


    def testdropdown(self):
        #First Method
        
        """dropDownID = "select#wsite-com-product-option-Quantity"
        dropDownElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_css_selector(dropDownID))
        Select(dropDownElement).select_by_visible_text("2") 
        """
        
        #Second method
        
        dropDownOption = "select#wsite-com-product-option-Quantity option[value = '2']"
        dropDownOptionElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(dropDownOption))
        dropDownOptionElement.click()
    
        
        
                                          
                                                        
                                                          


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()