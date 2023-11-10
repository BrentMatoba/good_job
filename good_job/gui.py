import tkinter as tk
import grapher as graphy
import good_job



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
    graphy.countPlot()
    #grapher functions here
    return
def histplot():
    graphy.histPlotLastThirty()
    return

#lineFinder = tk.Label(root, text ="", bg="red", width=2, height=30);
#ineFinder.grid(row=0, column=20)

title = tk.Label(root, text="Pomodoro Tracker", fg="white")
title.grid(row=0, column=12)

buttonFrame = tk.Frame(root)
buttonFrame.grid()



startButton = tk.Button(buttonFrame, height=5, width=20,text="start pomodoro", command=start)
trackButton = tk.Button(buttonFrame, height=5, width=20, text="track pomodoro", command=track)
countplotButton = tk.Button(buttonFrame, height=5, width=20, text="countplot pomodoros", command=countplot)
histplotButton = tk.Button(buttonFrame, height=5, width=20, text="histplot pomodoros", command=histplot)


#move using the sticky method
placeholderFrame = tk.Frame(root) #In TKinter, having items in different containers makes it so that they don't physically interact
placeholderFrame.grid(row=3, column=10, padx=300)
placeholderLabel = tk.Label(placeholderFrame, text="", bg="blue", width=50, height=30)
placeholderLabel.grid()


startButton.grid(row=1, column=0)
trackButton.grid(row=2, column=0)
countplotButton.grid(row=3, column=0)
histplotButton.grid(row=4, column=0)

root.mainloop()
