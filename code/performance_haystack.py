__author__ = 'hdermois'

import util
import read
import db_util
import sys
import os
from subprocess import call,check_output
import time

# filename = sys.argv[1]


points = util.get_central_points_from_file()
database_name = "photo"
collection_name ="gridfs"
collection = db_util.create_collection(database_name,collection_name)
database = db_util.create_database(database_name)

nr_queries = 10000
distance = 0.00167
times = 1
directory_name = "outputhaystack"

if not os.path.exists("./%s" % directory_name):
    os.makedirs("./%s" % directory_name)


temp = ""
for t in range(times):
    # util.restart_and_free_mongodb()
    # time.sleep(10)
    write=[]
    s = "point,execution time,returned nodes\n"
    write.append(s)
    for i,p in enumerate(points):
        if i == nr_queries:
            break
        output = read.finding_geohaystack(database, collection_name, p, distance)
        stats = output["stats"]
        print stats
        s = "%s,%f,%d\n" % (p,stats["time"],stats["n"])
        write.append(s)

    util.write_to_output("./%s/%s%d" % (directory_name , directory_name, t) , write)



# util.write_to_output("./output/%s" % (filename), write)
#stop mongod;sh -c "sync; echo 3 > /proc/sys/vm/drop_caches";start mongod
