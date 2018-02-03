'''
Created on Jan 30, 2018

@author: jagad
'''
import unittest
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pdb



class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com/")    
        driver.maximize_window()
        #pdb.set_trace()


    def tearDown(self):
        driver.quit()


    def test_header_traverse(self):
        amazon_header_xpath = "//*[@id='navbar']"
        amazon_header_Elements = driver.find_element_by_xpath(amazon_header_xpath)
        header_link = amazon_header_Elements.find_elements_by_tag_name("a")
        print( header_link)
        header_size = header_link.count("element")
        print(header_size)       
        
        
            
            #print(each)"""
        
        """#pdb.set_trace()
        ele_tag = "header"
        ale_tag_loc = driver.find_elements_by_tag_name(ele_tag)
        pdb.set trace()
        print (ale_tag_loc)"""
        
      
        #all_children_elements = amazon_header_Elements.find_element_by_css_selector() 
       # for child in all_children_elements:
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()