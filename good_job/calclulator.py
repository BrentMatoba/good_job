import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

e = tk.Entry(root, width=35 , borderwidth =5)
e.grid(row=0, column=0, columnspan=3, paxd=10, pady=10)

def button_add():

tk.Button_1(root, text="1", padx-40,pady=20, command=button_add)
tk.Button_2(root, text="2", padx-40,pady=20, command=button_add)
tk.Button_3(root, text="3", padx-40,pady=20, command=button_add)
tk.Button_4(root, text="4", padx-40,pady=20, command=button_add)
tk.Button_5(root, text="5", padx-40,pady=20, command=button_add)
tk.Button_6(root, text="6", padx-40,pady=20, command=button_add)
tk.Button_7(root, text="7", padx-40,pady=20, command=button_add)
tk.Button_8(root, text="8", padx-40,pady=20, command=button_add)
tk.Button_9(root, text="9", padx-40,pady=20, command=button_add)
tk.Button_0(root, text="0", padx-40,pady=20, command=button_add)




root.mainloop()