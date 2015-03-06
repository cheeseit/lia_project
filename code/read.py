__author__ = 'hdermois'

from pymongo import MongoClient
from pymongo import GEOSPHERE
from bson.son import SON

def finding_geolocation_sphere(col, point, distance):

    #temp = { "loc" : { "near" :{ "geometry" : point }, "maxDinstance" : distance } }
    temp = {"loc":{"$geoWithin":{"$centerSphere":[point["coordinates"],distance]}}}
    print temp

    cursor = col.find(temp)
    return cursor

def finding_geolocation_closest(col, point, distance):

    #temp = { "loc" : { "near" :{ "geometry" : point }, "maxDinstance" : distance } }
    temp = {"loc" : {"$near":{"$geometry": point, "$maxDistance": distance}}}
    print temp

    cursor = col.find(temp)
    return cursor


client = MongoClient()
db = client["photo"]
col = db.photos
mycursor = col.find()
first = mycursor[0]["loc"]



found = finding_geolocation_closest(col, first, 100000)

print first["coordinates"]

for i,f in enumerate(found):
    print f["loc"]["coordinates"]
    if i == 100:
        break

found = finding_geolocation_sphere(col, first,0.01)
print first["coordinates"]
for f in found:
    print f["loc"]["coordinates"]