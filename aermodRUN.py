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

def run():

            os.chdir(aermodlocray + aermodloc)
            os.system("aermod")


            copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray ,
                                      cwd=aermodlocray + plotfiles,
                                      shell=True, stdout=subprocess.PIPE)


            runplot = subprocess.call('aerplot_13329.exe',
                                          cwd=aerplotray,
                                          shell=True, stdout=subprocess.PIPE)






