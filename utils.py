# Utils function for crapy scraping 
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import requests
import selenium
from threading import Thread, RLock
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




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
     def __init__(self,url):
            Thread.__init__(self)
            self.url = url

    # def run(self):
    #   #There we will make a csv file with all data and format them if needed 
    #   getLocality(driver)
    #   getPrice(driver)
    #   getRoom(driver)
    #   getArea(driver)
    #   getKitchen(driver)
    #   getFurnished(driver)
    #   getFire(driver)
    #   getTerrace(driver)
    #   getTerraceArea(driver)
    #   getGarden(driver)
    #   getGardenArea(driver)
    #   getSurface(driver)
    #   getFacade(driver)
    #   getPool(driver)
    #   getState(driver)
    #   getSaleType(driver)
    #   getGarden(driver)
    #   getPropertyType(driver)
    #   getsubType(driver)
    # Get all values and append it to a csv file for each thread
