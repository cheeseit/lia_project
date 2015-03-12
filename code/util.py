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


def write_to_output(file,data):
    with open(file, "a") as f:
        for d in data:
            f.write(d)
    f.close

def get_central_points_from_file():
    f = open("./output/points")
    points = []
    for l in f:
        l_split = l.split(",")
        temp_point = [float(l_split[0]),float(l_split[1])]
        points.append(temp_point)
    return points
