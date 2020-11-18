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

url = 'https://immo.vlan.be/fr/immobilier/maison?transactiontypes=a-vendre,en-vente-publique&propertysubtypes=maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&noindex=1'


driver.get(url)  
innerHTML = driver.execute_script("return document.body.innerHTML")
sleep(3)
root=BeautifulSoup(innerHTML,"lxml") #parse HTML using beautifulsoup
viewcount=root.find_element_by_class_name("paginations")   #find the value which you need.
print(viewcount)
# test = html.find_element_by_class_name('pagination')

# print(test)
# soup=BeautifulSoup(html.page_source)
# print(soup.span)