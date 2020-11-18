# challenge-collecting-data
Real estate scrapping  script


Website Immovlan house to sale search:

https://immo.vlan.be/fr/immobilier/maison?transactiontypes=a-vendre,en-vente-publique&propertysubtypes=maison,villa,immeuble-mixte,maison-de-maitre,fermette,bungalow,chalet,chateau&countries=belgique&noindex=1

We need to collect all links within the list of each pages.
To do so we will loop on the index (see noindex=1 in url) in the url 
How to know how many page we will loop ? There is a ul at the end of page. Strating from 1 to xxx we need to collect the txt in span and transform in int to loop.
