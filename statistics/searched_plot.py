__author__ = 'harm'

#for the correlation between the searched files and the size of the collection.
from os import listdir
from os import walk
from os.path import isfile, join
from os import walk
import re
import matplotlib.pyplot as plt
import numpy as np

path = "/home/harm/results/"
#onlyfiles = [ f for f in listdir("/sne/home/hdermois/results") if isfile(join("/sne/home/hdermois/results",f)) ]

results_2d= []
results_haystack = []

directories= next(walk(path))[1]

files = {}

for d in directories:
    files[d] = [ f for f in listdir("%s%s" % (path,d) ) if isfile(join("%s%s" % (path,d),f)) ]

results = {}
for k in files.keys():
    if re.search("haystack",k):
        continue
    results[k] = 0
    for f in files[k]:
        file = open("%s%s/%s"%(path,k,f))
        for l in file.readlines()[1:]:
            l_split = l.split(",")
            results[k] = results[k] + int(l_split[4])

y= []
for k,i in results.iteritems():
    y.append(i/3000)

print results
print y
x = [1.8,3,6,12]
ax = plt.plot(x,y)


#make it nice
font_size = 16

plt.xlabel("Number of coordinates in the collection * 10^6",fontsize=font_size)
plt.ylabel("Number of documents searched", fontsize=font_size)
plt.tick_params(axis="both",labelsize=font_size)
plt.title("Average amount of documents searched per query",fontsize=22)

plt.show()