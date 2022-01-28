from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from supervisors import supervisorForm
from volunteer import volunteerForm

global appName


class mainFrame():
    def __init__(self, parent):
        self.mainframe = ttk.Frame(parent, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        menubar = Menu(root)

        registerMenu = Menu(menubar, tearoff=0)
        registerMenu.add_command(label="Volunteers", command=self.openVolunteer)
        registerMenu.add_command(label="Supervisors", command=self.openSupervisor)

        menubar.add_cascade(label="New", menu=registerMenu)

        parent.config(menu=menubar)

    def openVolunteer(self):
        frame = volunteerForm(self.mainframe, root)

    def openSupervisor(self):
        frame = supervisorForm(self.mainframe, root)


global root
root = Tk()
mainFrame(root)

root.mainloop()
