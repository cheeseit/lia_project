__author__ = 'hdermois'

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import generate_geolocations as gg


f = open('/sne/home/hdermois/allpoints','r')
points = []
for l in f.readlines():
    l_split = l.split(",")
    points.append([float(l_split[0][1:]),float(l_split[1][:-1])])




# for i in locs:
#     f.write(str(i)+"\n")
# f.close()
# # plt.scatter(x,y)
# # plt.show()

x = []
for i,l in enumerate(points) :
    x.append(l[0])

y = []
for i,l in enumerate(points):
    y.append(l[1])

figure()
hist2d(y,x,bins=100)
colorbar()
show()