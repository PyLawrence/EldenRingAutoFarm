from tkinter import *
import tkinter as tk
import commands


def createGui(self):
    """
       creates the window gui
       :param self: the tkinter frame we'd like to create the gui in
       :return:
       """

    self.lbl_From = tk.Label(self.master, text='Elden Ring Auto Farm')
    self.lbl_From.place(relx=0.5, rely=0.1, anchor=N)


    self.setExt = tk.Button(self.master, width=20, height=2, text='Start', command=lambda: commands.startStop(self))
    self.setExt.place(relx=0.5, rely=0.2, anchor=N)

    self.checkVar = IntVar(value=1)
    self.checkTopCbox = tk.Checkbutton(self.master, text="Check Foreground", variable=self.checkVar)
    self.checkTopCbox.place(relx=0.5, rely=0.5, anchor=CENTER)

    self.lbl_From = tk.Label(self.master, text='Delay')
    self.lbl_From.place(relx=0.5, rely=0.7, anchor=CENTER)

    self.delayString = StringVar()
    self.delay = tk.Entry(self.master, textvariable=self.delayString, width=20, font="Helvetica 10")
    self.delay.insert(0, "15")
    self.delay.place(relx=0.5, rely=0.8, anchor=CENTER)

