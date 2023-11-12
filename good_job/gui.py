import tkinter as tk
import grapher as graphy
import good_job



root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("1200x800")
root.resizable(False, False)


def start():
    countDownLabel(timerLabel)
def record():

    ##import good_job track functions here
    return
def countplot():
    graphy.countPlot()
    #grapher functions here
    return
def histplot():
    graphy.histPlotLastThirty()
    return
def countDownLabel(timerLabel, counter=1500):
    startButton.config(state=tk.DISABLED)
    if counter > 0:
        minutes, seconds = divmod(counter, 60)
        converted = f"{minutes:02d}:{seconds:02d}"
        timerLabel.config(text=converted)
        root.after(1000, countDownLabel, timerLabel, counter-1)


#lineFinder = tk.Label(root, text ="", bg="red", width=2, height=30);
#ineFinder.grid(row=0, column=20)

titleFrame = tk.Frame(root)
title = tk.Label(titleFrame, text="Pomodoro Tracker", fg="white")
title.grid()

buttonFrame = tk.Frame(root)
buttonFrame.place(x=100, y=50)





#buttons
startButton = tk.Button(buttonFrame, height=5, width=20,text="start pomodoro", command=start)
trackButton = tk.Button(buttonFrame, height=5, width=20, text="record pomodoro", command=record)
countplotButton = tk.Button(buttonFrame, height=5, width=20, text="countplot pomodoros", command=countplot)
histplotButton = tk.Button(buttonFrame, height=5, width=20, text="histplot pomodoros", command=histplot)


timerLabel = tk.Label(root, text=("0:00"), font=("Arial", 80), bg="blue", width=10, height=4)
timerLabel.place(x=600, y=50)



#startButton.grid(row=1, column=0)
#trackButton.grid(row=2, column=0)
#countplotButton.grid(row=3, column=0)
#histplotButton.grid(row=4, column=0)

startButton.pack()
trackButton.pack()
countplotButton.pack()
histplotButton.pack()

root.mainloop()
