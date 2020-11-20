from threading import Thread
from utils import LinkThread,DetailsThread


# houseSubTypeStart = 72
# aptSubTypeStart = 10
# house_url = []
# apt_url = []
# for i in range(33):
#      house_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=5&subType%5B0%5D='+str(houseSubTypeStart)+'&hash=eaaefff3761dbc9ada3a877ef9184200&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#      houseSubTypeStart += 1
# for i in range(4):
#     apt_url.append('https://www.zimmo.be/fr/biens/?status=1&type%5B0%5D=1&subType%5B0%5D='+str(aptSubTypeStart)+'&hash=aef0530b2cb50bf0b51f00277f373d22&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&region=none#gallery')
#     aptSubTypeStart += 1
# for url in apt_url:
#     thread_aptSubTypeStart = LinkThread(url)
#     thread_aptSubTypeStart.start()
    # Computer friendly uncomment it if you don't want to see your cpu burn in the flames of thread.
#     thread_aptSubTypeStart.join()
    # told u !

with open("zimmo_details_link.csv", "r") as a_file:
  for num,line in enumerate(a_file):
    stripped_url = line.strip()
    thread_num = DetailsThread(stripped_url)
    thread_num.start()
    # Computer friendly uncomment it if you don't want to see your cpu burn in the flames of thread.
    thread_num.join()