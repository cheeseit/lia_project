__author__ = 'hdermois'

import insert
import generate_geolocations as gg
from pymongo import MongoClient
import gridfs
import generate_images as gi
from PIL import Image

left_corner = 53.270020, 3.136886
right_corner = 49.494760, 6.432784

points = gg.create_random_points(100,left_corner,right_corner)

collection = insert.create_collection("photo","photos")
database = insert.create_database("photo")

fs = gridfs.GridFS(database)
for p in points:
    tmp_image = gi.create_image()
    fs.put(tmp_image)
