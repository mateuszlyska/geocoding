#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mateusz
#
# Created:     27.05.2017
# Copyright:   (c) Mateusz 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2, json, arcpy

class Miasto(object):
    def __init__(self, name):
        self.name = name

    def webData(self):

        input = self.name
        if " " in input:
			input = input.replace(" ", "+")
        api_key = "AIzaSyA8DcJMGtAOCb0j7IoM3yk5acZ7c-27NjQ"
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (input, api_key)
        data = urllib2.urlopen(url)
        return data

    def coords(self):
		dane = self.webData()
		info = json.load(dane).get("results")[0].get("geometry").get("location")
		lat = info.get("lat")
		lon = info.get("lng")
		return lat, lon

    def latitude(self):
		lat = str(self.coords()[0])
		return lat

    def longitude(self):
		lon = str(self.coords()[1])
		return lon

def user_input():
	user_input = raw_input("What city do you have on mind?")

	if "," in user_input:
		cities = user_input.split(",")
		for city in cities:
			city = city.strip()
			coord = Miasto(city)
			lat = coord.latitude()
			lon = coord.longitude()
			print city + ": " + lat + ", " + lon

	#Maybe without if
	else:
		coord = Miasto(user_input)
		lat = coord.latitude()
		lon = coord.longitude()
		print user_input + ": " + lat + ", " + lon


def main():
    try:
		user_input()
    except IndexError:
		print "There was an error"
    except urllib2.HTTPError:
		print "There was a problem with connection. Please try again."
    finally:
		raw_input("Goodbye")


if __name__ == "__main__":
    main()