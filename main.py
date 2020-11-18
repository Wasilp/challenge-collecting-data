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
#import shadow_useragent


driver = webdriver.Chrome('/Users/wasilewski/Downloads/chromedriver')
# Same as header read under
# ua = shadow_useragent.ShadowUserAgent()

# my_user_agent = ua.percent(0.05)
url = 'https://immo.vlan.be/fr/immobilier/maison?transactiontypes=a-vendre,en-vente-publique&propertysubtypes=maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&noindex=1'

# I do not need it for now. This header is there in case we need it in requests
# headers = {
#    'User-Agent': '{}'.format(my_user_agent),
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
# }

driver.get(url)
# driver.implicitly_wait(30)
     
sleep(5)
html = driver.execute_script("return document.getElementsByTagName('span')[0].innerHTML")
print(html)
# test = html.find_element_by_class_name('pagination')

# print(test)
# soup=BeautifulSoup(html.page_source)
# print(soup.span)