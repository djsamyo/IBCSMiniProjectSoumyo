from tkinter import *
from tkinter import ttk
global appName
import pandas as pd
appName = "Di@Tech-"

class mainFrame():
    def __init__(self,parent):
        global mainframe
        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
class volunteerForm:
    def __init__(self, parent):

        root.title(appName+"New Volunteer Sign Up")
        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)

        self.name=StringVar()
        ttk.Label(mainframe, text="Name :").grid(column=0, row=0)
        name_entry = ttk.Entry(mainframe, width=30, textvariable=self.name)
        name_entry.grid(column=1, row=0, columnspan=3)

        self.email=StringVar()
        ttk.Label(mainframe, text="Email :").grid(column=0, row=1, sticky=E)
        email_entry = ttk.Entry(mainframe, width=30,textvariable=self.email)
        email_entry.grid(column=1, row=1, columnspan=3)

        self.year=StringVar()
        ttk.Label(mainframe, text="Year :").grid(column=0, row=2, sticky=E)
        year_entry = ttk.Entry(mainframe, width=30,textvariable=self.year)
        year_entry.grid(column=1, row=2,  columnspan=3)

        errmsg=StringVar()
        ttk.Label(mainframe, textvariable=errmsg).grid(column=2, row=3)
        ttk.Button(mainframe, text="Register",command=self.registerVolunteer).grid(column=3, row=3, sticky=W)
        errmsg='error'

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
    def registerVolunteer(self,*args):
        volunteer_data = pd.read_csv('data/volunteers.csv')
        name=self.name.get()
        email=self.email.get()
        year=int(self.year.get())
        print(volunteer_data)
        volunteer_data.loc[len(volunteer_data.index)] = [name,email,year]
        print(volunteer_data)
        volunteer_data.to_csv('data/volunteers.csv',index=False)

global root
root = Tk()
mainFrame(root)
volunteerForm(mainframe)
root.mainloop()

