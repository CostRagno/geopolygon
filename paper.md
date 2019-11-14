# geopolygon: retrieve and correctly reshape the polygon of a geographical area

---
title: 'geopolygon: retrieve and correctly reshape the polygon of a geographical area'
tags:
  - Python
  - geoparsing
  - city polygons
  - concave hull
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
Authors:
  + Costantino Ragno, ANIMA Holding S.p.a., Corso Giuseppe Garibaldi, 99 - 20121 Milano, Italy.
  + Paola Zola, IIT-CNR, Via G. Moruzzi 1, 56124 Pisa, Italy.

bibliography: paper.bib
---
# Summary

Inferring the location of messages, people and events is an increasing branch of
researches nowadays. The wide amount of textual data from blogs, microblogs and 
social media opened to new challenges and, for many application, the location 
information is needed (Holsapple et al., 2018). 
However, obtaining the geographic information directly from the messages or users in study is not easy and in many situation it is needed to estimate it.
Moreover, especially for social media account information, the geographic indication is often not available at fine-grain resolution but only at Country or State level (Zola et al., 2019a). 
Thus, to estimate a finer location for a given user/text, some computations and data trasformation are needed. 

``geopolygon`` is a Python library able to represent at coordinates level, the original 
geographic information available at city or regional level. The representation is 
performed by deriving the polygon area over the World surface to represent the City/Region 
bounaries. The library have been used in our recent paper (Zola et al., 2019b) for Twitter users geolocation to create a synthetic dataset starting from a frequency distribution of cities over the Globe surface.

# The geopolygon Package
The ``geopolygon`` Python package provides two services: 

1. it retrieves a set of points enclosed in a geographical area; and
2. given the set of points, it computes the polygon. 

``geopolygon`` retrieves the set of points from [OpenStreetMap (OPS)](https://www.openstreetmap.org/). In order to obtain the data, ``geopolygon`` needs two information: the *OPS ID* and the *OPS element*. 
The *OPS ID* is an unique code able to identify each *OPS element*. 

The *OPS element* is the basic components of OpenStreetMap's conceptual data model of the physical world. It consists of: 

1. [nodes](https://wiki.openstreetmap.org/wiki/Node): a node is one of the core elements in the OpenStreetMap data model. It consists of a single point in space defined by its latitude, longitude and node id;
2. [way](https://wiki.openstreetmap.org/wiki/Way): it is an ordered list of nodes;
3. [relations](https://wiki.openstreetmap.org/wiki/Relation): ordered list of one or more nodes, ways and/or relations itself.

For example, a city is a relation composed by ways and nodes. A Country is a collection of relations and it is defined as a relation too.

Thus, given the name of a geographical area, for example the name of a city; ``geopolygon`` uses the ``geopy`` Python package ([geopy](https://github.com/geopy/geopy)) to get the *OPS element* and the *OPS ID*. Having the *OPS element* and the *OPS ID*, ``geopolygon`` retrieves the coordinates of the polygon for the queried area.

``geopolygon`` has been created in order to obtain the polygons of relations (cities, states and countries). Whenever a node or a way is given as input, ``geopolygon`` computes an approximated circumference of the area. In order to compute the approxmated circumference ``geopolygon`` uses the wikidata tag of the input area to retrive its surface A expressed in $km^2$. Then, it estimates the radius r as $r = \sqrt{{A}/{\pi}}$, obtaining the approximated circumference.

In general, the points got from OPS do not have the correct building sequence as shown in Figure 1 (a) about New York city polygon. To avoid this limitation  and compute the correct polygon that encompasses the set of points, we applied the concave hull method proposed by Moreira et al. 2007. The algorithm proposed by Moreira et al. is based on a k-nearest neighbours algorithm and it generates the correct concave hull such as exemplified in Figure 1 (b) for the city of New York. 

Figure 1:

a: OPS raw polygon            |  b: Reshaped polygon 
:-------------------------:|:-------------------------:
![](https://github.com/CostRagno/geopolygon/blob/master/images/new_york_red-1.png)  |  ![](https://github.com/CostRagno/geopolygon/blob/master/images/new_york_green-1.png)

# Example Usage 
The installation of ``geopolygon`` is available via [Python Package Index (pip)](https://pypi.org/project/geopolygon/), by running the following command:

```pip install geopolygon```

The main function of ``geopolygon`` is ``area_poly``. An example usage of ``area_poly`` is reported in the following code: 

```Python 
import geopolygon as gp
city = "Rome"
city_dict = gp.area_poly(city, concave_hull_reshape = 'yes')

print(city_dict.keys())
Out[1]: dict_keys(['type_polygon', 'raw_data', 'processed_data', 'center', 'location_info'])
```
The output ``city_dict`` is a dictionary which contains:
1. ``type_polygon``: can be "Concave Hull" or "Approximate Circumference";
2. ``raw_data``: contains the raw polygon as scrapered from OPS;
3. ``processed_data``: contains the polygon after being processed with the k-nearest neighbours algorithm;
4. ``center``: contains the center of the polygon;
5. ``location_info``: a ``geopy`` object which contains all the information about the location. 

# References
Holsapple, C. W., Hsiao, S. H., & Pakath, R. (2018). Business social media analytics: Characterization and conceptual framework. Decision Support Systems, 110, 32-45.

Moreira, A., & Santos, M. Y. (2007). Concave hull: A k-nearest neighbours approach for the computation of the region occupied by a set of points.

Zola, P., Cortez, P., & Carpita, M. (2019a). Twitter user geolocation using web country noun searches. Decision Support Systems, 120, 50-59.

Zola, P., & Ragno, C., & Cortez, P. (2019b, October). Inferring Twitter users home location based on trend topics. In ASA CONFERENCE 2019 Statistics for Health and Well-being BOOK OF SHORT PAPERS.


