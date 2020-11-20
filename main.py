from threading import Thread
from utils import LinkThread

url_house = 'https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&hash=82d1fed181cf30aaa8408f90d99003d3&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JLPFV&excludedEstates%5B1%5D=JOS24&excludedEstates%5B2%5D=JQ1LU&excludedEstates%5B3%5D=JQD7F&region=none#gallery'
houseSubTypeStart = 72
aptSubTypeStart = 1
house_url = []
apt_url = []
# for i in range(33):
#     house_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&subType%5B0%5D='+str(houseSubTypeStart)+'&hash=eaaefff3761dbc9ada3a877ef9184200&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#     houseSubTypeStart += 1

# for i in range(10):
#     apt_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=1&subType%5B0%5D='+str(aptSubTypeStart)+'&hash=aef0530b2cb50bf0b51f00277f373d22&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#     aptSubTypeStart += 1

# for url in apt_url:
#     thread_aptSubTypeStart = LinkThread(url)
    # thread_aptSubTypeStart.start()
    # Computer friendly uncomment it if you don't want to see your cpu burn in the flames of thread.
    #thread_houseSubTypeStart.join()
    # told u !
