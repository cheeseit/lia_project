__author__ = 'hdermois'

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import generate_geolocations as gg


locs = gg.get_locations(100000)

x = []
for i,l in enumerate(locs) :
    x.append(l[0])

y = []
for i,l in enumerate(locs):
    y.append(l[1])

f = open('/sne/home/hdermois/locations','w')
for i in locs:
    f.write(str(i)+"\n")
f.close()
# plt.scatter(x,y)
# plt.show()
figure()
hist2d(x,y,bins=100)
colorbar()
show()