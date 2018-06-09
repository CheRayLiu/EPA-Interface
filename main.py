import tkinter as tk
from tkinter import ttk
import subprocess
import threading

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

def runAERMAP():
    process =subprocess.Popen('RunAERMAP', cwd=r'D:\\EPA\\AERMAP\\aermap_testcase\\NW_Durham', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())



def runAERMOD():
    process =subprocess.Popen('runtests_AERMOD', cwd=r'D:\EPA\AERMOD\aermod_test_cases_18081\aermet_def_16216_aermod_16216r', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())




def runAERMET():
    process =subprocess.Popen('run_aermet_test_suite', cwd=r'D:\EPA\AERMET\aermet_test_cases_18081\aermet_def_testcases_18081', shell= True,stdout=subprocess.PIPE)

    popupmsg("",process.communicate()[0].decode())



def runAERScreen():
    process =subprocess.Popen('run_aerscreen', cwd=r'D:\EPA\AERScreen\aerscreen_test_cases\point', shell= True,stdout=subprocess.PIPE)

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
        runmenu.add_command(label="Run AERMAP", command=lambda: threading.Thread(target=runAERMAP).start())
        runmenu.add_command(label="Run AERMOD", command=lambda: threading.Thread(target=runAERMOD).start())
        runmenu.add_command(label="Run AERMET", command=lambda: threading.Thread(target=runAERMET).start())
        runmenu.add_command(label="Run AERSCREEN", command=lambda: threading.Thread(target=runAERScreen).start())
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

