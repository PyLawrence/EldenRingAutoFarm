from tkinter import *
import tkinter as tk
import commands
import gui

class ParentWindow(Frame):
    AutoEnabled = False
    currentSchedule = None
    scheduleThread = None
    checkTop = True


    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.master.geometry("200x200")

        self.master.resizable(False, False)
        self.master.title("Auto")
        self.master.configure(bg="#F0F0F0")
        # since I had to close out the thread, we needed manual functionality
        self.master.protocol("WM_DELETE_WINDOW", lambda: commands.closeWindow(self))

        gui.createGui(self)

        # it will attempt to auto run by default
        # commands.defaultSchedule(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()