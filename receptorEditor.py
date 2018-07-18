import tkinter as tk
from tkinter import ttk
import threading
import fileinput
import subprocess


aermodlocper = "D:\\EPA\\"
aermodloc = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs"
aermodIn = aermodlocper + aermodloc + "\\aermod.inp"
origfile ='                 ORIG'
distfile ='				 DIST'
gdirfile ='                 GDIR'


def numRec():
    popin = tk.Tk()
    popin.title("Input")
    tk.Label(popin, text="Number of receptor rings: ").grid(row=0)

    e1 = tk.Entry(popin)

    e1.grid(row=0, column=1)

    ttk.Button(popin, text='Enter',
               command=lambda: threading.Thread(target=recInput(int(e1.get()))).start()).grid(row=8, sticky=tk.W, pady=4)
    ttk.Button(popin, text='Quit', command=lambda: threading.Thread(target=popin.destroy).start()).grid(row=9,
                                                                                                        sticky=tk.W,
                                                                                                        pady=4)

    popin.mainloop()



def recInput(rec):

    recEdit = tk.Tk()
    recEdit.title("!")
    tk.Label(recEdit, text="ORIG: ").grid(row=1)
    orig = tk.Entry(recEdit)
    orig.grid(row=1, column=1)

    origstr = origfile+" "+str(orig.get()) + "\n"
    tk.Label(recEdit, text="DIST: ").grid(row=2)
    dist =[]
    for i in range(rec):
        dist.append(tk.Entry(recEdit))
        dist[i].grid(row=2, column = i+1)

    tk.Label(recEdit, text="GDIR: ").grid(row=3)

    gdir = []

    for i in range(3):
        gdir.append(tk.Entry(recEdit))
        gdir[i].grid(row=3, column = i + 1)

    ttk.Button(recEdit, text='Enter',
               command=lambda: threading.Thread(target=combine(orig, dist, gdir)).start()).grid(row=8, sticky=tk.W,
                                                                                              pady=4)

    ttk.Button(recEdit, text='Quit', command=lambda: threading.Thread(target=recEdit.destroy).start()).grid(row=9,
                                                                                                        sticky=tk.W,
                                                                                                        pady=4)
    recEdit.mainloop()



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



def combine(orig, dist, gdir):
    origstr = origfile + " " + str(orig.get()) + "\n"

    diststr = distfile

    for i in range(len(dist)):
        diststr += " " + str(dist[i].get()) + "."
    diststr += "\n"

    gdirstr = gdirfile

    for i in range(len(gdir)):
        gdirstr += " " + str(gdir[i].get()) + " "
    gdirstr += "\n"

    aermodIn = aermodlocper + aermodloc + "\\aermod.inp"
    searchRepLine("ORIG", origstr, aermodIn)
    searchRepLine("DIST", diststr, aermodIn)
    searchRepLine("GDIR", gdirstr, aermodIn)
    openinput = subprocess.call('aermod.inp', cwd=aermodlocper + aermodloc, shell=True, stdout=subprocess.PIPE)



numRec()







