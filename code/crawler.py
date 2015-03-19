__author__ = 'hdermois'

import urllib2

url= "https://www.google.nl/search?q=cats"
usock = urllib2.urlopen(url)

data = usock.read()
usock.close()
print data