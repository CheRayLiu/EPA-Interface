import subprocess
import os
import tkinter as tk
from tkinter import ttk
from popups import *

import sys





def confirm():
    confirm = "N"
    confirm = input("Confirm input ? (Y/N)")
    if confirm == "Y":
        return "Y"
    else:
        return "N"
def receptorInput():
    popupmsg("Please confirm AERMOD input file", "")
    openinput = subprocess.call('aermod.inp', cwd=r'D:\\EPA\\AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs', shell=True,stdout=subprocess.PIPE)

#Add popup to confirm input

    while True:
        confirm = ["N"]
        confirmpop(confirm)
        print(confirm)

        if confirm[0] == "Y":
            popupmsg("Processing...","")

            #Change directiy to where you save AERMOD
            os.chdir('D:\\EPA\AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs')
            os.system("aermod")
            popupmsg("Finished processing","")
            popupmsg("Displaying output file, close when done","")

            # Change directiy to where you save AERMOD
            openoutput = subprocess.call('aermod.out',
                                      cwd=r'D:\\EPA\\AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                                      shell=True, stdout=subprocess.PIPE)

            # Change directiy to where you save AERPLOT
            copyplot = subprocess.call('copy AERTEST_01H.PLT D:\\EPA\\AERPLOT_SCRAM',
                                      cwd=r'D:\\EPA\\AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\plotfiles',
                                      shell=True, stdout=subprocess.PIPE)
            popupmsg("Please confirm AERPLOT input file", "")
            # Change directiy to where you save AERPLOT
            openplotin = subprocess.call('aerplot.inp',
                                      cwd=r'D:\\EPA\\AERPLOT_SCRAM',
                                      shell=True, stdout=subprocess.PIPE)
            while True:
                confirmpop(confirm)
                if confirm[0] == "Y":
                    popupmsg("Loading Google Earth...", "")

                    # Change directiy to where you save AERPLOT
                    runplot = subprocess.call('aerplot_13329.exe',
                                          cwd=r'D:\\EPA\\AERPLOT_SCRAM',
                                          shell=True, stdout=subprocess.PIPE)
                break
            break
        if confirm[0] == "N":
            popupmsg("Please confirm AERMOD input file","")

            # Change directiy to where you save AERMOD
            openinput = subprocess.call('aermod.inp',
                                        cwd=r'D:\\EPA\\AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                                        shell=True, stdout=subprocess.PIPE)
        else:
            popupmsg("Please enter Y/N","")

