import tkinter as tk
from tkinter import ttk
import subprocess
import threading
from receptorInput import *
from receptorInput import popupmsg as popupmsg
from sourceEditor  import *
import time
from PIL import ImageTk, Image
from aermodRUN import *
from requirements import *






def popinput():
    popin = tk.Tk()
    popin.title("Input")
    tk.Label(popin, text="Input Location").grid(row=0)

    e1 = tk.Entry(popin)


    e1.grid(row=0, column=1)

    ttk.Button(popin, text='Confirm input file and Run AERSCREEN', command= lambda: threading.Thread(target=create_aerin(e1.get())).start()).grid(row=8, sticky=tk.W, pady=4)
    ttk.Button(popin, text='Quit', command= lambda: threading.Thread(target=popin.destroy).start()).grid(row=9, sticky=tk.W, pady=4)

    popin.mainloop()

def create_aerin(loc):
    process = subprocess.call('copy /Y ' +loc+' aerscreen.inp', cwd=r'D:\\AERSCREEN', shell=True,
                     stdout=subprocess.PIPE)
    run_aerscreen()

def run_aerscreen():
    process = subprocess.call('execute', cwd=r'D:\\AERSCREEN', shell=True,
                              stdout=subprocess.PIPE)
    popupmsg("", process.communicate()[0].decode())


def runAERMAP():
    process =subprocess.Popen('RunAERMAP', cwd=r'D:\\EPA\\AERMAP\\aermap_testcase\\NW_Durham', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())



def runAERMOD():
    process =subprocess.Popen('runtests_AERMOD', cwd=r'D:\EPA\AERMOD\aermod_test_cases_18081\aermet_def_16216_aermod_16216r', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())




def runAERMET():
    process =subprocess.Popen('run_aermet_test_suite', cwd=r'D:\EPA\AERMET\aermet_test_cases_18081\aermet_def_testcases_18081', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())







