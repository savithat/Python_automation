'''
Created on Dec 30, 2017

@author: jagad
'''
import unittest
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait



class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://www.tizag.com/javascriptT/javascriptconfirm.php")
        driver.maximize_window()


    def tearDown(self):
        pass


    def testSwichFocusAlert(self):
        leaveTizagBottonXpath = "//*[@value='Leave Tizag.com']"
        leaveTizagBottonElement = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(leaveTizagBottonXpath))
        leaveTizagBottonElement.click()
        alert = driver.switch_to_alert()
        alert.accept()
        #alert.dismiss()
        alert = driver.switch_to_alert()
        alert.accept()
        
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSwichFocusAlert']
    unittest.main()