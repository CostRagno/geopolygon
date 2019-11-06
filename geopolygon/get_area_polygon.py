# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:56:40 2019

@author: Costantino_Ragno
"""

from geopy.geocoders import Nominatim
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ConcaveHull
from  wikidata.client import Client
import ast
from obspy.geodetics.base import kilometer2degrees

def circumference_point(r, center):
    t= np.arange(0,2*np.pi,.01)
    x = center[0] + r*np.sin(t);
    y= center[1] + r*np.cos(t);
    circumference = np.transpose(np.vstack([x,y]))
    return circumference

def get_location_data(city):
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout = 120)   
    location = geolocator.geocode(city)
    center = [float(location.raw['lat']),float(location.raw['lon'])]
    return location, center


def get_type_hull(location):
    if location.raw['osm_type'] == 'relation':
       type_hull = 'Concave Hull'
    else:
       type_hull = 'Approximate Circumference'
    return type_hull

def get_routes_links(location):
    osm_id = location.raw['osm_id']
    url = "https://www.openstreetmap.org/relation/" + str(osm_id)
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    routes = soup.findAll('li', {'class': 'way'})
    routes_links = ["https://www.openstreetmap.org/api/0.6" + routes[i].find('a').get('href') + "/full" for i in range(len(routes))]
    return routes_links

def get_routes_data(routes_links):
    Routes_data = {}
    for i in range(len(routes_links)):
        route_id = routes_links[i].split('/')[-2]
        page_temp = urlopen(routes_links[i]).read()
        soup_temp = BeautifulSoup(page_temp, 'html.parser')
        xml_node_list = soup_temp.find_all('node')
        
        nodes_data = {}
        for node_j in xml_node_list:
            node_id = node_j['id']
            nodes_data[node_id] = {'latitude': float(node_j['lat']), 'longitude': float(node_j['lon'])}
        Routes_data[route_id] = nodes_data 
    return Routes_data

def get_long_lat(Routes_data):
    long_lat = []
    for i in range(len(Routes_data)):
        temp_route = Routes_data[list(Routes_data.keys())[i]]
        long_lat_temp = []
        for j in range(len(temp_route)):
            lat_temp = temp_route[list(temp_route.keys())[j]]['latitude']
            long_temp = temp_route[list(temp_route.keys())[j]]['longitude']        
            long_lat_temp.append([lat_temp,long_temp])
        long_lat += long_lat_temp  
    return np.array(long_lat)
   
def get_concave_hull_poly(type_hull, location, concave_hull_reshape, center):

    routes_links = get_routes_links(location)

    Routes_data = get_routes_data(routes_links)

    long_lat = get_long_lat(Routes_data)
    
    if concave_hull_reshape == 'yes':    
        hull_poly = ConcaveHull.concaveHull(np.array(long_lat), 5)
        hull_poly_arr = np.array(hull_poly)
        polygon_data = {'type_polygon':type_hull, 'raw_data':long_lat, 'processed_data': hull_poly_arr, 'center': center, 'location_info': location}
    else:                
        polygon_data = {'type_polygon':type_hull, 'raw_data':long_lat, 'center': center, 'location_info': location}

    return polygon_data 

def get_wikidata_code(location): 
    osm_id = location.raw['osm_id']
    url = "https://www.openstreetmap.org/"+location.raw['osm_type']+"/" + str(osm_id)
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    td_list = soup.findAll('td', {'class': 'browse-tag-v'})
    for i in range(len(td_list)):
        if 'Wikidata' in str(soup.findAll('td', {'class': 'browse-tag-v'})[i]):
            break
    wikidata_code = td_list[i].text    
    return wikidata_code

def get_city_area(wikidata_code):
    client = Client()
    try:
        entity = client.get(wikidata_code, load=True)
        image_prop = client.get('P2046')
        entity[image_prop]
    except Exception as e:
        string_dict = str(e)[32:]
        dict_final = ast.literal_eval(string_dict)
    value = dict_final['value']['amount']
    values = ''
    for i in range(len(value)):
        if (value[i].isdigit() == True) or value[i] == '.':
           values += value[i]
        else:
            continue
    Area = float(values)
    return Area
     
def get_approximate_circumference(type_hull, location, center):

    wikidata_code = get_wikidata_code(location)
    
    Area = get_city_area(wikidata_code)
    raggio = kilometer2degrees(np.sqrt(Area/np.pi))

    hull_poly_arr = circumference_point(raggio, center)
    
    polygon_data = {'type_polygon':type_hull, 'appoximate_circumference': hull_poly_arr, 'center': center, 'location_info': location}
    return polygon_data

def area_poly(city, concave_hull_reshape = 'yes'):    
    try: 
        location, center = get_location_data(city)
    except AttributeError:
        polygon_data = city + ' is not a valid Area.'    
        return polygon_data
    type_hull = get_type_hull(location)
    
    try:
        if type_hull == 'Concave Hull':
           polygon_data = get_concave_hull_poly(type_hull, location, concave_hull_reshape, center)
        else:           
           polygon_data = get_approximate_circumference(type_hull, location, center)
        return polygon_data
    except SyntaxError:
        polygon_data = city + ' is not a valid Area.'    
        return polygon_data