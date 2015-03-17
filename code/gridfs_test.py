__author__ = 'hdermois'

import db_util
import generate_geolocations as gg
from pymongo import MongoClient
import gridfs
import generate_images as gi
from PIL import Image
import util as u
from cStringIO import StringIO


left_corner = 53.270020, 3.136886
right_corner = 49.494760, 6.432784

points = gg.create_random_points(10000,left_corner,right_corner)

collection = db_util.create_collection("photo","photos")
database = db_util.create_database("photo")

fs = gridfs.GridFS(database)
for p in points:
    tmp_image = gi.create_image()
    b = fs.put(tmp_image)
    collection.insert(u.insert_location(p,b))

cursor = collection.find({},{"image":1})

for c in cursor:
    for f in fs.find({"_id":c["image"]}):
        tmp = StringIO(f.read())
        img =Image.open(tmp)
        # print c["image"]
        # tmp = fs.get(c["image"]).explain
        # retrieve =  StringIO(tmp.read())
        # img = Image.open(retrieve)
        img.show()
        break
    break