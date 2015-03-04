__author__ = 'hdermois'

from random import randint
from PIL import ImageDraw, Image

width = 1280
height = 720

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
    for i in range(nr_images):
        im = Image.new("RGB",(width,height))
        draw = ImageDraw.ImageDraw(im)
        generate_shapes(draw)
        im.save("/sne/home/hdermois/Documents/LIA/project/images/image%d.bmp" % i, "BMP")




def main():
    nr_images = 10
    create_images(nr_images)

main()