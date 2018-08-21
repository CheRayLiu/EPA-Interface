import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

def popupmsg(msg, result):
    popup = tk.Tk()
    def leavemini():
        popup.destroy()
    popup.wm_title("!")
    if result !="":
        s = tk.Scrollbar(popup)
        T = tk.Text(popup)

        T.focus_set()
        s.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=T.yview)
        T.config(yscrollcommand=s.set)
        T.insert(tk.END, result)
        B1 = ttk.Button(popup, text="Okay", command=leavemini)
        B1.pack()
    else:
        label = ttk.Label(popup, text = msg, font = NORM_FONT)
        label.pack(side = "top", fill = "x", pady = 10)
        B1 = ttk.Button(popup, text = "Okay", command = leavemini)
        B1.pack()
    popup.mainloop()


def confirmpop(confirm):
    popup = tk.Tk()
    def confirmy():
        confirm[0]="Y"
        popup.destroy()



    def confirmn():
        confirm[0]="N"
        popup.destroy()


    popup.wm_title("")
    label = ttk.Label(popup, text = "Confirm Input file and Run?", font = NORM_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    B1 = ttk.Button(popup, text = "Yes", command = confirmy)
    B2 = ttk.Button(popup, text="No", command=confirmn)
    B1.pack()
    B2.pack()
    popup.mainloop()
