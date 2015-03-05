__author__ = 'hdermois'

import generate_geolocations
from geolocation.google_maps import GoogleMaps


locs = generate_geolocations.get_locations()

maps = GoogleMaps(api_key="AIzaSyAurR9wWMsNYu8Sdj0S0FuGm5_oWfj4Wcg")
#maps.search(lat=locs[1][0],lng=locs[1][1])
print locs[0]