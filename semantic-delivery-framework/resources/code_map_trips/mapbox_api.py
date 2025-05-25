"""
Use MapBox API for getting durations of a trip


For mapping adress string to coordinates
(this is called 'geocoding'):

https://docs.mapbox.com/help/how-mapbox-works/geocoding/

"""

import json
import requests


# Mr. Beppo Mappo's API_KEY:
API_ACCESS_TOKEN = "pk.eyJ1IjoiYmVwcG9tYXBwbyIsImEiOiJjazV0ZThwdnUwNG9lM21vemdra2tyaHRjIn0.OovNDeYTSbiwgi0OiM_mQA"

BASE_API_STR = "https://api.mapbox.com/directions/v5/mapbox/"

# this was the original str, used for testing:
# https://api.mapbox.com/directions/v5/mapbox/cycling/-84.518641,39.134270;-84.512023,39.102779?geometries=geojson&access_token=


def build_request(from_coord, to_coord, ride='cycling',
                  base_api_str=BASE_API_STR, access_token=API_ACCESS_TOKEN):
    """
    
    Parameters
    ----------
    from_coord : tuple of float
        (longitude, latidue)
    
    to_coord : tuple of float
    
    ride : str
        either : 'cycling' or 'driving'
    
    base_api_str : str
    
    access_token : str
    
    Returns
    -------
    req_str : str
        the full url for getting directions    
    """
    req_str = base_api_str + ride + '/' + \
              "{},".format(from_coord[0]) + "{}".format(from_coord[1]) + ';' + \
              "{},".format(to_coord[0]) + "{}".format(to_coord[1]) + \
              '?geometries=geojson&access_token=' + access_token

    return req_str


def get_directions(from_coord, to_coord, ride='cycling'):
    """
    
    Parameters
    ----------
    from_coord : tuple of float
        (longitude, latitude)
    
    to_coord : tuple of float
        (longitude, latitude)
    
    ride : str
        either : 'cycling' or 'driving'
        
    Returns
    -------
    response_dict : dict
        dictionary with response, containing duration
        and waypoints, etc.    
    """
    req_str = build_request(from_coord, to_coord, ride)
    
    response_directions = requests.get(req_str)
    
    response_dict = json.loads(response_directions.content)
    
    return response_dict


# limit search to this area of locations:
# minLon, minLat, maxLon, maxLat 
BBOX_LONDON = (-0.25, 51.47, -0.05, 51.54)

# https://docs.mapbox.com/search-playground/#{%22url%22:%22%22,%22index%22:%22mapbox.places%22,%22approx%22:true,%22staging%22:false,%22onCountry%22:true,%22onType%22:true,%22onProximity%22:true,%22onBBOX%22:true,%22onLimit%22:true,%22onLanguage%22:true,%22countries%22:[{%22name%22:%22United%20Kingdom%22,%22code%22:%22gb%22}],%22proximity%22:%22%22,%22typeToggle%22:{%22country%22:true,%22region%22:true,%22district%22:false,%22postcode%22:false,%22locality%22:false,%22place%22:false,%22neighborhood%22:false,%22address%22:false,%22poi%22:false},%22types%22:[%22country%22,%22region%22],%22bbox%22:%22-0.25,%2051.47,%20-0.05,%2051.54%22,%22limit%22:%22%22,%22autocomplete%22:true,%22languages%22:[],%22languageStrict%22:false,%22onDebug%22:false,%22selectedLayer%22:%22%22,%22debugClick%22:{},%22localsearch%22:false,%22query%22:%22-0.10500652525377063,51.4976429189048%22}

PROX_CENTER_LONDON = (-0.13636825220692117, 51.49662605760645)
# (-0.139107, 51.496992)



def get_coordinates_from_address(address_str, country='GB',
                                 bbox=BBOX_LONDON, proximity_center=PROX_CENTER_LONDON,
                                 access_token=API_ACCESS_TOKEN):
    """
    
    Parameters
    ----------
    
    
    Returns
    -------
    
    
    """
    req_str = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + \
              "{}".format(address_str) + \
              ".json?" +  \
              "bbox=" + "{0}, {1}, {2}, {3}".format(*bbox) + \
              "&proximity=" + "{0}, {1}".format(*proximity_center) + \
              "&country=" + country + \
              "&access_token=" + access_token
    
    
    response_geocode = requests.get(req_str)
    
    return json.loads(response_geocode.content)
    
    
