import tkinter as tk
from tkinter import ttk
import threading
import fileinput
import subprocess



aermodlocper = "D:\\EPA\\"
aermodloc = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs"
aermodIn = aermodlocper + aermodloc + "\\aermod.inp"
locationog = "   LOCATION"

def sourceBox():
    popin = tk.Tk()
    popin.geometry("300x200")
    popin.title("Enter Source info")
    tk.Label(popin, text="Source ID: ").grid(row=0)
    tk.Label(popin, text="Source Type: ").grid(row=1)
    tk.Label(popin, text="Xs: ").grid(row=2)
    tk.Label(popin, text="Ys: ").grid(row=3)
    tk.Label(popin, text="Zs (Optional): ").grid(row=4)


    id = tk.Entry(popin)
    id.grid(row=0, column=1)


    type = tk.Entry(popin)
    type.grid(row=1, column=1)


    xin = tk.Entry(popin)
    xin.grid(row=2, column=1)


    yin = tk.Entry(popin)
    yin.grid(row=3, column=1)


    zin = tk.Entry(popin)
    zin.grid(row=4, column=1)



    ttk.Button(popin, text='Enter', command=lambda: threading.Thread(target= combine(popin,str(id.get()), str(type.get()), str(xin.get()), str(yin.get()), str(zin.get())) ).start()).grid(row=8, sticky=tk.W, pady=4)

    ttk.Button(popin, text='Quit', command=lambda: threading.Thread(target=popin.destroy).start()).grid(row=9,
                                                                                                        sticky=tk.W,
                                                                                                        pady=4)

    popin.mainloop()



def searchRepLine(keyword,sub,filename):

    f = open(filename, "r")

    for line in f:
        if keyword in line:
            orig = line
    f.close()

    with fileinput.FileInput(aermodIn, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(orig, sub), end='')
    fileinput.close()



def combine(popin,id, type, xin, yin, zin):
    popin.destroy()
    sourceLoc = locationog + "  " + id + "  " + type + "  "  + xin + "  " + yin + "  " + zin + "\n"


    aermodIn = aermodlocper + aermodloc + "\\aermod.inp"
    searchRepLine("LOCATION", sourceLoc, aermodIn)
    openinput = subprocess.call('aermod.inp', cwd=aermodlocper + aermodloc, shell=True, stdout=subprocess.PIPE)





#sourceBox()







