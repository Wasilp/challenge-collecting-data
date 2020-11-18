# challenge-collecting-data
Real estate scrapping  script


Website Immovlan house to sale search:

https://immo.vlan.be/fr/immobilier/maison?transactiontypes=a-vendre,en-vente-publique&propertysubtypes=maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&noindex=1

https://immo.vlan.be/fr/immobilier?propertytypes=appartement,maison&transactiontypes=a-vendre,en-vente-publique&propertysubtypes=appartement,rez-de-chaussee,duplex,penthouse,studio,loft,triplex,maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&pageOffset=167&noindex=1

We need to collect all links within the list of each pages.
To do so we will loop on the index (see pageOffset in url) in the second url 
How to know how many page we will loop ? There is a ul at the end of page. Strating from 1 to xxx we need to collect the txt in span and transform in int to loop.
