__author__ = 'hdermois'

from pymongo import MongoClient
from pymongo import GEOSPHERE
from bson.son import SON
import json

def finding_geolocation_sphere(col, point, distance):

    #temp = { "loc" : { "near" :{ "geometry" : point }, "maxDinstance" : distance } }
    # Radius in kilometers.
    temp = {"loc":{"$geoWithin":{"$centerSphere":[point["coordinates"], (distance / 3959.0) * (1/1609.0)]}}}
    cursor = col.find(temp).explain("executionStats")
    return cursor

def finding_geolocation_closest(col, point, distance):

    #temp = { "loc" : { "near" :{ "geometry" : point }, "maxDinstance" : distance } }
    temp = {"loc" : {"$near":{"$geometry": point, "$maxDistance": distance}}}
    cursor = col.find(temp)
    return cursor


def finding_geolocation_sphere_coordinates(col, point, distance):

    #temp = { "loc" : { "near" :{ "geometry" : point }, "maxDinstance" : distance } }
    # Radius in kilometers.
    temp = {"loc":{"$geoWithin":{"$centerSphere":[point, (distance / 3959.0) * (1/1609.0)]}}}
    cursor = col.find(temp)
    return cursor


def finding_geohaystack(db,c_name,point,distance):
    # tmp = {"geoSearch" : c_name ,"search" : {"direction": 1} ,"near": point , "maxDistance" : distance}
    # return db.command(tmp)
    tmp ="db.runCommand( { geoSearch : \"%s\" ,search : { direction: 1 } ,near : %s , maxDistance : 0.00167 , limit : 20} )"% (c_name,point)
    return db.eval(tmp)

def find_all_10mb():
    pass

# client = MongoClient()
# db = client["photo"]
# col = db.photos
# mycursor = col.find()
# first = mycursor[0]["loc"]
# explain = col.find().explain()
# print explain.keys()
# print explain["executionStats"]





# found = finding_geolocation_closest(col, first, 100000)

# print first["coordinates"]
#
# for i,f in enumerate(found):
#     print f["loc"]["coordinates"]
#     if i == 100:
#         break
#
# found = finding_geolocation_sphere(col, first,0.01)
# print first["coordinates"]
# for f in found:
#     print f["loc"]["coordinates"]