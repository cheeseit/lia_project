__author__ = 'hdermois'

import generate_geolocations as gg
import random
import insert
import util as u
import generate_images as gi

central_points = 500

amsterdam_left_corner = 52.386212, 4.875950
amsterdam_right_corner = 52.359592, 4.915775


cent_points = gg.create_random_points(central_points,amsterdam_left_corner, amsterdam_right_corner)
for p in cent_points:
    temp = random.randint(0,99)
    if temp > 90:
        cent_points = cent_points + gg.points_in_radius(99, p, 50)
    elif temp > 70:
        cent_points = cent_points + gg.points_in_radius(19, p, 50)
    elif temp > 40:
        cent_points = cent_points + gg.points_in_radius(4, p, 50)
    else :
        continue


collection = insert.create_database("photo","photos")

# insert image at each point
for p in cent_points:
    temp_img = gi.create_images(1)
    query = u.insert_location(p,temp_img)
    collection.insert(query)
print "hello"