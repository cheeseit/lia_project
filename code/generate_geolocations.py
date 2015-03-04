import random
import math
# We want to make geolocation of the Western part of europe.


def deg(rd) :
	return (rd* 180 / math.pi);

def rad(dg):
    return (dg * math.pi /180)

def normalizeLongitude(lon):
    n = math.pi
    if (lon > n):
        lon = lon - 2*n
    elif (lon < -n) :
        lon = lon + 2*n
    return lon

def get_locations():
    left_corner = 58.213754, -14.238377
    right_corner= 35.955197, 39.067284
    north = 58.213754
    south = 35.955197

    west = -14.238377
    east = 39.067284
    #number of points
    nr_p = 100000

    random.seed(123456789)


    gStartlat = (north -south)/ 2 + 1 * south
    south = math.radians(south)
    north = math.radians(north)
    west = math.radians(west)
    east = math.radians(east)

    sinsl = math.sin(south)
    width = east- west

    if (width< 0):
        width = width + 2* math.pi

    gstartlon = deg(normalizeLongitude(west + width/2))

    longlat_list = []

    for i in range(nr_p):
        lat = deg(math.asin(random.random()*(math.sin(north) - sinsl) + sinsl))
        lon = deg(normalizeLongitude(west + width*random.random()))
        longlat_list.append([lat,lon])

    return longlat_list