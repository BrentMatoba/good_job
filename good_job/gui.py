import tkinter as tk

root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("1200x800")
root.resizable(False, False)


def start():
    ##import good_job here, why doesn't import work??
    return

def track():
    ##import good_job track functions here
    return
def countplot():
    #grapher functions here
    return

#lineFinder = tk.Label(root, text ="", bg="red", width=2, height=30);
#ineFinder.grid(row=0, column=20)

title = tk.Label(root, text="Pomodoro Tracker", fg="white")
title.grid(row=0, column=12)

dataButtonFrame = tk.Frame(root)
dataButtonFrame.grid()



startButton = tk.Button(root, height=5, width=20,text="start pomodoro", command=start)
trackButton = tk.Button(root, height=5, width=20, text="track pomodoro", command=track)
countplotButton = tk.Button(dataButtonFrame, height=5, width=20, text="countplot pomodoros", command=countplot)


#move using the sticky method
placeholderFrame = tk.Frame(root) #In TKinter, having items in different containers makes it so that they don't physically interact
placeholderFrame.grid(row=3, column=10, padx=425)
placeholderLabel = tk.Label(placeholderFrame, text="", bg="blue", width=50, height=30)
placeholderLabel.grid()


startButton.grid(row=3, column=0)
trackButton.grid(row=2, column=0)
countplotButton.grid(row=2, column=3)

root.mainloop()
