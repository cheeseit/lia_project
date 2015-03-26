__author__ = 'hdermois'

__author__ = 'hdermois'


import random as ran
import db_util
import util as u
import generate_images as gi
import sys
import generate_geolocations as gg
import os
import gridfs
from pymongo import GEOSPHERE
from pymongo import GEOHAYSTACK
from pymongo import GEO2D
from bson import Binary

from PIL import ImageDraw, Image

from cStringIO import StringIO

from os import listdir
from os.path import isfile, join
from os import walk
import re
import matplotlib.pyplot as plt
import numpy as np

directory= "/sne/home/hdermois/Documents/LIA/project/real_images"
onlyfiles = [ f for f in listdir(directory) if isfile(join(directory,f)) ]

print onlyfiles

# import numpy as np
# import matplotlib.pyplot as plt
#
# from pylab import *

ran.seed(987654)

#number of nodes
# central_points = sys.argv[1]

central_points = 15

# amsterdam_left_corner = 52.386212, 4.875950
# amsterdam_right_corner = 52.359592, 4.915775

# photo =1 , gridfs =2 ,os_level =3
db_choice = 1
generate_points = 1
if generate_points:
    left_corner = 53.270020, 3.136886
    right_corner = 49.494760, 6.432784
    points = gg.create_random_points(central_points,left_corner, right_corner)
    cent_points = []
    collection_name = "real"
    database_name = "photo"
    #Calculate densities for these points.
    for i,p in enumerate(points):
        temp = ran.randint(0,99)
        tmp_point = {}
        tmp_point["c_point"] = p
        if temp >= 80:
            points = points + gg.points_in_radius(19, p, 50)
            tmp_point["density"] = "high"
        elif temp >= 50:
            points = points + gg.points_in_radius(4, p, 50)
            tmp_point["density"] = "medium"
        else:
            tmp_point["density"] = "low"
        cent_points.append(tmp_point)

collection = db_util.create_collection(database_name, collection_name)
collection.create_index([("pos",GEO2D),("direction", 1)])
collection.create_index([("loc",GEOSPHERE)])
collection.create_index([("pos",GEOHAYSTACK),("direction", 1)], bucketSize=0.00167)

#insert image at each point

if not os.path.exists("./output"):
    os.makedirs("./output")
f = open("./output/cent_points","w")

for p in cent_points:
    f.write("%s,%s,%s\n" % (p["c_point"][0],p["c_point"][1],p["density"]))
f.close


if db_choice == 1:
    for i, p in enumerate(points):
        print i
        print onlyfiles[i]
        str_img = StringIO()
        tmp_img = Image.open("%s/%s"%(directory, onlyfiles[i]))
        string_split = onlyfiles[i].split(".")

        if string_split[-1] == "png":
            ext = "PNG"
        elif string_split[-1] == "jpg" or string_split[-1] == "jpeg":
            ext = "JPEG"
        tmp_img.save(str_img,ext)
        tmp_image = str_img.getvalue()
        tmp_image = Binary(tmp_image)
        query = u.insert_location(p,tmp_image)
        collection.insert(query)
        f.write("%s\n" % p)
    f.close()
elif db_choice == 2:
    database = db_util.create_database(database_name)
    fs = gridfs.GridFS(database)
    for p in points:
        tmp_image = gi.create_image()
        b = fs.put(tmp_image)
        collection.insert(u.insert_location(p,b))

#elif db_choice == 3:


else:
    print "Nothing inserted"

#TESTSTUFF
# print len(points)
# figure()
# x = []
# y = []
# for p in points:
#     x.append(p[0])
#     y.append(p[1])

# hist2d(x,y,bins=100)
# colorbar()
# show()
# print "Everything is generated."