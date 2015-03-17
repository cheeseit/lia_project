__author__ = 'hdermois'

import util
import db_util
import read
import time
import gridfs



points = util.get_central_points_from_file()
nr_queries = 200
radius = 50
times = 1
collection = db_util.create_collection("photo","photos")
database = db_util.create_database("photo")
fs = gridfs.GridFS(database)

write=[]
s = "point,execution time, returned, keys examined, success,total docs,querywalltime,imagewalltime\n"
write.append(s)
points = collection.find()

temp = ""
for t in range(times):
    for i,p in enumerate(points):
        #the time for the queries
        start_queries=time.time()
        output = read.finding_geolocation_sphere_coordinates(collection,p["loc"]["coordinates"],radius)
        stop_queries = time.time()
        explain = output.explain()
        t_q = stop_queries-start_queries
        #timing the retrieval of the images.
        start_image = time.time()
        for c in output:
            fs.get(c["image"])
        end_image = time.time()
        t_i = end_image-start_image
        # print output.explain()
        exe_stats = explain["executionStats"]
        # print exe_stats.keys()
        # print "%d,%d,%d,%d,%d\n" % (exe_stats["executionTimeMillis"], exe_stats["nReturned"], exe_stats["totalKeysExamined"], exe_stats["executionSuccess"], exe_stats["totalDocsExamined"])
        s = "%s,%d,%d,%d,%d,%d,%d,%d\n" % (p,exe_stats["executionTimeMillis"], exe_stats["nReturned"], exe_stats["totalKeysExamined"], exe_stats["executionSuccess"], exe_stats["totalDocsExamined"],t_q ,t_i)
        write.append(s)

    util.write_to_output("./output/result1", write)


    # util.restart_and_free_mongodb()
    #time.sleep(10)