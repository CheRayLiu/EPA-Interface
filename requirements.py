import subprocess
from popups import *

perdir = "D:\\EPA\\"

from receptorEditor import *
from tkinter import ttk
from popups import *

import sys

aermodlocpray= "D:\\EPA\\"
aermodloclfh = "C:\\Users\\LFH\\Documents\\0.work\\Aermod\\EPA\\"
aermodloc = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs"
plotfiles = "AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\plotfiles"

aerplotray = "D:\\EPA\\AERPLOT_SCRAM\\"
aerplotlocper = "C:\\Users\\LFH\\Documents\\0.work\\Aermod\\EPA\\"
aerplotloc = "AERPLOT\\aerplot_13329\\AERPLOT_SCRAM"



def mapMult():
    inp1 =  subprocess.Popen('aermap_nad27_dem.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NW_Durham', shell= True,stdout=subprocess.PIPE)
    inp2 = subprocess.Popen('aermap_nad27_ned.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NW_Durham', shell=True,
                           stdout=subprocess.PIPE)
    inp3 = subprocess.Popen('aermap_nad83_dem.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NW_Durham', shell=True,
                           stdout=subprocess.PIPE)
    inp4 = subprocess.Popen('aermap_nad83_ned.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NW_Durham', shell=True,
                           stdout=subprocess.PIPE)


    process =subprocess.Popen('RunAERMAP', cwd=perdir +'AERMAP\\aermap_testcase\\NW_Durham', shell= True,stdout=subprocess.PIPE)
    popupmsg("",process.communicate()[0].decode())

    os.chdir(aermodlocray + aermodloc)
    os.system('copy /y "aermod map1.inp" "aermod.inp"')
    os.system("aermod")

    copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray,
                               cwd=aermodlocray + plotfiles,
                               shell=True, stdout=subprocess.PIPE)

    runplot = subprocess.call('aerplot_13329.exe',
                              cwd=aerplotray,
                              shell=True, stdout=subprocess.PIPE)




def map2():
    inp1 =  subprocess.Popen('aermap_NAD-GAP.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NAD_Gap', shell= True,stdout=subprocess.PIPE)


    process =subprocess.Popen('RunAERMAP', cwd=perdir +'AERMAP\\aermap_testcase\\NAD_Gap', shell= True,stdout=subprocess.PIPE)
    popupmsg("",process.communicate()[0].decode())



def map3():
    out = subprocess.Popen('aermap_NAD-GAP.out', cwd=perdir + 'AERMAP\\aermap_testcase\\NAD_Gap', shell=True,
                           stdout=subprocess.PIPE)

def met1():




        process = subprocess.Popen('run_aermet_test_suite >> out_met.txt',
                                   cwd=perdir + 'AERMET\\aermet_test_cases_18081\\aermet_def_testcases_18081',
                                   shell=True,
                                   stdout=subprocess.PIPE)

        process = subprocess.Popen('out_met.txt',
                                   cwd=perdir + 'AERMET\\aermet_test_cases_18081\\aermet_def_testcases_18081',
                                   shell=True,
                                   stdout=subprocess.PIPE)


        os.chdir(aermodlocray + aermodloc)
        os.system('copy /y "aermod OG.inp" "aermod.inp"')
        os.system("aermod")

        copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray,
                                   cwd=aermodlocray + plotfiles,
                                   shell=True, stdout=subprocess.PIPE)

        runplot = subprocess.call('aerplot_13329.exe',
                                  cwd=aerplotray,
                                  shell=True, stdout=subprocess.PIPE)



def mod1():
    os.chdir(aermodlocray + aermodloc)
    os.system('copy /y "aermod OG.inp" "aermod.inp"')

    inp1 = subprocess.Popen('aermod.inp',
                            cwd=perdir + 'AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                            shell=True,
                            stdout=subprocess.PIPE)
    os.system("aermod")

    copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray,
                               cwd=aermodlocray + plotfiles,
                               shell=True, stdout=subprocess.PIPE)

    runplot = subprocess.call('aerplot_13329.exe',
                              cwd=aerplotray,
                              shell=True, stdout=subprocess.PIPE)


def mod2():
    os.chdir(aermodlocray + aermodloc)
    os.system('copy /y "allsrcs.inp" "aermod.inp"')
    os.system("aermod")
    inp1 = subprocess.Popen('aermod.inp',
                            cwd=perdir + 'AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                            shell=True,
                            stdout=subprocess.PIPE)
    os.system("aermod")

    copyplot = subprocess.call('copy ALLSRCS_STACKDW_24H.PLT ' + aerplotray,
                               cwd=aermodlocray + plotfiles,
                               shell=True, stdout=subprocess.PIPE)
    changename = subprocess.call('copy /y "ALLSRCS_STACKDW_24H.PLT" "TESTPM10_MULTYR_01H.PLT"',
                              cwd=aerplotray,
                              shell=True, stdout=subprocess.PIPE)
    runplot = subprocess.call('aerplot_13329.exe',
                              cwd=aerplotray,
                              shell=True, stdout=subprocess.PIPE)
    out = subprocess.Popen('aermod.out',
                            cwd=perdir + 'AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                            shell=True,
                            stdout=subprocess.PIPE)
