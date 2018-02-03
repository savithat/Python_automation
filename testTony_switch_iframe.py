'''
Created on Jan 22, 2018

@author: jagad
'''
import unittest
from selenium import webdriver


class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_w3schools")
        driver.maximize_window()


    def tearDown(self):
        


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()