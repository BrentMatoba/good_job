import tkinter as tk
root = tk.Tk() #window, always comes first in Tkinter programs


#two steps of creating anything in Tkinter, first instantiate the object, then display it.
myLabel = tk.Label(root, text="Hello World", fg="white")

root.geometry("300x300")
myLabel.pack() #Places object onto screen


#Like game loops, Tkinter needs an event loop
root.mainloop()