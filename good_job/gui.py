import tkinter as tk

root = tk.Tk()
root.title("Pomodoro Tracker")
root.geometry("300x300")


startButton = tk.Button(root, text="start pomodoro")
trackButton = tk.Button(root, text="track pomodoro")

startButton.pack()
trackButton.pack()

root.mainloop()