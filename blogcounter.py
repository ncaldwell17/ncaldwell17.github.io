from datetime import datetime, timedelta
from threading import Timer
from tkinter import *

import os

x = datetime.today()
y = x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t = y-x
secs = delta_t.total_seconds()
# t = Timer(secs, run_setProgram)

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        
        # self-created 
        self.init_window()
    
    def init_window(self):
        # kind of like the HTML meta title
        self.master.title("GUI")
        # Button() is a part of Tkinter's package
        # If you have the button's doing commands, best to make them inside the class 
        self.electButton = Button(self, text="openElections", command=self.open_elections)
        self.aiButton = Button(self, text="openAI", command=self.open_ai)
        self.geoButton = Button(self, text="openGeo", command=self.open_geo)
        self.closeButton = Button(self, text="quit", command=self.quit).place(x=0, y=90)
        # each object MUST be placed or it won't render 
        self.electButton.place(x=0, y=0)
        self.aiButton.place(x=0, y=30)
        self.geoButton.place(x=0, y=60)

        # seems to decide whether the buttons will be rendered 
        self.pack(fill=BOTH, expand=1)
    
    def open_elections(self):
        os.chdir("../..")
        path = "Desktop/ncaldwell17.github.io/projects/elections/posts"
        retval = os.getcwd()
        os.chdir(path)
        retval = os.getcwd()
        os.system('open .')
    
    def open_ai(self):
        os.chdir("../..")
        path = "Desktop/ncaldwell17.github.io/projects/ai/posts"
        retval = os.getcwd()
        os.chdir(path)
        retval = os.getcwd()
        os.system('open .')

    def open_geo(self):
        os.chdir("../..")
        path = "Desktop/ncaldwell17.github.io/projects/geo/posts"
        retval = os.getcwd()
        os.chdir(path)
        retval = os.getcwd()
        os.system('open .')
    
    def quit(self):
        exit()


# allows TK to work with what I've made 
myWindow = Tk()

# specifies the dimmensions of the window
myWindow.geometry("100x300")

# not sure what this does, but it just opens an empty window without it 
app = Window(myWindow)

# runs the program similar to what an if __main__ would do 
myWindow.mainloop()


