# Utils function for crapy scraping 
from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import requests
import selenium
from threading import Thread, RLock
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def hasxpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


class LinkThread(Thread):
    def __init__(self, url,link = []):
        Thread.__init__(self)
        self.url = url

    def run(self):
        link = []
        lock = RLock()
        with lock:
            driver = webdriver.Chrome('/Users/wasilewski/Downloads/chromedriver')
            driver.get(self.url)
            # waiting 3 second to avoid any problem cause internet connection,
            driver.implicitly_wait(3)

            driver.find_element_by_id("didomi-notice-agree-button").click()
            driver.implicitly_wait(3)

            soup=BeautifulSoup(driver.page_source,'xml')
            xpath = "//li[contains(@class, 'last disabled')]/a"
            while hasxpath(driver,xpath) == False:
                for elem in soup.find_all('div',attrs={"class" :"property-item_title "}):
                    link = ('https://www.zimmo.be' + elem.a.get('href'))
                    df=pd.DataFrame({link})
                    df.to_csv('zimmo_details_link.csv',  mode='a', header=False, index=False)
                #Click action to manage pagination
                driver.find_element_by_xpath("//li[contains(@class, 'last')]/a").click()
                
                sleep(4)