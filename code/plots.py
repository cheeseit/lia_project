__author__ = 'hdermois'

from os import listdir
from os.path import isfile, join
from os import walk
import re
import matplotlib.pyplot as plt
import numpy as np

directory= "/sne/home/hdermois/results/"
onlyfiles = [ f for f in listdir("/sne/home/hdermois/results") if isfile(join("/sne/home/hdermois/results",f)) ]

results_2d= []
results_haystack = []


for i,f in enumerate(onlyfiles):
    tmp = open("%s%s"%(directory,f))
    all_lines = []
    for l in tmp.readlines()[1:]:

        if re.search("haystack",f):
            l_split = l.split(",")
            if l_split > 3:
                tmp_res = {}
                tmp_res["time"] = l_split[2].strip()
                tmp_res["nodes"] = l_split[3].strip()
        else :
            l_split = l.split(",")
            if l_split > 3:
                tmp_res = {}
                tmp_res["time"] = l_split[2].strip()
                tmp_res["nodes"] = l_split[3].strip()
        all_lines.append(tmp_res)
    if re.search("haystack",f):
        results_haystack.append(all_lines)
    else:
        results_2d.append(all_lines)

average_haystack = []
average_2d = []
average_haystack_1= 0
average_haystack_5 = 0
average_haystack_20 = 0

counter_haystack_1 = 0
counter_haystack_5 = 0
counter_haystack_20 = 0

average_2d_1= 0
average_2d_5 = 0
average_2d_20 = 0

counter_2d_1 = 0
counter_2d_5 = 0
counter_2d_20 = 0


for i,entry in enumerate(results_haystack):
    for r in entry:
        if 1 <= int(r["nodes"]) < 5:
            average_haystack_1 += float(r["time"])
            counter_haystack_1 += 1
        if 5 <= int(r["nodes"]) < 20:
            average_haystack_5 += float(r["time"])
            counter_haystack_5 += 1
        if int(r["nodes"]) >= 20:
            average_haystack_20 += float(r["time"])
            counter_haystack_20 += 1

for i,entry in enumerate(results_2d):
    for r in entry:
        if 1 <= int(r["nodes"]) < 5:
            average_2d_1 += float(r["time"])
            counter_2d_1 += 1
        if 5 <= int(r["nodes"]) < 20:
            average_2d_5 += float(r["time"])
            counter_2d_5 += 1
        if int(r["nodes"]) >= 20:
            average_2d_20 += float(r["time"])
            counter_2d_20 += 1
# for i,r in enumerate(results_2d):
# for i,r in enumerate(results_2d):
#     average_2d[i] = average_2d[i]+r["time"]
values_haystack =[]
values_2d = []

values_haystack.append(average_haystack_1/counter_haystack_1)
values_haystack.append(average_haystack_5/counter_haystack_5)
values_haystack.append(average_haystack_20/counter_haystack_20)

values_2d.append(average_2d_1/counter_2d_1)
values_2d.append(average_2d_5/counter_2d_5)
values_2d.append(average_2d_20/counter_2d_20)


N=3
fig = plt.figure()
ax = fig.add_subplot(111)
ind = np.arange(N)                # the x locations for the groups
width = 0.35                      # the width of the bars

ax.set_ylim(0,2000)
ax.set_title('Index response time per density')
ax.set_ylabel('Repsonse time(ms)')

xTickMarks = ['Density '+str(i) for i in [1,5,20]]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

rects1 = ax.bar(ind, values_haystack, width,color='blue')
rects2 = ax.bar(ind+width, values_2d, width,color='red')
ax.legend( (rects1[0], rects2[0]), ('Haystack', '2d Sphere') )
plt.show()