__author__ = 'hdermois'

from bson import Binary

f = open("/sne/home/hdermois/Documents/LIA/project/images/image0.bmp")
f_b= Binary(f)
print f_b