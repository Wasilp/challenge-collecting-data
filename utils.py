# Utils function for crapy scraping 
from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import requests
import selenium
from threading import Thread, RLock
from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options




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
        lock = RLock()

        with lock:
            driver = uc.Chrome()
            driver.get(self.url)

            driver.find_element_by_id("didomi-notice-agree-button").click()
            driver.implicitly_wait(3)
            soup=BeautifulSoup(driver.page_source,'xml')
            xpath = "//li[contains(@class, 'last disabled')]/a"
            while hasxpath(driver,xpath) == False:
                current_url = driver.current_url
                driver.get(current_url)
                soup=BeautifulSoup(driver.page_source,'xml')
                uniqueItem =[]
                links = []
                for elem in soup.find_all('div',attrs={"class" :"property-item_title "}):
                    links.append('https://www.zimmo.be' + elem.a.get('href'))
                    print(elem.a.get('href'))
                for link in links:
                    print(link)
                    if link not in uniqueItem:
                        uniqueItem.append(uniqueItem)
                        df=pd.DataFrame({link})
                        df.to_csv('zimmo_details_link.csv',  mode='a', header=False, index=False)
                #Click action to manage pagination
                driver.find_element_by_xpath("//li[contains(@class, 'last')]/a").click()
                # wait for URL to change with 15 seconds timeout
                WebDriverWait(driver, 15).until(EC.url_changes(current_url))
 
            driver.close()





class DetailsThread(Thread):
     def __init__(self,
            locality:int, 
            price:int, 
            room:int, 
            area:int, 
            kitchen:int, 
            furnished:int, 
            fire:int, 
            terrace:int, 
            terraceArea:int, 
            garden:int, 
            gardenArea:int, 
            surface:int, 
            facade:int, 
            pool:int,
            state:str,
            saleType:str,
            propertyType:str,
            subType:str 
        ):
            Thread.__init__(self)
            self.locality = locality
            self.price = price
            self.room = room
            self.area = area
            self.kitchen = kitchen
            self.furnished = furnished
            self.fire = fire
            self.terrace = terrace
            self.terraceArea = terraceArea
            self.garden = garden
            self.gardenArea = gardenArea
            self.surface = surface
            self.facade = facade
            self.pool = pool
            self.state = state
            self.saleType = saleType
            self.propertyType = propertyType
            self.subType = subType

    # def run(self):
    #   #There we will make a csv file with all data and format them if needed        