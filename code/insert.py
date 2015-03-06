__author__ = 'hdermois'

import util
import generate_geolocations as gg
import generate_images as gi
import util as u
from pymongo import MongoClient
from pymongo import GEOSPHERE

nr_images = 1500
nr_points = 1500

locations = gg.get_locations(nr_images)
images = gi.create_images(nr_points)

client = MongoClient()
db = client["photo"]
col = db.photos
col.create_index([("loc", GEOSPHERE)])
col.ensure_index([("loc", GEOSPHERE)])

for i,l in enumerate(locations):
    temp = u.create_insert_statement(l, images[i])
    col.insert(temp)

