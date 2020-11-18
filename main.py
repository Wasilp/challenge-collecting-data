from lxml import etree
from bs4 import BeautifulSoup
import requests
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/Users/wasilewski/Downloads/chromedriver')

url = 'https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&hash=82d1fed181cf30aaa8408f90d99003d3&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery'


driver.get(url)  
sleep(3)
python_button = driver.find_element_by_xpath("//li[contains(@class, 'last')]/a").click()
print(python_button)
# And then it's like Beautiful soup
soup=BeautifulSoup(driver.page_source,'xml')

# And then it's like Beautiful soup
print(soup)
print(soup.text)