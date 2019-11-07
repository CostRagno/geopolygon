# geopolygon
---
title: 'geopolygon: retrieve and correctly reshape the polygon of a geographical area'
tags:
  - Python
  - geoparsing
  - city polygons
  - concave hull
  - 
authors:
  - name: Costantino Ragno
    affiliation: 1 
  - name: Paola Zola
    affiliation: 2
affiliations:
 - name: ANIMA Holding S.p.a., Corso Giuseppe Garibaldi, 99 - 20121 Milano.
   index: 1
 - name: IIT-CNR, Via G. Moruzzi 1, 56124 Pisa, Italy.
   index: 2
date: November 2019
bibliography: paper.bib
---
# Summary

Inferring the location of messages, people and events is an increasing branch of
researches nowadays. The wide amount of textual data from blogs, microblogs and 
social media opened to new challenges and, for many application, the location 
information is needed. 
However, obtaining the geographic information directly from the messages or users in study is not easy and in many situation it is needed to estimate it.
Moreover, especially for social media account information, the geographic indication is often not available at fine-grain resolution but only at Country or State level. 
Thus, to estimate a finer location for a given user/text, some computations and data trasformation are needed. 

Geopolygon is a Python library able to represent at coordinates level, the original 
geographic information available at city or regional level. The representation is 
performed by deriving the polygon area over the World surface to represent the City/Region 
bounaries. The library have been used in our recent paper (Zola et al., 2019) for Twitter users geolocation to create a synthetic dataset starting from a frequency distribution of cities over the Globe surface.

# The geopolygon Package
The geopolygon Python package retrive the shape of a geographical area from [OpenStreetMap (OPS)](https://www.openstreetmap.org/). To accomplish this task geopolygon needs two informations: the OPS element and the OPS ID. The OPS element corresponds to the identification of the geographical element. There are three elements: way, nodes and relations. Where, the way connect the nodes and a set of ways and nodes are called relations. Note that a relation can be a set of relations as well. It follows that a city, for example, is a relation (which contains ways and nodes). A country is again a realtion but it contains other relations. The OPS ID is an unique code which identify the element. The geopolygon Package is able to retrive only the polygons of the relations (countries, states and cities). Once the gepgraphical area is idenfied as relation and the OSM ID is obtained, geopolygon is able to scrape the area boundaries obtaining the polygon.
If a given geographical area is not a relation, so for example it is a suburb (considered as a node in OPS), geopolygon calculate an approximate circumference of the geographical area. To accomplish this task geopolygon uses the wikidata tag of that area to retrive the area in $km^{2}$          

In particular what geopolygon works on is the   It uses the package [geopy](https://geopy.readthedocs.io/en/stable/#),a Python 2 and 3 client for several popular geocoding web services (such as Google Maps, Bing Maps, or Nominatim), to get the OPS id of the location.   

geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.
# References
#---------------------------------------------------------------------------------------

Zola, P., & Ragno, C., & Cortez, P. (2019, October). Inferring Twitter users home location based on trend topics. In ASA CONFERENCE 2019 Statistics for Health and Well-being BOOK OF SHORT PAPERS.
