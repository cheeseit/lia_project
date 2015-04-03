__author__ = 'hdermois'

from os import listdir
from os.path import isfile, join
from os import walk
import re
import matplotlib.pyplot as plt
import numpy as np

path = "/home/harm/results/"
#onlyfiles = [ f for f in listdir("/sne/home/hdermois/results") if isfile(join("/sne/home/hdermois/results",f)) ]
directories= next(walk(path))[1]

files = {}


for d in directories:
    files[d] = [ f for f in listdir("%s%s" % (path,d) ) if isfile(join("%s%s" % (path,d),f)) ]

results_haystack = {}
results_2d = {}
counter_haystack={}
counter_2d={}
total_haystack = {}
total_2d = {}
total_ret_2d={}
total_ret_haystack ={}

# first is a summation of all the values 2nd is a counter
for k in files.keys():
    if re.search("haystack",k):
        results_haystack[k] = [0,0]
        counter_haystack[k] = 0
        total_haystack[k] = 0
        total_ret_haystack[k] =0
    else:
        results_2d[k] = [0,0]
        counter_2d[k] = 0
        total_2d[k] = 0
        total_ret_2d[k] = 0


# fill the results


#fill the 2d
for k in files.keys():
    for f in files[k]:
        file = open("%s%s/%s"%(path,k,f))
        for l in file.readlines()[1:]:
            l_split = l.split(",")
            q_time = float(l_split[2])
            # total calculation
            if re.search("haystack",k):
                total_haystack[k] += q_time
                total_ret_haystack[k] += int(l_split[3][:-1])
            else:
                total_2d[k] += q_time
                total_ret_2d[k] += int(l_split[3])

            if q_time > 15 and not re.search("haystack",f):
                results_2d[k][0] += int(l_split[2])
                results_2d[k][1] += 1
            elif not re.search("haystack",f):
                counter_2d[k] += 1
            elif q_time > 15:
                results_haystack[k][0] += float(l_split[2])
                results_haystack[k][1] += 1
            else:
                counter_haystack[k] += 1

print counter_haystack
print counter_2d
print results_haystack
print results_2d
print total_2d
print total_haystack
print "total ret"
print total_ret_2d
print total_ret_haystack

# print files
# for k in files.keys():
#     for f in files[k]:
#         file = open("%s%s/%s"%(path,k,f))
#         all_lines = []
#         for l in file.readlines()[1:]:
#             pass
y_2d=[0,0,0,0]
for k,i in results_2d.iteritems():
    print i
    if k == 'output2dsphere_300k':
        y_2d[0] = i[0]/i[1]
    elif k == 'output2dsphere_500k':
        y_2d[1] = i[0]/i[1]
    elif k == 'output2dsphere_1m':
        y_2d[2] = i[0]/i[1]
    else:
        y_2d[3] = i[0]/i[1]

y_haystack=[0,0,0,0]
for k,i in results_haystack.iteritems():
    if k == 'outputhaystack_300k':
        y_haystack[0] = i[0]/i[1]
    elif k == 'outputhaystack_500k':
        y_haystack[1] = i[0]/i[1]
    elif k == 'outputhaystack_1m':
        y_haystack[2] = i[0]/i[1]
    else:
        y_haystack[3] = i[0]/i[1]

y_total_2d= [0,0,0,0]
for k,i in total_2d.iteritems():
    print i
    if k == 'output2dsphere_300k':
        y_total_2d[0] = i/3000
    elif k == 'output2dsphere_500k':
        y_total_2d[1] = i/3000
    elif k == 'output2dsphere_1m':
        y_total_2d[2] = i/3000
    else:
        y_total_2d[3] = i/3000

y_total_haystack= [0,0,0,0]
for k,i in total_haystack.iteritems():
    if k == 'outputhaystack_300k':
        y_total_haystack[0] = i/3000
    elif k == 'outputhaystack_500k':
        y_total_haystack[1] = i/3000
    elif k == 'outputhaystack_1m':
        y_total_haystack[2] = i/3000
    else:
        y_total_haystack[3] = i/3000

print y_haystack
print y_2d

print y_total_haystack
print y_total_2d


x = [1800,3000,6000,12000]
# plt.plot(x,y_haystack)
#
# #make it nice
# font_size = 16
# plt.xlabel("Number of coordinates in the collection * 10^3",fontsize=font_size)
# plt.ylabel("Query time", fontsize=font_size)
# plt.tick_params(axis="both",labelsize=font_size)
# plt.title("Query time of different sizes haystack collections",fontsize=22)
#
# plt.show()
#
# plt.plot(x,y_2d)
#
# #make it nice
# font_size = 16
# plt.xlabel("Number of coordinates in the collection * 10^3",fontsize=font_size)
# plt.ylabel("Query time", fontsize=font_size)
# plt.tick_params(axis="both",labelsize=font_size)
# plt.title("Query time of different sizes 2d sphere collections",fontsize=22)
#
# plt.show()


blue, = plt.plot(x,y_total_2d, color="blue",label="2d sphere")
red, = plt.plot(x,y_total_haystack,color="red",label="Haystack")

#make it nice
font_size = 16
plt.xlabel("Number of coordinates in the collection * 10^3",fontsize=font_size)
plt.ylabel("Query time", fontsize=font_size)
plt.tick_params(axis="both",labelsize=font_size)
plt.title("Query time of different sizes haystack and 2d sphere",fontsize=22)
plt.legend([blue,red],["2d sphere", "Haystack"],loc=2)
plt.show()


