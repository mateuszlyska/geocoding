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

import googlemaps, json

class Miasto(object):
    api_key = "AIzaSyA8DcJMGtAOCb0j7IoM3yk5acZ7c-27NjQ"

    def __init__(self, name):
        self.name = name

    def coords(self):
        map_access = googlemaps.Client(Miasto.api_key)
        coords = map_access.geocode(self.name)
        return coords

chicago = Miasto("Chicago")
print chicago.coords()