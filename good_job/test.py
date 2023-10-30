import tkinter as tk
root = tk.Tk()
myLabel1 = tk.Label(root, text="Hello World", fg="white")
myLabel2 = tk.Label(root, text="Hello World", fg="white")

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row=1, column=0)

root.mainloop()