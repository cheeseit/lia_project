__author__ = 'hdermois'

from os import listdir
from os.path import isfile, join
from os import walk
import re
import matplotlib.pyplot as plt
import numpy as np

path = "/home/harm/resultsold/"
#onlyfiles = [ f for f in listdir("/sne/home/hdermois/results") if isfile(join("/sne/home/hdermois/results",f)) ]

results_2d= []
results_haystack = []

directories= next(walk(path))[1]

files = {}

for d in directories:
    files[d] = [ f for f in listdir("%s%s" % (path,d) ) if isfile(join("%s%s" % (path,d),f)) ]


results_2d= [0,0,0]
results_haystack = [0,0,0]
counter_2d = [0,0,0]
counter_haystack = [0,0,0]


print files
for k in files.keys():
    for f in files[k]:
        file = open("%s%s/%s"%(path,k,f))
        all_lines = []
        for l in file.readlines()[1:]:
            l_split = l.split(",")
            nr_nodes = int(l_split[3])
            if l_split[2] > 3 and not re.search("haystack",k):
                if 1 <= nr_nodes < 5:
                    results_2d[0] +=  + int(l_split[2])
                    counter_2d[0] += 1
                elif 5 <= nr_nodes < 20:
                    results_2d[1] = results_2d[1] + int(l_split[2])
                    counter_2d[1] += 1
                else:
                    results_2d[2] = results_2d[2] + int(l_split[2])
                    counter_2d[2] += 1
            elif l_split[2] > 3:
                if 1 <= nr_nodes < 5:
                    results_haystack[0] =  results_haystack[0] + float(l_split[2])
                    counter_haystack[0] += 1
                elif 5 <= nr_nodes < 20:
                    results_haystack[1] = results_haystack[1] + float(l_split[2])
                    counter_haystack[1] += 1
                else:
                    results_haystack[2] = results_haystack[2] + float(l_split[2])
                    counter_haystack[2] += 1



for i,r in enumerate(results_2d):
    results_2d[i] = r/counter_2d[i]
for i,r in enumerate(results_haystack):
    results_haystack[i] = r / counter_haystack[i]

print results_2d
print results_haystack
N=3
fig = plt.figure()
ax = fig.add_subplot(111)
ind = np.arange(N)                # the x locations for the groups
width = 0.4                      # the width of the bars

font_size = 16

ax.set_ylim(0,2000)
ax.set_title('Index response time per density', fontsize=22)
ax.set_ylabel('Repsonse time(ms)', fontsize=font_size)

xTickMarks = ['Density '+str(i) for i in [1,5,20]]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=font_size)

rects1 = ax.bar(ind, results_haystack, width,color='blue')
rects2 = ax.bar(ind+width, results_2d, width,color='red')
ax.legend( (rects1[0], rects2[0]), ('Haystack', '2d Sphere') )
plt.show()