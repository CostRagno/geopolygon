#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:12:50 2019

@author: costantino
"""


from distutils.core import setup
    
setup(
  name = 'geopolygon',         # How you named your package folder (MyLib)
  packages = ['geopolygon'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python package to retrieve and correctly reshape the polygon of a geographical area',   # Give a short description about your library
  author = 'Costantino Ragno',                   # Type in your name
  author_email = 'costantino.ragno@unicam.it',      # Type in your E-Mail
  url = 'https://github.com/CostRagno/geopoly',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/CostRagno/geopoly/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['geoinformation', 'polygons', 'CityPolygons', 'openstreetmap', 'concavehull','wikidata'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'geopy',
          'beautifulsoup4',
          'numpy',
          'wikidata',
          'ast',
          'obspy',
          'scipy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
