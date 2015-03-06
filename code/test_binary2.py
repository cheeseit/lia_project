__author__ = 'hdermois'

from cStringIO import StringIO
from PIL import Image
from bson import Binary
from pymongo import MongoClient


# connect to mongodb
client = MongoClient()
print client.database_names()

db = client.mydb

imgfile = StringIO()
img = Image.open("/sne/home/hdermois/Documents/LIA/project/images/image1.bmp")
img.save(imgfile,"BMP")
imagestring = imgfile.getvalue()
b_imagestring = Binary(imagestring)
#db.posts.createIndex({loc : "2dsphere"})

#post = {"loc": {"type" : "Point", "coordinates" :[49.09141221192625, 14.663380323014103] },"image": b_imagestring}
post = {"loc": {"type" : "Point", "coordinates" :[49.09141221192625, 14.663380323014103] }}
posts = db.posts

#post_id = posts.insert(post)
mycursor = posts.find()
#print post_id


print mycursor.count()

for i in mycursor:
        retrieve =  StringIO(i["image"])
        print i.keys()
        if "loc" in i.keys():
                print i.get("loc")
                img = Image.open(retrieve)
                img.show()
        #print i.get("test")

# print b_imagestring
# print imagestring