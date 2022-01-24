from tkinter import *
from tkinter import ttk
from tkinter import messagebox
global appName
import pandas as pd
class volunteerForm:
    def __init__(self, parent):


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

        ttk.Button(mainframe, text="Register",command=self.registerVolunteer).grid(column=3, row=3, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
    def registerVolunteer(self,*args):
        volunteer_data = pd.read_csv('data/volunteers.csv')
        if self.name.get() and self.email.get():
            name=self.name.get()
            email=self.email.get()
            try:
                year=int(self.year.get())
                print(volunteer_data)
                volunteer_data.loc[len(volunteer_data.index)] = [name, email, year]
                print(volunteer_data)
                volunteer_data.to_csv('data/volunteers.csv', index=False)
            except:
                messagebox.showinfo(message='Year is Invalid')

        else:
            messagebox.showinfo(message='Inputs are blank')
