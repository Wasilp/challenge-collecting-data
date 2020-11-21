# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import re
import csv
import requests
from bs4 import BeautifulSoup as bs
import shadow_useragent


# %%
url = "https://www.zimmo.be/fr/couvin-5660/a-vendre/maison/JQLJU/?search=82d1fed181cf30aaa8408f90d99003d3"

#url = "https://www.zimmo.be/fr/langemark-8920/a-vendre/maison/JHWY7/?search=3ae7b1a98206095502d8253991210414&boosted=1"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# %%
requete = requests.get(url, headers=headers)
page = requete.content
soup = bs(page, 'html.parser')


# %%
print(soup.prettify())


# %%
#locality

loc = soup.find("h2", class_="section-title").text
loc = loc.split()
for x in loc:
    if re.match("^[0-9]{4}",x):
        loc = x
        print(loc)


# %%
#function for determine type and subtype of property
def itemType(var):
    var = soup.find('ul', class_="main-features").text
    var = var.split('Type')
    var = var[1]
    var = var.split('\n')
    var = var[1]
    return var


# %%
a = itemType('var')
a.split('(Maison)')


# %%
#subtype of property
equiv2 = itemType('var')   # call the function
#equiv2
if len(equiv2) > 10:
    type_check2 = re.search('Maison', equiv2)

    if type_check2 != 'None':
        subtype = equiv2.split('(Maison)')
        subtype = subtype[0]
        print(subtype)
    else:
        subtype = equiv2.split('(Apartment)')
        subtype = subtype[0]
        print(subtype)
else:
    print('None')
#suitemType('subtype')


# %%
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

    print(price)
    
except IndexError:
    print('None')


# %%
#number of rooms

try:
    rooms = soup.find('ul', class_="main-features").text
    rooms = rooms.split('Chambres')
    rooms = rooms[1]
    rooms = rooms.split('\n')
    rooms = rooms[2]
    rooms = rooms.strip()
    rooms = int(rooms)


    print(rooms)

except ValueError:
    print('None')


# %%
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

    print(surf)

except ValueError:
    print('None')


# %%
#private bathroom

try:
    bathroom = soup.find('ul', class_="main-features").text
    bathroom = bathroom.split('Salles de bain\n\n')
    bathroom = bathroom[1]
    bathroom = bathroom.split('\n')
    bathroom = bathroom[0]
    bathroom = bathroom.strip()
    bathroom = int(bathroom)

    print(bathroom)

except IndexError:
    print('None')


# %%
#State of the building
    #year of build
    
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
    print("None")
else: 
    if int(build_year) >= 2000:
        State_of_the_building = 'New'
        print(State_of_the_building)

    elif int(build_year) < 2000 and int(build_year) > 1980:
        State_of_the_building = 'fairly new'
        print(State_of_the_building)

    elif int(build_year) < 1980:
        State_of_the_building = 'to be renovated'
        print(State_of_the_building)


# %%
#Surface area of the plot of land

if typ_prop == "Maison":
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
      print(Surfac_land)
   except ValueError:
      print('None')
else:
    print('None')


# %%
#Number of facades

if typ_prop == "Maison":
    facades = soup.find('ul', class_="main-features").text
    facades = facades.split('Construction\n\n')
    facades = facades[1]
    facades = facades.split('-')
    facades = facades[0]
    facades = facades.strip()
    facades = int(facades)
    print(facades)
else:
    print('None')


# %%
#garden 'ungiven area'
garden = soup.find('section', class_="section-overige overige").text
garden = garden.split('\n\n\n\n')
garden = garden[1]
garden = garden.split('\n')
garden = garden[0]

#garden
if garden == 'Jardin':
    print('True')
else:
    print('False')


# %%
#Terasse

try:
    terrace = soup.find('div', class_="column-right").text
    terrace = terrace.split('Disposition\n\n\n\n')
    terrace = terrace[1]
    terrace = terrace.split('\n')
    terrace = terrace[0]

    if terrace == 'Terrasse':
        print('Yes')
    else:
        print('No')

except IndexError:
    print('No')


# %%
#furnished
#declare a 'No' value when i != 'Yes'

furn = soup.find('section', class_="section-comfort").text
furn = furn.split('\n')
for i in furn:
    if i == 'Meublé':
        print('Yes')


# %%



