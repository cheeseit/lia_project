__author__ = 'hdermois'

from random import randint
from PIL import ImageDraw, Image
import util
from cStringIO import StringIO
from bson import Binary

width = 2000
height = 1680

def generate_rectangle_points():
    x1 = randint(1,width)
    y1 = randint(1,height)
    x2 = randint(1,width)
    y2 = randint(1,height)
    return [x1,y1,x2,y2]

def generate_shapes(draw):
    color = ["Blue","Red","Yellow","Lime"]
    for i in range(randint(1,3)):
        draw.rectangle(generate_rectangle_points(), fill=color[randint(0,3)])

def create_images(nr_images):
    images = []
    for i in range(nr_images):
        image_file = StringIO()
        im = Image.new("RGB",(width,height))
        draw = ImageDraw.ImageDraw(im)
        # Dar shapes
        generate_shapes(draw)
        #save image to a stringIOP
        im.save(image_file,"BMP")
        imagestring = image_file.getvalue()
        image = Binary(imagestring)
        images.append(image)
    return images

def create_image():
    image_file = StringIO()
    im = Image.new("RGB",(width,height))
    draw = ImageDraw.ImageDraw(im)
    # Dar shapes
    generate_shapes(draw)
    im.save(image_file,"BMP")
    image_string = image_file.getvalue()
    #save image to a stringIOP
    return image_string

def save_image_to_file(counter):
    im = Image.new("RGB",(width,height))
    draw = ImageDraw.ImageDraw(im)
    # Dar shapes
    generate_shapes(draw)
    im.save("/sne/home/hdermois/Documents/LIA/project/images/image%d.bmp" %(counter), "BMP")

def create_images_other():
    pass

def create_images_storage(nr_images,width,height):
    images = []
    for i in range(nr_images):
        image_file = StringIO()
        im = Image.new("RGB",(width,height))
        draw = ImageDraw.ImageDraw(im)
        # Dar shapes
        generate_shapes(draw)
        #save image to a stringIOP
        im.save(image_file,"BMP")
        imagestring = image_file.getvalue()
        image = Binary(imagestring)
        images.append(image)
    return images