from tkinter import *

root = Tk() #window, always comes first in Tkinter programs

#two steps of creating anything in Tkinter, first instantiate the object, then display it.
myLabel = Label(root, text="Hello World")
myLabel.pack() #Places object onto screen

#Like game loops, Tkinter needs an event loop
root.mainloop()