def mod7():
    # in1 = subprocess.Popen('aermod.inp',
    #                         cwd=perdir + 'AERMOD\\CO',
    #                         shell=True,
    #                         stdout=subprocess.PIPE)
    # os.chdir(perdir + 'AERMOD\\CO')
    # os.system('aermod')




    out1 = subprocess.Popen('aermod.out',
                           cwd=perdir + 'AERMOD\\CO',
                           shell=True,
                           stdout=subprocess.PIPE)
    copyplot = subprocess.call('copy ORD15CO1.PLT' + aerplotray,
                               cwd=perdir + 'AERMOD\\CO',
                               shell=True, stdout=subprocess.PIPE)
    changename = subprocess.call('copy /y "ORD15CO1.PLT" "TESTPM10_MULTYR_01H.PLT"',
                                 cwd=aerplotray,
                                 shell=True, stdout=subprocess.PIPE)
    runplot = subprocess.call('aerplot_13329.exe',
                              cwd=aerplotray,
                              shell=True, stdout=subprocess.PIPE)

def mod8():
        os.chdir(aermodlocray + aermodloc)
        os.system('copy /y "testpm10.inp" "aermod.inp"')
        os.system("aermod")

        os.system('copy /y "testpm25.inp" "aermod.inp"')
        os.system("aermod")
        out25 = subprocess.Popen('testpm25.out',
                                cwd=perdir + 'AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                                shell=True,
                                stdout=subprocess.PIPE)

        out10 = subprocess.Popen('testpm10.out',
                                 cwd=perdir + 'AERMOD\\aermod_test_cases_18081\\aermet_def_16216_aermod_16216r\\inputs',
                                 shell=True,
                                 stdout=subprocess.PIPE)
        copyplot = subprocess.call('copy TESTPM10_01H.PLT ' + aerplotray,
                                   cwd=aermodlocray + plotfiles,
                                   shell=True, stdout=subprocess.PIPE)
        copyplot = subprocess.call('copy TESTPM25_01H.PLT ' + aerplotray,
                                   cwd=aermodlocray + plotfiles,
                                   shell=True, stdout=subprocess.PIPE)
        changename = subprocess.call('copy /y "TESTPM10_01H.PLT" "TESTPM10_MULTYR_01H.PLT"',
                                     cwd=aerplotray,
                                     shell=True, stdout=subprocess.PIPE)
        runplot = subprocess.call('aerplot_13329.exe',
                                  cwd=aerplotray,
                                  shell=True, stdout=subprocess.PIPE)

        changename = subprocess.call('copy /y "TESTPM25_01H.PLT" "TESTPM10_MULTYR_01H.PLT"',
                                     cwd=aerplotray,
                                     shell=True, stdout=subprocess.PIPE)
        runplot = subprocess.call('aerplot_13329.exe',
                                  cwd=aerplotray,
                                  shell=True, stdout=subprocess.PIPE)

def screen1():
    os.chdir(perdir + 'AERScreen\\aerscreen_test_cases')
    os.system("start cmd /c AERSCREEN")

    # process = subprocess.Popen('run_aerscreen',
    #                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\area',
    #                            shell=True,
    #                            stdout=subprocess.PIPE)
    #
    # popupmsg("", process.communicate()[0].decode())
    out1 = subprocess.Popen('AERSCREEN_AREA.out',
                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\area',
                            shell=True,
                            stdout=subprocess.PIPE)

    # process = subprocess.Popen('run_aerscreen',
    #                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\point',
    #                            shell=True,
    #                            stdout=subprocess.PIPE)
    #
    # popupmsg("", process.communicate()[0].decode())
    out2 = subprocess.Popen('AERSCREEN_FLAT_DW.out',
                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\point',
                            shell=True,
                            stdout=subprocess.PIPE)

    # process = subprocess.Popen('run_aerscreen',
    #                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\circle',
    #                            shell=True,
    #                            stdout=subprocess.PIPE)
    #
    # popupmsg("", process.communicate()[0].decode())
    out3 = subprocess.Popen('AERSCREEN_FLAT.out',
                            cwd=perdir + 'AERScreen\\aerscreen_test_cases\\circle',
                            shell=True,
                            stdout=subprocess.PIPE)

