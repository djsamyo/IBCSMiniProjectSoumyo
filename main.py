from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global appName
from volunteer import volunteerForm
import pandas as pd


class mainFrame():
    def __init__(self, parent):
        global mainframe
        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        menubar = Menu(root)

        registerMenu = Menu(menubar, tearoff=0)
        registerMenu.add_command(label="Volunteers", command=self.openVolunteerFrame)
        registerMenu.add_command(label="Supervisors")
        menubar.add_cascade(label="Register", menu=registerMenu)

        parent.config(menu=menubar)

    def openVolunteerFrame(self):
        for widget in mainframe.winfo_children():
            widget.destroy()
        volunteerForm(mainframe)


appName = "Di@Tech"
root = Tk()
root.title(appName)
mainFrame(root)

root.mainloop()
