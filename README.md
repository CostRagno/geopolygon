# geopolygon
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
---
# Summary

Inferring the location of messages, people and events is an increasing branch of
researches nowadays. The wide amount of textual data from blogs, microblogs and 
social media opened to new challenges and, for many application, the location 
information is needed. 
However, obtaining the geographic information directly from the messages or users in study is not easy and in many situation it is needed to estimate it.
Moreover, especially for social media account information, the geographic indication is often not available at fine-grain resolution but only at Country or State level. 
Thus, to estimate a finer location for a given user/text, some computations and data trasformation are needed. 

``geopolygon`` is a Python library able to represent at coordinates level, the original 
geographic information available at city or regional level. The representation is 
performed by deriving the polygon area over the World surface to represent the City/Region 
bounaries. The library have been used in our recent paper (Zola et al., 2019) for Twitter users geolocation to create a synthetic dataset starting from a frequency distribution of cities over the Globe surface.

# The geopolygon Package
The ``geopolygon`` Python package provides two kind of services. It retrieves the polygon of a geographical area from [OpenStreetMap (OPS)](https://www.openstreetmap.org/) and corrects the building sequence of the OPS polygons. To retrieve the polygons OPS polygons ``geopolygon`` needs two informations from OPS: the OPS element and the OPS ID. 

The OPS element identifies a geographical OPS object. It exists three OPS elements: 

1. [nodes](https://wiki.openstreetmap.org/wiki/Node), a node is one of the core elements in the OpenStreetMap data model. It consists of a single point in space defined by its latitude, longitude and node id;
2. [way](https://wiki.openstreetmap.org/wiki/Way), a way is an ordered list of nodes;
3. [relations](https://wiki.openstreetmap.org/wiki/Relation), ordered list of one or more nodes, ways and/or relations.

It follows that a city, for example, is a relation (which contains ways and nodes). A country is again a realtion made of relations. 

The OPS ID is, simply, an unique code which identify each OPS element. 

So, given the name of a geographical area, for example the name of a city, ``geopolygon`` uses the ``geopy`` Python package ([geopy](https://github.com/geopy/geopy)) to get the OPS element and the OPS ID. Then,``geopolygon`` uses this information to retrieve the coordinates of the polygon which circumscribes that spacific area.

Note that ``geopolygon`` retrieves only the polygons of the relations (countries, states and cities). If a given geographical area is not a relation, so for example it is a node (for example in OPS a suburb is a node), then ``geopolygon`` calculate an approximate circumference of the geographical area. To accomplish this task ``geopolygon`` uses the wikidata tag of that area to retrive the area surface A in <a href="https://www.codecogs.com/eqnedit.php?latex=km^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?km^2" title="km^2" /></a>. Then, it estimates the radius r as <a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;\sqrt{{A}/{\pi}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&space;=&space;\sqrt{{A}/{\pi}}" title="r = \sqrt{{A}/{\pi}}" /></a>, obtaining the approximate circumference.

The  OPS polygons usually do not have the correct building sequence, such as exemplified in Figure 1. To solve this issue, we applied the concave hull method proposed by Moreira et al. 2007, which is based on a k-nearest neighbours algorithm. The concave hull improved all inspected problematic polygons, such as exemplified in Figure 1. 

Figure 1:

OPS raw polygon            |  Reshaped polygon 
:-------------------------:|:-------------------------:
![](https://github.com/CostRagno/geopolygon/blob/master/images/new_york_red-1.png)  |  ![](https://github.com/CostRagno/geopolygon/blob/master/images/new_york_green-1.png)

# Example Usage 
The installation of ``geopolygon`` can be done via [Python Package Index (pip)](https://pypi.org/project/geopolygon/), by running the following command:

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
1. ``type_polygon``, which can be "Concave Hull" or "Approximate Circumference";
2. ``raw_data``, which contains the raw polygon as scrapered from OPS;
3. ``processed_data``, which contains the polygon after being processed with the k-nearest neighbours algorithm;
4. ``center``, which contains the center of the polygon;
5. ``location_info``, a ``geopy`` object which contains all the information about the location. 

# References

Zola, P., & Ragno, C., & Cortez, P. (2019, October). Inferring Twitter users home location based on trend topics. In ASA CONFERENCE 2019 Statistics for Health and Well-being BOOK OF SHORT PAPERS.

Moreira, A., & Santos, M. Y. (2007). Concave hull: A k-nearest neighbours approach for the computation of the region occupied by a set of points.
