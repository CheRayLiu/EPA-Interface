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
    confirm = ["N"]
    verifymsg ='1.1\n(1)能以錨點 ANCHORXY Anchor point specification \n(2)及座標方式\n(3)描述區域 \n(4)污染源 \n(5)及污染受體等平面資料 \n(6) 並在經緯度上能以卡笛生座標(Cartesian X- and Y-coordinates)及極座標(polar)標識並能和\n(7)UTM 位置表示法進行轉換'
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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
    confirm = ["N"]
    verifymsg = '1.2\n' \
                '(1)能標註多重區域 (Domain) DOMAINXY\n' \
                '(2)範圍及邊界,\n' \
                '(3)並標示區域包含之地形、污染源及污染受體\n\n' \
                +'1.3\n' \
                '(1)能處理汚染源位置,\n' \
                '(2)高度\n' \
                '(3)及所在地形(3)\n\n'\
                +'1.4\n' \
                 '(1)污染源型式包含單點,\n' \
                 '(2)量體(VOLUME),\n' \
                 '(3)矩形區域,\n' \
                 '(4)多邊形區域,\n' \
                 '(5)圓形區域\n\n'\
                 + '1.6\n' \
                   '能處理地形資料之水平及垂直資料\n\n'\
                 + '1.7\n' \
                   '(1)高度資料能由地理資料標示,\n' \
                   '(2)也能執行時輸入指定值\n\n' \
                 + '1.8\n' \
                    '(1)能連結不同格式之多重區域,\n' \
                    '(2)並能處理於邊界邊際上之污染受體'
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
        inp1 =  subprocess.Popen('aermap_NAD-GAP.inp', cwd=perdir + 'AERMAP\\aermap_testcase\\NAD_Gap', shell= True,stdout=subprocess.PIPE)


        process =subprocess.Popen('RunAERMAP', cwd=perdir +'AERMAP\\aermap_testcase\\NAD_Gap', shell= True,stdout=subprocess.PIPE)
        popupmsg("",process.communicate()[0].decode())

        os.chdir(aermodlocray + aermodloc)
        os.system('copy /y "aermod map2.inp" "aermod.inp"')
        os.system("aermod")

        copyplot = subprocess.call('copy TESTPM10_MULTYR_01H.PLT ' + aerplotray,
                                   cwd=aermodlocray + plotfiles,
                                   shell=True, stdout=subprocess.PIPE)

        runplot = subprocess.call('aerplot_13329.exe',
                                  cwd=aerplotray,
                                  shell=True, stdout=subprocess.PIPE)



def map3():
    confirm = ["N"]
    verifymsg = '1.9\n' \
                '(1) Debug output files具有異常情形除錯能力,\n' \
                '(2)輸出包含所處理的污染源、\n' \
                '(3)污染受體\n' \
                '(4)及高度等地理元件、\n' \
                '(5)參數\n' \
                '(6)及地理註記資訊'
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
        out = subprocess.Popen('aermap_NAD-GAP.out', cwd=perdir + 'AERMAP\\aermap_testcase\\NAD_Gap', shell=True,
                               stdout=subprocess.PIPE)

def met1():
    confirm = ["N"]
    verifymsg = '2.1\n' \
                '能處理至小時區間表面觀察(surface observations)的氣象資訊\n\n' \
                +'2.2\n' \
                 '現場(on-site)或場地特定評估程式(site-specific measurement program)的地理資料\n\n' \
                +'2.3\n' \
                 '由基本觀察氣象資訊中能萃取(extraction)高階氣象資訊\n\n' \
                +'2.4\n' \
                 '能由進行氣象資訊之資訊品質評估(quality assessment)\n\n' \
                +"2.5\n" \
                 "能進行地表,高空及特定指定等各類型氣象資訊之合併\n\n" \
                +"2.6\n" \
                 "能處理生成模擬預處理之氣象資料"
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":



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
    confirm = ["N"]
    verifymsg = '3.1\n' \
                '(1)能模擬整合地理、\n' \
                '(2)氣象資訊之' \
                '(3)指定污染源、\n' \
                '(4)污染受體\n' \
                '(5)於特定高度之預期結果\n\n' \
               +'3.2\n' \
                '能依指定平面及模擬影響情況\n\n' \
               +'3.3\n' \
                '能依污染受體所在不同地形進行不同情況模擬'\


    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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
    confirm = ["N"]
    verifymsg = '3.4\n' \
                '能依不同時間之氣象資料進行不同模擬\n\n' \
               +'3.5\n' \
                '能依多重型式污染源型式(點, 總量,區域)進行模擬\n\n' \
               +'3.6\n' \
                '(1)能於模擬結果顯示污染源、\n' \
                '(2)污染受體、\n' \
                '(3)地理選項、\n' \
                '(4)多重污源貢獻比例'

    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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
    confirm = ["N"]
    verifymsg = '3.7\n' \
                '能模擬一氧化碳擴污染影響情況'
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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
    confirm = ["N"]
    verifymsg = '3.8\n' \
                '(1)能模擬PM10,\n' \
                '(2)PM2.5擴污染影響情況'


    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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
    confirm = ["N"]
    verifymsg = '4.1\n' \
                '(1)具備和模擬軟體的互動式介面\n' \
                '(2)並產生時序結果\n\n' \
               +'4.2\n' \
                '能以介面指定模擬污染源型式包含' \
                '(1)點，\n' \
                '(2)矩型,\n' \
                '(3)圓型區域\n\n' \
               +'4.3\n' \
                '能以介面指定模擬建物下洗(Building downwash)能力\n\n' \
               +'4.4\n\n' \
                '能以介面指定模擬最高低温限制\n\n' \
               +'4.5\n' \
                '能以介面指定模擬地形高度\n\n' \
               +'4.6\n' \
                '能以介面指定模擬地表特性\n\n'\
               +'4.7\n' \
                '能以介面指定模擬影響平均區間為3小時/8小時/24小時及年度\n\n'
    verifypop(confirm, verifymsg)
    if confirm[0] == "Y":
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

