__author__ = 'hdermois'

#post = {"loc": {"type" : "Point", "coordinates" :[49.09141221192625, 14.663380323014103] },
        # "image": b_imagestring}

from cStringIO import StringIO
from PIL import Image
from bson import Binary
from pymongo import MongoClient

def insert_location(loc, image=""):
    if image:
        temp = {"loc": {"type" : "Point", "coordinates" : loc}, "image" : image}
    else :
        temp = {"loc": {"type" : "Point", "coordinates" : loc} }
    return temp
# def convert_image_to_binary(image):
#     imgfile = StringIO()
#     img = Image.open(image)
#     img.save(imgfile,"BMP")
#     imagestring = imgfile.getvalue()
#     return Binary(imagestring)


def connect_db(db_name):
    client = MongoClient()
    db = client.db_name
    return db
