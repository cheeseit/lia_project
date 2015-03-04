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
img = Image.open("/sne/home/hdermois/Documents/LIA/project/images/image0.bmp")
img.save(imgfile,"BMP")
imagestring = imgfile.getvalue()
b_imagestring = Binary(imagestring)

post = {"test": "testzor",
        "image": b_imagestring}
posts = db.posts

#post_id = posts.insert(post)
mycursor = posts.find()
#print post_id
print mycursor.count()

for i in mycursor:
        retrieve =  StringIO(i["image"])
        image_retrieve = Image.open(retrieve)
        #print i.get("test")

# print b_imagestring
# print imagestring