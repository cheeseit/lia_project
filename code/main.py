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


# import numpy as np
# import matplotlib.pyplot as plt
#
# from pylab import *

ran.seed(987654)

#number of nodes
# central_points = sys.argv[1]

central_points = 2000000

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
    collection_name = "gridfs"
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


if not os.path.exists("./output"):
    os.makedirs("./output")
f = open("./output/cent_points","w")

for p in cent_points:
    f.write("%s,%s,%s\n" % (p["c_point"][0],p["c_point"][1],p["density"]))
f.close

#collection = db_util.create_collection(database_name, collection_name)
#collection.create_index([("pos",GEO2D),("direction", 1)])
#collection.create_index([("loc",GEOSPHERE)])
#collection.create_index([("pos",GEOHAYSTACK),("direction", 1)], bucketSize=0.00167)
#
##insert image at each point
#
#
#
#if db_choice == 1:
#    for i, p in enumerate(points):
#        temp_img = gi.create_images(1)
#        query = u.insert_location(p,temp_img)
#        collection.insert(query)
#        f.write("%s\n" % p)
#    f.close()
#elif db_choice == 2:
#    database = db_util.create_database(database_name)
#    fs = gridfs.GridFS(database)
#    for p in points:
#        tmp_image = gi.create_image()
#        b = fs.put(tmp_image)
#        collection.insert(u.insert_location(p,b))
#
##elif db_choice == 3:
#
#
#else:
#    print "Nothing inserted"

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
