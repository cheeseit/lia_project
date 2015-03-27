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
import multiprocessing
import pickle

def generating(offset,points,i):
    ran.seed(987654)
    ran.jumpahead(offset)
    tmp_allpoints = []
    global all_points
    for p in points:
        temp = ran.randint(0,99)
        tmp_point = {}
        tmp_point["c_point"] = p
        tmp_allpoints.append(p) 
        if temp >= 80:
            tmp_allpoints = tmp_allpoints + gg.points_in_radius(19, p, 50)
        elif temp >= 50:
            tmp_allpoints = tmp_allpoints + gg.points_in_radius(4, p, 50)
        else:
            continue
    pickle.dump(tmp_allpoints, open("./output/process%d_points"%(i),"wb"))

def inserting_db(points,collection):
    collection = db_util.create_collection(database_name, collection_name)
    for i, p in enumerate(points):
        #temp_img = gi.create_images(1)
        query = u.insert_location(p,"s")
        collection.insert(query)
# import numpy as np
# import matplotlib.pyplot as plt
#
# from pylab import *

#ran.seed(987654)

#number of nodes
# central_points = sys.argv[1]

central_points = 80000
all_points = []


thread_lock = multiprocessing.Lock()
# amsterdam_left_corner = 52.386212, 4.875950
# amsterdam_right_corner = 52.359592, 4.915775

# photo =1 , gridfs =2 ,os_level =3
db_choice = 1
generate_points = 1
nr_threads = 8
threads = []

if generate_points:
    left_corner = 53.270020, 3.136886
    right_corner = 49.494760, 6.432784
    points = gg.create_random_points(central_points,left_corner, right_corner)
    cent_points = []
    collection_name = "gridfs"
    database_name = "photo"
    thread_points = central_points/nr_threads
    print "done generating the central points" 
    for i,t in enumerate(range(nr_threads)):
        thread = multiprocessing.Process(target=generating,args=(i*thread_points, points[i*thread_points:(i+1)*thread_points],i))
        thread.start()
        threads.append(thread)

for t in threads:
    t.join()


collection = db_util.create_collection(database_name, collection_name)
collection.create_index([("pos",GEO2D),("direction", 1)])
collection.create_index([("loc",GEOSPHERE)])
collection.create_index([("pos",GEOHAYSTACK),("direction", 1)], bucketSize=0.00167)

threads = []
for i in range(nr_threads):
    tmp = pickle.load(open("./output/process%d_points"%(i),"rb"))
    #all_points = all_points + tmp
    collection = db_util.create_collection(database_name, collection_name)
    thread = multiprocessing.Process(target=inserting_db,args=(tmp,collection))
    thread.start()
    threads.append(thread)


for t in threads:
    t.join()

##insert image at each point
#
#
#


