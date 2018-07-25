import subprocess
import os
import tkinter as tk
from tkinter import ttk
from popups import *

import sys

aermodlocray= "D:\\EPA\\"
aermodlocper = "C:\\Users\\LFH\\Documents\\0.work\\Aermod\\EPA\\" 
aermodloc = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs"
plotfiles = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\plotfiles"

aerplotray = "D:\\EPA\\AERPLOT_SCRAM\\"
aerplotlocper = "C:\\Users\\LFH\\Documents\\0.work\\Aermod\\EPA\\"
aerplotloc = "AERPLOT\\aerplot_13329\\AERPLOT_SCRAM"
def confirm():
    confirm = "N"
    confirm = input("Confirm input ? (Y/N)")
    if confirm == "Y":
        return "Y"
    else:
        return "N"
def receptorInput():
    popupmsg("Please confirm AERMOD input file", "")
    #Change directly to where you save AERMOD
    print("hi")
    openinput = subprocess.call('aermod.inp', cwd=aermodlocray + aermodloc, shell=True,stdout=subprocess.PIPE)
    print("hi")
#Add popup to confirm input

    while True:
        confirm = ["N"]
        confirmpop(confirm)
        #print(confirm)

        if confirm[0] == "Y":
            popupmsg("Processing...","")

            #Change directiy to where you save AERMOD
            os.chdir(aermodlocray + aermodloc)
            os.system("aermod")
            popupmsg("Finished processing","")
            popupmsg("Displaying output file, close when done","")

            # Change directiy to where you save AERMOD
            openoutput = subprocess.call('aermod.out',
                                      cwd=aermodlocray + aermodloc,
                                      shell=True, stdout=subprocess.PIPE)

            # Change directiy to where you save AERPLOT
            copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray ,
                                      cwd=aermodlocray + plotfiles,
                                      shell=True, stdout=subprocess.PIPE)
            popupmsg("Please confirm AERPLOT input file", "")
            # Change directiy to where you save AERPLOT
            openplotin = subprocess.call('aerplot.inp',
                                      cwd=aerplotray,
                                      shell=True, stdout=subprocess.PIPE)
            while True:
                confirmpop(confirm)
                if confirm[0] == "Y":
                    popupmsg("Loading Google Earth...", "")

                    # Change directiy to where you save AERPLOT
                    runplot = subprocess.call('aerplot_13329.exe',
                                          cwd=aerplotray,
                                          shell=True, stdout=subprocess.PIPE)
                break
            break
        if confirm[0] == "N":
            popupmsg("Please confirm AERMOD input file","")

            # Change directiy to where you save AERMOD
            openinput = subprocess.call('aermod.inp',
                                        cwd=aermodlocray + aermodloc,
                                        shell=True, stdout=subprocess.PIPE)
        else:
            popupmsg("Please enter Y/N","")

#receptorInput()


