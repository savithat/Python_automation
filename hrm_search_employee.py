'''
Created on Jan 12, 2018

@author: jagad
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class Test(unittest.TestCase):


    def setUp(self):
        global driver;
        name = "sweta"
        password = "november!"
        driver = webdriver.Chrome();
        driver.get("http://local.school.portnov.com:4515/symfony/web/index.php/auth/login");
        driver.maximize_window();
        userNameLocator_id = "txtUsername";
        passwordLocator_id = "txtPassword";
        loginLocator_id = "btnLogin"
        userNmaeLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id(userNameLocator_id));
        userNmaeLocatorElement.send_keys(name)
        passworNmaeLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id(passwordLocator_id));
        passworNmaeLocatorElement.send_keys(password);    
        loginLocatorElement = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id(loginLocator_id)).click();
        
                                                    
        
        


    def tearDown(self):
        pass 
        #driver.quit();


    def testhrm_search_employee(self):
        
        EmployeeNameLaocator_xpath = "//*[@id='empsearch_employee_name_empName']";
        SearchButtonLocator_id = "searchBtn"
        Search_name = "nat fillo"
        ClickOnSearcNameLocator_xpath = "//*[text()='nat']"
        
        EmployeeNameLaocatorElement_xpath = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(EmployeeNameLaocator_xpath));
        EmployeeNameLaocatorElement_xpath.send_keys(Search_name)
        SearchButtonLocatorElement_id = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(SearchButtonLocator_id));
        SearchButtonLocatorElement_id.click();
        ClickOnSearcNameLocatorElement_xpath = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(ClickOnSearcNameLocator_xpath)); 
        ClickOnSearcNameLocatorElement_xpath.click();
        
        jobLocator_xpath = "//*[@id='sidenav']/li[6]/a";
        editLocator_id = "btnSave"
        
        
        jobLocatorElement_xpath = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(jobLocator_xpath)); 
        jobLocatorElement_xpath.click();
        editLocatorElement_id = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(editLocator_id));
        editLocatorElement_id.click();
        
        jobTitleLocator_xpath = "//*[@id='job_job_title']"
        savebuttonLocator_id = "btnSave"
        
        jobTitleLocatorElement_id = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(jobTitleLocator_xpath));
        Select(jobTitleLocatorElement_id).select_by_value("42");
        savebuttonLocatorElement_id = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(savebuttonLocator_id));
        savebuttonLocatorElement_id.click();
        
        employeeListLocator_xpath = '//*[@id="menu_pim_viewEmployeeList"]'
        employeeListLocatorElement_xpath = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_xpath(employeeListLocator_xpath));
        employeeListLocatorElement_xpath.click();
        
        jobTitleLocator_id = 'empsearch_job_title'
        SearchButtonLocator_id = "searchBtn"
        
        jobTitleLocatorElement_id = WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(jobTitleLocator_id));
        Select(jobTitleLocatorElement_id).select_by_index(5)
        SearchButtonLocatorElement_id =  WebDriverWait(driver, 10).\
        until(lambda driver:driver.find_element_by_id(SearchButtonLocator_id));
        SearchButtonLocatorElement_id.click();
        
        #check jobtitle = HHH using assertequal
        
        
                
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testhrm_search_employee']
    unittest.main()