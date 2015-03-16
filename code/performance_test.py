__author__ = 'hdermois'

import util
import read
import insert
import sys
import os
from subprocess import call,check_output
import time

# filename = sys.argv[1]


points = util.get_central_points_from_file()
collection = insert.create_database("photo","photos")
write=[]
s = "point,execution time, returned, keys examined, success,total docs\n"
write.append(s)
nr_queries = 10000
radius = 50
times = 10

temp = ""
for t in range(times):
    for i,p in enumerate(points):
        if i == nr_queries:
            break
        output = read.finding_geolocation_sphere_coordinates(collection,p,radius)
        # print output.explain()
        exe_stats = output["executionStats"]
        # print exe_stats.keys()
        # print "%d,%d,%d,%d,%d\n" % (exe_stats["executionTimeMillis"], exe_stats["nReturned"], exe_stats["totalKeysExamined"], exe_stats["executionSuccess"], exe_stats["totalDocsExamined"])
        s = "%s,%d,%d,%d,%d,%d\n" % (p,exe_stats["executionTimeMillis"], exe_stats["nReturned"], exe_stats["totalKeysExamined"], exe_stats["executionSuccess"], exe_stats["totalDocsExamined"])
        write.append(s)

    util.write_to_output("./output/result1", write)


    util.restart_and_free_mongodb()
    time.sleep(10)

# util.write_to_output("./output/%s" % (filename), write)
#stop mongod;sh -c "sync; echo 3 > /proc/sys/vm/drop_caches";start mongod