class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("ARTISC Version 1.8.1")

        self.geometry("400x358")
        
        img = ImageTk.PhotoImage(file = "companylogy.jpg")

        imgicon = ImageTk.PhotoImage(file='company.ico')
        self.tk.call('wm', 'iconphoto', self._w, imgicon)
        panel = tk.Label(self, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        ## required to make window show before the program gets to the mainloop
        self.update()

class EPAgui(tk.Tk):

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs) #convention, *args -> any number of variables, **kwargs -> pass through dictionaries


        tk.Tk.wm_title(self, "ARTISC Version 1.8.1")
        imgicon = ImageTk.PhotoImage(file='company.ico')

        self.tk.call('wm', 'iconphoto', self._w, imgicon)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1) # 0 -> min size
        container.columnconfigure(0, weight=1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Session", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        filemenu.add_command(label="Load File", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        filemenu.add_separator()
        
        menubar.add_cascade(label="檔案 (File)"
                                  "", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="汙染源", command=lambda: threading.Thread(target=sourceBox).start())
        editmenu.add_command(label="接受體", command=lambda: threading.Thread(target=numRec).start())
        editmenu.add_command(label="地理/地形", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        editmenu.add_command(label="氣候", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        editmenu.add_command(label="建築物", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        # runmenu.add_command(label="Run AERSCREEN testcase", command=lambda: threading.Thread(target=runAERScreen).start())
        menubar.add_cascade(label="汙染環境(Environment input)", menu=editmenu)

        sensormenu = tk.Menu(menubar, tearoff=0)
        sensormenu.add_command(label="汙染源", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        sensormenu.add_command(label="接受體", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        sensormenu.add_command(label="地理/地形", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        sensormenu.add_command(label="氣候", command=lambda:threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        sensormenu.add_command(label="建築物", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        tk.Tk.config(self, menu=menubar)
        menubar.add_cascade(label="汙染監控(Environment sensors)", menu=sensormenu)

        simuMenu = tk.Menu(menubar, tearoff=0)
        simuMenu.add_command(label="自動模擬",
                             command=lambda: threading.Thread(target=run).start())
        simuMenu.add_command(label="分鐘", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="小時", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="天日", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="星期", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="月", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="年", command=lambda:threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        simuMenu.add_command(label="依輸入資料", command= lambda: threading.Thread(target=receptorInput).start())

        menubar.add_cascade(label="汙染模擬(Simulation)", menu=simuMenu)

        resultMenu = tk.Menu(menubar, tearoff=0)
        resultMenu.add_command(label="過程檔案", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        resultMenu.add_command(label="結果檔案", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        resultMenu.add_command(label="除錯檔案", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        resultMenu.add_command(label="圖形結果", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())

        menubar.add_cascade(label="模擬結果(Result)", menu=resultMenu)

        recordMenu = tk.Menu(menubar, tearoff=0)
        recordMenu.add_command(label="Temp", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        recordMenu.add_command(label="Temp", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())

        menubar.add_cascade(label="模擬紀錄(Record)", menu=recordMenu)

        prefMenu = tk.Menu(menubar, tearoff=0)
        prefMenu.add_command(label="Temp", command=lambda:threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        prefMenu.add_command(label="Temp", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())

        menubar.add_cascade(label="偏好設定(User Preference)", menu=prefMenu)

        aboutMenu = tk.Menu(menubar, tearoff=0)
        aboutMenu.add_command(label="幫助", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        aboutMenu.add_command(label="版權", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        aboutMenu.add_command(label="使用合約", command=lambda: threading.Thread(target=popupmsg("Not supported yet!", "")).start())
        aboutMenu.add_command(label="Run AERMAP testcase", command=lambda: threading.Thread(target=runAERMAP).start())
        aboutMenu.add_command(label="Run AERMOD testcase", command=lambda: threading.Thread(target=runAERMOD).start())
        aboutMenu.add_command(label="Run AERMET testcase", command=lambda: threading.Thread(target=runAERMET).start())
        tk.Tk.config(self, menu=menubar)
        menubar.add_cascade(label="關於 About", menu=aboutMenu)

        reqMenu = tk.Menu(menubar, tearoff=0)

        aermapMenu = tk.Menu(reqMenu, tearoff =0)
        reqMenu.add_cascade(label = '地形資料處理 Examples',underline=0,
                               menu= aermapMenu)



        aermapMenu.add_command(label="地形資料處理 Example 1", command=lambda: threading.Thread(target=mapMult).start())
        aermapMenu.add_command(label="地形資料處理 Example 2",
                              command=lambda: threading.Thread(target=map2).start())
        aermapMenu.add_command(label="地形資料處理 Output File",
                            command=lambda: threading.Thread(target=map3).start())
        reqMenu.add_command(label="氣象資料處理",
                              command=lambda: threading.Thread(target=met1).start())

        aermodMenu = tk.Menu(reqMenu, tearoff=0)
        reqMenu.add_cascade(label='大氣擴散污染評估 Examples', underline=0,
                            menu=aermodMenu)
        aermodMenu.add_command(label="大氣擴散污染評估 Example 1",
                            command=lambda: threading.Thread(target=mod1).start())
        aermodMenu.add_command(label="大氣擴散污染評估 Example 2",
                            command=lambda: threading.Thread(target=mod2).start())
        aermodMenu.add_command(label="大氣擴散污染評估 Example 3",
                            command=lambda: threading.Thread(target=mod7).start())
        aermodMenu.add_command(label="大氣擴散污染評估 Example 4",
                            command=lambda: threading.Thread(target=mod8).start())
        aermodMenu.add_command(label="AERSCREEN",
                            command=lambda: threading.Thread(target=screen1).start())
        tk.Tk.config(self, menu=menubar)
        menubar.add_cascade(label="Function Verify", menu=reqMenu)









        self.withdraw()
        splash = Splash(self)

        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()


    # def show_frame(self,cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Start Page", font = LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
#         button1.pack()
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Page One", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
#         button1.pack()
#
#         button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
#         button.pack()
#
#
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Page Two", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
#         button.pack()
#
#         button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
#         button1.pack()



# class Gui:
#
#     def refresh(self):
#         self.root.update()
#         self.root.after(1000,self.refresh)
#
#     def start(self):
#         self.refresh()
#         threading.Thread(target=doingALotOfStuff).start()
#
# #outside
# GUI = Gui(Tk())
# GUI.mainloop()



app = EPAgui()
app.geometry("1200x768")
app.mainloop()

