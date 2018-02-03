'''
Created on Dec 30, 2017

@author: jagad
'''
import unittest
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select



class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://travelingtony.weebly.com/store/p3/Asala_lodge.html")
        driver.maximize_window()
        


    def tearDown(self):
        pass
    #driver.quit()


    def testSwitchWindow(self):
        facebooksharingLinkLocatorXpath = "//*[@id='wsite-com-product-social-sharing']/li[1]/a"
        facebookEmailUserNameLocatorId = "email"
        facebookEPasswordLocatorId = "pass"
        facebookLoginButtonLocatorName = "login"
        
        facebooksharingLinkLocatorElement = WebDriverWait(driver, 10).\
        until(lambda driver: driver.find_element_by_xpath(facebooksharingLinkLocatorXpath))
        mainWindowHandle = driver.window_handles
        print("main window handle=",mainWindowHandle)
        
        facebooksharingLinkLocatorElement.click()
        allWindowHandleList = driver.window_handles
        print("all window handle=",allWindowHandleList)
        
        
        for handle in allWindowHandleList:
            if handle != mainWindowHandle[0]:
                driver.switch_to_window(handle)
                break
        facebookEmailUserNameLocatorElement = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(facebookEmailUserNameLocatorId))
        facebookEmailUserNameLocatorElement.send_keys("tutorys123@gmail.com")
        facebookEPasswordLocatorElement = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(facebookEPasswordLocatorId))
        facebookEPasswordLocatorElement.send_keys("year2014")
        facebookLoginButtonLocatoElement = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_name(facebookLoginButtonLocatorName))
        facebookLoginButtonLocatoElement.click()
        
         

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSwitchWindow']
    unittest.main()