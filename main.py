from threading import Thread
from utils import LinkThread

url_house = 'https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&hash=82d1fed181cf30aaa8408f90d99003d3&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JLPFV&excludedEstates%5B1%5D=JOS24&excludedEstates%5B2%5D=JQ1LU&excludedEstates%5B3%5D=JQD7F&region=none#gallery'

url_apt = 'https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=1&hash=35a4eea02e536082c87d606f0b71f597&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JLPFV&excludedEstates%5B1%5D=JOS24&excludedEstates%5B2%5D=JQ1LU&excludedEstates%5B3%5D=JQD7F&region=none#gallery' 



thread_1 = LinkThread(url_house)
thread_2 = LinkThread(url_apt)

thread_1.start()
thread_2.start()