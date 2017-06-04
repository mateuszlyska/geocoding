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

#main
root = Tk()

#Entering cities label
cityLabel = Label(root, text = "Cities:", bg = "white", fg = "green")
cityLabel.grid(row=0, sticky=E)

#Entering cities
cityEntry = Entry(root)
cityEntry.grid(row=0, column=1)

#Message box
def messageCoord(event):
    tkMessageBox.showinfo("Coordinates", "Hello")

#Starting button
butStart = Button(root, text = "Find coordinates", fg = "red")
butStart.bind("<Button-1>", messageCoord)
butStart.grid(columnspan=2)

root.mainloop()