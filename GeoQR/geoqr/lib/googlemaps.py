"""
Library for accessing and massaging data from
google maps
"""
from httplib2 import Http
from urllib import urlencode

import json

GOOGLE_MAPS_GEOCODE = "http://maps.google.com/maps/api/geocode/json"

def get_entry(address):
    """
    Returns the raw results for a look up based on an address
    """
    h = Http()
    url_params = {
        'address': address,
        'sensor': 'false'
    }    

    url = "%s?%s" % (GOOGLE_MAPS_GEOCODE, urlencode(url_params))
    response, content = h.request(url)
    result = json.loads(content)
    if "status" not in result or result["status"] != "OK":
        return
    return result


def decode_to_latlon(address):
    """
    Takes a string address and attempts to decode it to some meaningful geolocational
    data
    """
    entry = get_entry(address)
    if not entry:
        return None, None
    else:
        def get_coord(l):
            return entry['results'][0]['geometry']['location'][l]
        return get_coord('lat'), get_coord('lng')
