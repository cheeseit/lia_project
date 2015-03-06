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


def calculate_lat_long (north,south,west,east):
    gStartlat = (north -south)/ 2 + 1 * south
    compas ={}
    south = math.radians(south)
    north = math.radians(north)
    west = math.radians(west)
    east = math.radians(east)

    sinsl = math.sin(south)
    width = east- west

    if (width< 0):
        width = width + 2* math.pi

    gstartlon = deg(normalizeLongitude(west + width/2))
    compas["width"]= width
    compas["south"] = south
    compas["north"] = north
    compas["west"] = west
    compas["east"] =east
    compas["sinsl"] = sinsl
    return  compas


def get_locations(nr_p):
    # England to Turkey
    left_corner = 58.213754, -14.238377
    right_corner= 35.955197, 39.067284
    # Amsterdam
    nr_p_a = 10000
    amsterdam_left_corner = 52.386212, 4.875950
    amsterdam_right_corner = 52.359592, 4.915775

    north = 58.213754
    south = 35.955197

    west = -14.238377
    east = 39.067284
    #number of points
    nr_p_b = 10000
    berlin_left_corner = 41.975381, 12.389471
    berlin_right_corner = 41.836380, 12.600272

    random.seed(123456789)

    compas= calculate_lat_long(north,south,west,east)

    longlat_list = []
    for i in range(nr_p):
        lat = deg(math.asin(random.random()*(math.sin(compas["north"]) - compas["sinsl"]) + compas["sinsl"]))
        lon = deg(normalizeLongitude(compas["west"] + compas["width"]*random.random()))
        longlat_list.append([lat,lon])

    #Points in Amsterdam central
    compas_a= calculate_lat_long(amsterdam_left_corner[0],amsterdam_right_corner[0],amsterdam_left_corner[1],amsterdam_right_corner[1])
    for i in range(nr_p_a):
        lat = deg(math.asin(random.random()*(math.sin(compas_a["north"]) - compas_a["sinsl"]) + compas_a["sinsl"]))
        lon = deg(normalizeLongitude(compas_a["west"] + compas_a["width"]*random.random()))
        longlat_list.append([lat,lon])

    #Points in Berlin
    compas_b= calculate_lat_long(berlin_left_corner[0],berlin_right_corner[0],berlin_left_corner[1],berlin_right_corner[1])
    for i in range(nr_p_b):
        lat = deg(math.asin(random.random()*(math.sin(compas_b["north"]) - compas_b["sinsl"]) + compas_b["sinsl"]))
        lon = deg(normalizeLongitude(compas_b["west"] + compas_b["width"]*random.random()))
        longlat_list.append([lat,lon])

    return longlat_list