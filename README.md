Name

	CHALLENGE-COLLECTING-DATA

Description

CHALLENGE-COLLECTING-DATA is a consolidation team project (3 peoples) that stands for 3 days.
It was asked to us to scrap a Belgium real estate website, collect their different informations about house and appartment selling.
Those informations will be used by 'ImmoEliza' company to make price predictions through a machine learning model.

Informations to collect, if exist:

	Locality
	Type of property (House/apartment)
	Subtype of property (Bungalow, Chalet, Mansion, ...)
	Price
	Type of sale (Exclusion of life sales)
	Number of rooms
	Area
	Fully equipped kitchen (Yes/No)
	Furnished (Yes/No)
	Open fire (Yes/No)
	Terrace (Yes/No)
	If yes: Area
	Garden (Yes/No)
	If yes: Area
	Surface area of the plot of land
	Number of facades
	Swimming pool (Yes/No)
	State of the building (New, to be renovated, ...)

Requirements

	Data for all of Belgium.
	Minimum of 10 000 inputs
	No empty row. If you are missing information, set the value to None.

Installation

To work on this repository or for external use, you can fork or clone it.
	
	Clone it on your computer

	git clone https://github.com/becodeorg/LIE-Thomas-1.26.git


	Did you fork the repository? That works aswell.

	In your terminal, navigate to the clone of your fork, and enter the following command :

	git remote add upstream git@github.com:becodeorg/LIE-Thomas-1.26.git
	
	And to make sure if all went well, use the `git remote -v command`

	Once that's done, every time you want to synchronize your fork with the reference repository, just use the following command:

	git pull upstream master

Packages needed

Here is a list of all packagages we used in this project:

	os
	time
	re
	csv
	requests
	BeautifulSoup ( from bs4) 
	ThreadPoolExecutor (from concurrent.futures)
	Thread (from threading)
	LinkThread,DetailsThread (from utils)
	etree (from lxml)
	pandas as pd
	selenium
	import Thread, RLock (from threading)
	undetected_chromedriver as uc
	UserAgent (from fake_useragent)

Website choosed

	for this project we use: https://www.zimmo.be/fr/

How it works?

	1 - At first, we use a script to collect all the pages of the website that contains all House and Appartment 
		in sale and store them in a csv file (zimmo_details_link.csv)

	2 - After that, we extracte all existing informations listed above for every link in the above csv file

	3 - finally, we store all scraped informations on a csv file also (dataset_house.csv), clean and ordered it.


Contributors

	- https://github.com/Wasilp
	- https://github.com/Nooreyni
	- https://github.com/hajrashidimad

Caoch
	Tom Crasset
	-> https://github.com/tcrasset

Scool

	BeCode.Org, Liege
	-> https://becode.org/

