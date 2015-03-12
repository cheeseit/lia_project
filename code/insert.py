__author__ = 'hdermois'

import util
import generate_geolocations as gg
import generate_images as gi
import util as u
from pymongo import MongoClient
from pymongo import GEOSPHERE
from pymongo import GEO2D
from pymongo import GEOHAYSTACK

# nr_images = 1500
# nr_points = 1500
#
# locations = gg.get_locations(nr_images)
# images = gi.create_images(nr_points)
#
# client = MongoClient()
# db = client["photo"]
# col = db.photos
# col.create_index([("loc", GEOSPHERE)])
# col.ensure_index([("loc", GEOSPHERE)])
#
# for i,l in enumerate(locations):
#     temp = u.insert_location(l, images[i])
#     col.insert(temp)

def create_database(db_name, col_name):
    client = MongoClient()
    db = client[db_name]
    col = db[col_name]
    return col

def insert_into_collection(collection, insert, index=""):
    if not index:
        collection.create_index([("loc"), index])
    # This contains a locations and possibly an image
    for i in insert:
        u.insert_location(i["loc"], i["image"])
