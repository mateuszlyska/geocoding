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

import urllib2, json
import Tkinter as tk
import tkMessageBox

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

    #Defining longitude
    def longitude(self):
		lon = str(self.coords()[1])
		return lon


class GeocodingWindow:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.cityLabel = tk.Label(frame, text = "Cities:", bg = "white", fg = "green")
        self.cityLabel.grid(row=0, sticky=tk.E)

       	self.cityEntry = tk.Entry(frame)
        self.cityEntry.grid(row=0, column=1)

        self.butStart = tk.Button(frame, text = "Find coordinates", fg = "red", command = self.messageCoord)
        self.butStart.grid(columnspan=2)

    def enterText(self):
		self.entTxt = str(self.cityEntry.get())
		return self.entTxt

    def user_input(self):
		user_input = self.enterText()

		if "," in user_input:
			cities = user_input.split(",")
			for city in cities:
				city = city.strip()
				coord = Miasto(city)
				lat = coord.latitude()
				lon = coord.longitude()
				return city + ": " + lat + ", " + lon

		#Maybe without if
		else:
			coord = Miasto(user_input)
			lat = coord.latitude()
			lon = coord.longitude()
			return user_input + ": " + lat + ", " + lon


    def messageCoord(self):
        x = self.user_input()
        tkMessageBox.showinfo("Coordinates", x)


def main():
	try:
		root = tk.Tk()
		window = GeocodingWindow(root)
		root.mainloop()
	except IndexError:
		print "There was an error"
	except urllib2.HTTPError:
		print "There was a problem with connection. Please try again."


if __name__ == "__main__":
	main()