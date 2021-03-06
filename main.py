from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from supervisors import supervisorForm
from volunteer import volunteerForm
from activities import activitiesForm
from assignVolunteers import assignForm
from Vreport import vReportForm
from Areport import aReportForm
from Treport import tReportForm
from attendance import attendanceForm
global appName


class mainFrame():
    def __init__(self, parent):
        self.mainframe = ttk.Frame(parent, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        menubar = Menu(root)

        registerMenu = Menu(menubar, tearoff=0)
        registerMenu.add_command(label="Volunteer", command=self.openVolunteer)
        registerMenu.add_command(label="Supervisor", command=self.openSupervisor)
        registerMenu.add_command(label="Activity", command=self.openActivity)
        menubar.add_cascade(label="New", menu=registerMenu)

        assignMenu = Menu(menubar, tearoff=0)
        assignMenu.add_command(label="Volunteers", command=self.openAssign)
        menubar.add_cascade(label="Assign", menu=assignMenu)
        parent.config(menu=menubar)

        reportMenu = Menu(menubar, tearoff=0)
        reportMenu.add_command(label="By Volunteer", command=self.openVreport)
        reportMenu.add_command(label="By Activity", command=self.openAreport)
        reportMenu.add_command(label="By Time", command=self.openTreport)
        menubar.add_cascade(label="Reports", menu=reportMenu)
        parent.config(menu=menubar)

        attendanceMenu = Menu(menubar, tearoff=0)
        attendanceMenu.add_command(label="Check Attendance", command=self.openattendanceForm)
        menubar.add_cascade(label="Check Attendance", menu=attendanceMenu)
        parent.config(menu=menubar)

    def openVolunteer(self):
        frame = volunteerForm(self.mainframe, root)

    def openSupervisor(self):
        frame = supervisorForm(self.mainframe, root)

    def openActivity(self):
        frame = activitiesForm(self.mainframe, root)

    def openAssign(self):
        frame = assignForm(self.mainframe, root)

    def openVreport(self):
        frame= vReportForm(self.mainframe, root)

    def openAreport(self):
        frame= aReportForm(self.mainframe, root)

    def openTreport(self):
        frame= tReportForm(self.mainframe,root)

    def openattendanceForm(self):
        frame=attendanceForm(self.mainframe,root)

global root
root = Tk()
mainFrame(root)

root.mainloop()
