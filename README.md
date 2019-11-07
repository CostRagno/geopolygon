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

# References
#---------------------------------------------------------------------------------------

Zola, P., & Ragno, C., & Cortez, P. (2019, October). Inferring Twitter users home location based on trend topics. In ASA CONFERENCE 2019 Statistics for Health and Well-being BOOK OF SHORT PAPERS.
