import tkinter as tk



root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("500x500")



def start():
    ##import good_job here, why doesn't import work??
    return

def track():
    ##import good_job track functions here
    return
def countplot():
    #grapher functions here
    return

startButton = tk.Button(root, text="start pomodoro", command=start)
trackButton = tk.Button(root, text="track pomodoro", command=track)
countplotButton = tk.Button(root, text="countplot pomodoros", command=countplot)


startButton.pack()
trackButton.pack()
countplotButton.pack()

root.mainloop()