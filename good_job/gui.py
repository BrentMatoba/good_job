import tkinter as tk
import grapher as graphy
import good_job
from subprocess import Popen
from PIL import Image, ImageTk

def countDownLabel(timerLabel, counter=15000): #counter should be 1500 for 25 min
    startButton.config(state=tk.DISABLED)
    if counter >= 0:
        minutes, seconds = divmod(counter, 60)
        converted = f"{minutes:02d}:{seconds:02d}"
        timerLabel.config(text=converted)
        root.after(1000, countDownLabel, timerLabel, counter-1)
    elif counter < 0:
        enableStart(startButton)
        good_job.goodJobSound()
        inputWindow()
def enableStart(startButton):
    startButton.config(state="normal")
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

def lastweekList():
    #Creates Window
    lastweekWindow = tk.Toplevel(root)
    lastweekWindow.title("Pomodoros From last week")
    lastweekWindow.geometry("800x400")
    lastweekWindow.resizable(False, False)


    list = graphy.lastweekList()
    for row in list:
        item = tk.Label(lastweekWindow, text=row)
        item.pack()


def inputWindow():
    def returnInfo():
        # take pomodoro type from dropdown menu, and text from tk.entry, and add to record function
        type = selectedOption.get()
        desc = description.get()
        good_job.logPomodoroGui(type, desc)

        iWindow.destroy()

    # Colors: B09E99 CINEREOUS, FEE9E1 MISTY ROSE, FAD4C0 APRICOT, 64B6AC VERDIGRIS, C0FDFB CELESTE
    #window boilerplate
    iWindow = tk.Toplevel(root, bg="#FEE9E1")
    iWindow.title("Input Window")
    iWindow.geometry("800x400")
    iWindow.resizable(False, False)

    #Gets pomodoro type
    selectedOption = tk.StringVar(root)
    options = ["odin", "Japaneseß", "extracurricular programming", "testing"]
    selectedOption.set(options[0])
    type = tk.OptionMenu(iWindow, selectedOption, *options)
    type.place(x=350, y=50)

    #gets pomodoro description
    descriptionTitle = tk.Label(iWindow, text="What did you do during the pomodoro?", bg="#FEE9E1", fg="black")
    descriptionTitle.pack()
    description = tk.Entry(iWindow, width=20)
    description.place(x=350, y=75)

    #creates record button
    iwindowRecord = tk.Button(iWindow, text="Record", bg="#FEE9E1", command=returnInfo)
    iwindowRecord.place(x=350, y=100)




root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("1200x800")
root.resizable(False, False)
root.configure(background="#FAD4C0")
#Colors: B09E99 CINEREOUS, FEE9E1 MISTY ROSE, FAD4C0 APRICOT, 64B6AC VERDIGRIS, C0FDFB CELESTE

#Buttons
#First Column
buttonFrame1 = tk.Frame(root)
buttonFrame1.place(x=100, y=50)

#Second Column
buttonFrame2 = tk.Frame(root)
buttonFrame2.place(x=350, y=50)

startButton = tk.Button(buttonFrame1, height=5, width=20,text="start pomodoro", command=start)
trackButton = tk.Button(buttonFrame1, height=5, width=20, text="record pomodoro", command=record)
countplotButton = tk.Button(buttonFrame1, height=5, width=20, text="countplot pomodoros", command=countplot)
histplotButton = tk.Button(buttonFrame1, height=5, width=20, text="histplot pomodoros", command=histplot)
openLogButton = tk.Button(buttonFrame2, height=5, width=20, text="Open Log", command=openLog)
lastweekButton = tk.Button(buttonFrame2, height=5, width=20, text="Last Week", command=lastweekList)

#Timer Label
timerLabel = tk.Label(root, text=("0:00"), font=("Arial", 80), bg="#B09E99", width=10, height=4)
timerLabel.place(x=600, y=50)

#Ranks
rankFrame = tk.Frame(root)
rankFrame.place(x=600, y=450)
rankFrame.configure(bg="white")
badgeText = tk.Label(rankFrame, text="Ranks", font=("Arial", 80), fg="black", bg="white", width=10, height=3)
badgeText.pack()

badgeIMG = Image.open("assets/Badges/Rank emblems1.png")
resizedIMG = badgeIMG.resize((100, 100))
cleanedIMG = ImageTk.PhotoImage(resizedIMG)
badge = tk.Label(rankFrame, image=cleanedIMG, bg="white")
badge.pack()


#Apply Buttons to main window
startButton.pack()
trackButton.pack()
countplotButton.pack()
histplotButton.pack()
openLogButton.pack()
lastweekButton.pack()



root.mainloop()
