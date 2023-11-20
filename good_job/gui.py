import tkinter as tk
import grapher as graphy
import good_job
from subprocess import Popen


def countDownLabel(timerLabel, counter=1500): #counter should be 1500 for 25 min
    startButton.config(state=tk.DISABLED)
    if counter >= 0:
        minutes, seconds = divmod(counter, 60)
        converted = f"{minutes:02d}:{seconds:02d}"
        timerLabel.config(text=converted)
        root.after(1000, countDownLabel, timerLabel, counter-1)
    elif counter < 0:
        good_job.logPomodoroGui()

def start():
    countDownLabel(timerLabel)

def record():
    inputWindow()
    #good_job.logPomodoroGui()

    return
def countplot():
    graphy.countPlot()
    #grapher functions here
    return
def histplot():
    graphy.histPlotLastThirty()
    return

def openLog():
    p = Popen("open log.csv", shell=True)



def inputWindow():
    def returnInfo():
        # take pomodoro type from dropdown menu, and text from tk.entry, and add to record function
        type = selectedOption.get()
        desc = description.get()
        good_job.logPomodoroGui(type, desc)

        iWindow.destroy()



    #window boilerplate
    iWindow = tk.Toplevel(root)
    iWindow.title("Input Window")
    iWindow.geometry("800x400")
    iWindow.resizable(False, False)

    #Gets pomodoro type
    selectedOption = tk.StringVar(root)
    options = ["Japanese", "odin", "extracurricular programming", "testing"]
    selectedOption.set(options[0])
    type = tk.OptionMenu(iWindow, selectedOption, *options)
    type.place(x=350, y=50)

    #gets pomodoro description
    descriptionTitle = tk.Label(iWindow, text="What did you do during the pomdoro?")
    descriptionTitle.pack()
    description = tk.Entry(iWindow, width=20)
    description.place(x=350, y=75)

    #creates record button
    iwindowRecord = tk.Button(iWindow, text="Record", command=returnInfo)
    iwindowRecord.place(x=350, y=100)




root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("1200x800")
root.resizable(False, False)

#Buttons
buttonFrame = tk.Frame(root)
buttonFrame.place(x=100, y=50)

startButton = tk.Button(buttonFrame, height=5, width=20,text="start pomodoro", command=start)
trackButton = tk.Button(buttonFrame, height=5, width=20, text="record pomodoro", command=record)
countplotButton = tk.Button(buttonFrame, height=5, width=20, text="countplot pomodoros", command=countplot)
histplotButton = tk.Button(buttonFrame, height=5, width=20, text="histplot pomodoros", command=histplot)


#Timer Label
timerLabel = tk.Label(root, text=("0:00"), font=("Arial", 80), bg="blue", width=10, height=4)
timerLabel.place(x=600, y=50)


startButton.pack()
trackButton.pack()
countplotButton.pack()
histplotButton.pack()

openLog()

root.mainloop()
