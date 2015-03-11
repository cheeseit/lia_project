__author__ = 'hdermois'


import random as ran
import insert
import util as u
import generate_images as gi
import sys
import numpy as np
import matplotlib.pyplot as plt
import generate_geolocations as gg
from pylab import *
import os

ran.seed(987654)

#number of nodes
# central_points = sys.argv[1]

central_points = 50000

# amsterdam_left_corner = 52.386212, 4.875950
# amsterdam_right_corner = 52.359592, 4.915775

left_corner = 53.270020, 3.136886
right_corner = 49.494760, 6.432784
points = gg.create_random_points(central_points,left_corner, right_corner)
cent_points = []
#Calculate densities for these points.
for i,p in enumerate(points):
    temp = ran.randint(0,99)
    tmp_point = {}
    tmp_point["c_point"] = p
    if temp >= 90:
        points = points + gg.points_in_radius(99, p, 50)
        tmp_point["density"] = "very high"
    elif temp >= 70:
        points = points + gg.points_in_radius(19, p, 50)
        tmp_point["density"] = "high"
    elif temp >= 40:
        points = points + gg.points_in_radius(4, p, 50)
        tmp_point["density"] = "medium"
    else:
        tmp_point["density"] = "low"
    cent_points.append(tmp_point)


if not os.path.exists("./output"):
    os.makedirs("./output")
f = open("./output/points","w")
for i in cent_points:
    f.write('%f,%f,%s\n' % (i["c_point"][0],i["c_point"][1],i["density"]))

collection = insert.create_database("photo","photos")
# insert image at each point
for p in points:
    temp_img = gi.create_images(1)
    query = u.insert_location(p,temp_img)
    collection.insert(query)


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