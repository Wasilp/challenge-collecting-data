# Utils function for crapy scraping 
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import requests
import selenium
import csv
import re
import os
import time
from bs4 import BeautifulSoup as bs
import shadow_useragent
from threading import Thread, RLock
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
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

     def run(self):

            driver = uc.Chrome()
            driver.get(self.url)
            driver.implicitly_wait(3)
            driver.find_element_by_id("didomi-notice-agree-button").click()
            driver.implicitly_wait(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.implicitly_wait(3)
            
            #locality
            #datass = []
            try:
                loc = soup.find("h2", class_="section-title").text
                loc = loc.split()
                for x in loc:
                    if re.match("^[0-9]{4}",x):
                        loc = x
                        #print(loc)
            except AttributeError:
                loc = 'None'
                        


            #function for determine type and subtype of property
            def itemType(var):
                var = soup.find('ul', class_="main-features").text
                var = var.split('Type')
                var = var[1]
                var = var.split('\n')
                var = var[1]
                return var


            #Type of property
            try:
                equiv = itemType('var')   # call the function

                type_check = re.search('Maison', equiv)

                if type_check != 'None':
                    prop_type = 'House'
                    #print(prop_type)
                else:
                    prop_type = 'Apartment'
                    #print(prop_type)
            except AttributeError :
                prop_type = 'None'



            #subtype of property
            
            try:
                equiv2 = itemType('var')   # call the function
                if len(equiv2) > 10: #to filter if equiv2 return one word, then we don't have the subtype
                    type_check2 = re.search('Maison', equiv2)

                    if type_check2 != 'None':
                        subtype = equiv2.split('(Maison)')
                        subtype = subtype[0]
                        #print(subtype)
                    else:
                        subtype = equiv2.split('(Apartment)')
                        subtype = subtype[0]
                        #print(subtype)
                else:
                    subtype = 'None'
                    #print(subtype)
                    
            except AttributeError:
                subtype = 'None'
            

            #determining the price

            try:
                price = soup.find('span', class_="feature-value").text
                price = price.split("\n")
                price = price[4]
                price = price.strip()
                price = price.split(" ")
                price = price[1]
                price = price.replace('.', '')
                price = int(price)

                #print(price)
                
            except (AttributeError, IndexError):
                price = 'None'
                #print(price)


            #number of rooms

            try:
                rooms = soup.find('ul', class_="main-features").text
                rooms = rooms.split('Chambres')
                rooms = rooms[1]
                rooms = rooms.split('\n')
                rooms = rooms[2]
                rooms = rooms.strip()
                rooms = int(rooms)


                #print(rooms)

            except (AttributeError, ValueError):
                rooms = 'None'
                #print(rooms)


            #Area

            try:
                surf = soup.find('ul', class_="main-features").text
                surf = surf.split('Surf. habitable\n\n')
                surf = surf[1]
                surf = surf.split('\n')
                surf = surf[0]
                surf = surf.strip()
                surf = surf.split(' ')
                surf = surf[0]
                surf = int(surf)

                #print(surf)

            except (AttributeError, ValueError):
                surf = 'None'
                #print(surf)


            #private bathroom

            try:
                bathroom = soup.find('ul', class_="main-features").text
                bathroom = bathroom.split('Salles de bain\n\n')
                bathroom = bathroom[1]
                bathroom = bathroom.split('\n')
                bathroom = bathroom[0]
                bathroom = bathroom.strip()
                bathroom = int(bathroom)

                #print(bathroom)

            except (AttributeError, IndexError):
                bathroom = 'None'
                #print(bathroom)


            #State of the building
                #year of build
            
            try:    
                build_year = soup.find('ul', class_="main-features").text
                build_year = build_year.split('Construit en\n\n')
                build_year = build_year[1]
                build_year = build_year.split('\n')
                build_year = build_year[0]
                build_year = build_year.split('»')
                build_year = build_year[0]
                build_year = build_year.strip()

                #build_year

                if build_year == 'sur demande':
                    State_of_the_building = 'None'
                    #print(State_of_the_building)
                else: #intervals are choosen arbitrarily because only the year is avalaible on the website
                    if int(build_year) >= 2000:
                        State_of_the_building = 'New'
                        #print(State_of_the_building)

                    elif int(build_year) < 2000 and int(build_year) > 1980:
                        State_of_the_building = 'fairly new'
                        #print(State_of_the_building)

                    elif int(build_year) < 1980:
                        State_of_the_building = 'to be renovated'
                        #print(State_of_the_building)
                        
            except (AttributeError, IndexError):
                State_of_the_building = 'None'

            #Surface area of the plot of land

            if prop_type == "Maison":
                try:
                    Surfac_land = soup.find('ul', class_="main-features").text
                    Surfac_land = Surfac_land.split('Sup. du terrain\n\n')
                    Surfac_land = Surfac_land[1]
                    Surfac_land = Surfac_land.split('\n')
                    Surfac_land = Surfac_land[0]
                    Surfac_land = Surfac_land.strip()
                    Surfac_land = Surfac_land.split(' ')
                    Surfac_land = Surfac_land[0]
                    Surfac_land = int(Surfac_land)
                    #print(Surfac_land)
                except ValueError:
                    Surfac_land = 'None'
                    #print(Surfac_land)
            else:
                Surfac_land = 'None'
                #print(Surfac_land)


            #Number of facades

            if prop_type == "Maison":
                facades = soup.find('ul', class_="main-features").text
                facades = facades.split('Construction\n\n')
                facades = facades[1]
                facades = facades.split('-')
                facades = facades[0]
                facades = facades.strip()
                facades = int(facades)
                #print(facades)
            else:
                facades = 'None'
                #print(facades)


            #garden 'ungiven area'
                
            try:
                gard = soup.find('section', class_="section-overige overige").text
                gard = gard.split('\n\n\n\n')
                gard = gard[1]
                gard = gard.split('\n')
                gard = gard[0]

                #garden
                if gard == 'Jardin':
                    garden = 'True'
                    #print(garden)
                else:
                    garden = 'True'
                    #print(garden)
            except (AttributeError, IndexError):
                garden = 'None'

            #Terasse

            try:
                terrace = soup.find('div', class_="column-right").text
                type_check3 = re.search('Terrasse', terrace)
                if type_check3 != 'None':
                    terrasse = terrace.split('Disposition\n\n\n\n')
                    terrasse = terrace[1]
                    terrasse = terrace.split('\n')
                    terrasse = terrasse[0]

                    if terrasse == 'Terrasse':
                        terrace = 'Yes'
                        #print(terrace)
                    else:
                        terrace = 'No'
                        #print(terrace)
                else:
                    terrace = 'No'
                    #print(terrace)

            except (AttributeError, IndexError):
                terrace = 'No'
                #print(terrace)


            #furnished
            #declare a 'No' value as Default value for when i != 'Yes'
            Furnished = ''
            try:
                furn = soup.find('section', class_="section-comfort").text
                furn = furn.split('\n')
                for i in furn:
                    if i == 'Meublé':
                        Furnished = 'Yes'
                        #Furnished
                        
            except (AttributeError, IndexError):
                Furnished = 'No'
                    
            Type_sale = 'None'
            kitchen = 'None'
            Open_fire = 'None'
            swim_pool = 'None'
        # datass = []
        # for url in url_list:
        #   temp = scrape_page(url)
        #   #datass.append(temp)      
            driver.implicitly_wait(3) 
            csv_file = open('list_of_datas.csv', 'a')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([loc, prop_type, subtype, price, Type_sale, rooms, surf, kitchen, Furnished, Open_fire,  terrace, 
                                garden, bathroom, Surfac_land, facades, swim_pool, State_of_the_building])
            driver.implicitly_wait(200)
            csv_file.close()
            driver.close()