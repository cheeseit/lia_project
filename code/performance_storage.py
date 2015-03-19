__author__ = 'hdermois'

__author__ = 'hdermois'

import util
import read
import db_util
import sys
import os
from subprocess import call,check_output
import time
import gridfs
from cStringIO import StringIO
from PIL import Image

# filename = sys.argv[1]

collection_name ="gridfs1"
database_name = "photo"
# photo =1 , gridfs =2 ,os_level =3
db_choice = 3


points = util.get_central_points_from_file()
collection = db_util.create_collection(database_name, collection_name)
database = db_util.create_database(database_name)
fs = gridfs.GridFS(database)


nr_queries = 100
radius = 100
times = 1
directory_name = "outputstorageindb"

if not os.path.exists("./%s" % directory_name):
    os.makedirs("./%s" % directory_name)

s_io=StringIO()


temp = ""

for t in range(times):
    util.restart_and_free_mongodb()
    time.sleep(5)
    write=[]
    s = "point,execution time\n"
    write.append(s)
    if db_choice == 1:
        for i,p in enumerate(points):
            if i == nr_queries:
                break
            start = time.time()
            output = read.finding_geolocation_sphere_coordinates(collection,p,radius)
            end  = time.time()
            s = "%s,%f\n" % (p,(end-start) *1000)
            write.append(s)

    if db_choice == 2:
        for i,p in enumerate(points):
            if i == nr_queries:
                break
            start = time.time()
            output = read.finding_geolocation_sphere_coordinates(collection,p,radius)
            for c in output:
                fs.get(c["image"])
            end  = time.time()
            s = "%s,%f\n" % (p,(end-start) *1000)
            write.append(s)

    if db_choice == 3:
        for i,p in enumerate(points):
            if i == nr_queries:
                break
            start = time.time()
            output = read.finding_geolocation_sphere_coordinates(collection,p,radius)
            for c in output:
                image = Image.open(c["image"])
            end  = time.time()
            s = "%s,%f,%s,%s,%d\n" % (p,(end-start) *1000, c["size"],c["density"],output.count())
            write.append(s)

    util.write_to_output("./%s/%s%d" % (directory_name , directory_name, t) , write)



# util.write_to_output("./output/%s" % (filename), write)
#stop mongod;sh -c "sync; echo 3 > /proc/sys/vm/drop_caches";start mongod
