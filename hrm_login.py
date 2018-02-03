'''
Created on Dec 26, 2017

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait







class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://local.school.portnov.com:4515/symfony/web/index.php/auth/login")
        driver.maximize_window()


    def tearDown(self):
        driver.quit()


    def testLogin(self):
        userNameLocator = "txtUsername"
        userNameLocatorElement= WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_name( userNameLocator))
       # userNameLocatorElement.click()
        userNameLocatorElement.send_keys("sweta")
        passwordNameLocator =  WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_name("txtPassword"))
        #passwordNameLocator.click()
        passwordNameLocator.send_keys("november!")
        loginLocator = "//*[@id = 'btnLogin']"
        loginLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath(loginLocator))
        loginLocatorElement.click()
        expectedMessage = "Welcome sweta"
        welcomeElememt = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("welcome"))
        actualMessage = welcomeElememt.text
        print(actualMessage)
        self.assertEqual(expectedMessage, actualMessage, print("pass"))  
        
        addEmployeeLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("menu_pim_addEmployee"))
        addEmployeeLocatorElement.click()
        employeeIdLocator = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("employeeId")) 
        employeeIdValue = employeeIdLocator.get_attribute("value")
        
        
        fullNamelocatorElememt =  WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("firstName"))
       # fullNamelocatorElememt.click()        
        fullNamelocatorElememt.send_keys("mary")
        lastNamelocatorElememt =  WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("lastName"))
      #  lastNamelocatorElememt.click()
        lastNamelocatorElememt.send_keys("com")

        saveButtonLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("btnSave"))
        saveButtonLocatorElement.click()
        
        employeeListLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_link_text("Employee List"))
        employeeListLocatorElement.click()
        
        idLocatorElemet = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("empsearch_id"))
        idLocatorElemet.send_keys(employeeIdValue)
        searchLocatorElement =  WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("searchBtn"))
        searchLocatorElement.click()
        
        welcomeLocaotorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath("//*[@id='welcome']"))
        welcomeLocaotorElement.click()        
                                          
        logOutElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_link_text("Logout"))
        logOutElement.click()
         
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogin']
    unittest.main()