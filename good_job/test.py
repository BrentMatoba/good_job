import tkinter as tk
root = tk.Tk()


def myClick():
    myLabel = tk.Label(root, text="Look! I clicked a button!")
    myLabel.pack()
myLabel1 = tk.Label(root, text="Hello World", fg="white")
myLabel2 = tk.Label(root, text="Hello World", fg="white")

#add buttons, notably this didn't work while the grid was active, seems like one or the other?
myButton = tk.Button(root, text="click me", command=myClick)
myButton.pack()





#Gives far more control over positioning than pack(). Remember that Python is Object oriented, and that these items are objects, and can be manipulated as such.
#myLabel1.grid(row = 0, column = 0)
#myLabel2.grid(row=1, column=0)



#tk.Entry creates an input box the user can access. How would I input this into goodjob? goodjob itself needs to be modified was well.
e = tk.Entry(root, width=50)
e.pack()






root.mainloop()