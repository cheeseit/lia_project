__author__ = 'hdermois'

import util
import db_util

collection = db_util.create_database("photo","photos")
# cursor = collection.find()
# for c in cursor:
# collection.update({},{"$set" :{"column4":1}}, multi=True)

cursor1 = collection.find()
for c in cursor1:
    print c.keys()