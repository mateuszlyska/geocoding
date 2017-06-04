#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Mateusz
#
# Created:     27.05.2017
# Copyright:   (c) Mateusz 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *
import tkMessageBox
import geocoding2

class GeocodingWindow:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.cityLabel = Label(frame, text = "Cities:", bg = "white", fg = "green")
        self.cityLabel.grid(row=0, sticky=E)

       	self.cityEntry = Entry(frame)
        self.cityEntry.grid(row=0, column=1)

        self.butStart = Button(frame, text = "Find coordinates", fg = "red", command = self.messageCoord)
        self.butStart.grid(columnspan=2)


    def enterText(self):
		self.entTxt = str(self.cityEntry.get())
		return self.entTxt

    def messageCoord(self):
        x = self.enterText()
        tkMessageBox.showinfo("Coordinates", x)



#main
root = Tk()
b = GeocodingWindow(root)
root.mainloop()