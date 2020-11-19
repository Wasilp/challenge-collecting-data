# Utils function for crapy scraping 
from selenium import webdriver
import time

def hasxpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False