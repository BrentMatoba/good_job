import tkinter as tk



root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("500x500")



def start():
    ##import good_job here, why doesn't import work??

startButton = tk.Button(root, text="start pomodoro", command=start())
trackButton = tk.Button(root, text="track pomodoro")

startButton.pack()
trackButton.pack()

root.mainloop()