import tkinter as tk
from tkinter import ttk
import subprocess
import threading
from receptorInput import *
from receptorInput import popupmsg as popupmsg
from sourceEditor  import *






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








class EPAgui(tk.Tk):

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs) #convention, *args -> any number of variables, **kwargs -> pass through dictionaries

        tk.Tk.wm_title(self, "EPA Client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1) # 0 -> min size
        container.columnconfigure(0, weight=1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label="New Session", command = lambda: popupmsg("Not supported yet!",""))
        filemenu.add_command(label="Load File", command=lambda: popupmsg("Not supported yet!",""))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = quit)
        menubar.add_cascade(label="檔案 (File)"
                                  "", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=lambda: popupmsg("Not supported yet!",""))
        editmenu.add_command(label="Redo", command=lambda: popupmsg("Not supported yet!",""))
        tk.Tk.config(self, menu= menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)

        runmenu = tk.Menu(menubar, tearoff=0)
        runmenu.add_command(label="Run AERMAP testcase", command=lambda: threading.Thread(target=runAERMAP).start())
        runmenu.add_command(label="Run AERMOD testcase", command=lambda: threading.Thread(target=runAERMOD).start())
        runmenu.add_command(label="Run AERMET testcase", command=lambda: threading.Thread(target=runAERMET).start())
        runmenu.add_command(label="Edit AERMOD Source", command=lambda: threading.Thread(target=sourceBox).start())
        runmenu.add_command(label="Edit AERMOD Receptor", command=lambda: threading.Thread(target=numRec).start())
        runmenu.add_command(label="Run AERMOD with input", command=lambda: threading.Thread(target=receptorInput).start())
        #runmenu.add_command(label="Run AERSCREEN testcase", command=lambda: threading.Thread(target=runAERScreen).start())
        runmenu.add_command(label="Run AERSCREEN", command=lambda: threading.Thread(target=popinput).start())
        tk.Tk.config(self, menu=menubar)
        menubar.add_cascade(label="執行 (Run)", menu=runmenu)


        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row =0, column =0, sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button.pack()




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()



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
app.geometry("1280x720")
app.mainloop()

