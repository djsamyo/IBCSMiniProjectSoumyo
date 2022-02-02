from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global appName
import pandas as pd


class volunteerForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title('Di@tech-Volunteer Registration')
        frame = ttk.Frame(parent, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)

        self.name = StringVar()
        ttk.Label(frame, text="Name :").grid(column=0, row=0)
        name_entry = ttk.Entry(frame, width=30, textvariable=self.name)
        name_entry.grid(column=1, row=0, columnspan=3)

        self.email = StringVar()
        ttk.Label(frame, text="Email :").grid(column=0, row=1, sticky=E)
        email_entry = ttk.Entry(frame, width=30, textvariable=self.email)
        email_entry.grid(column=1, row=1, columnspan=3)

        ttk.Label(frame, text="Year :").grid(column=0, row=2, sticky=E)
        self.year = StringVar()
        year = ttk.Combobox(frame, textvariable=self.year)
        year.grid(column=1, row=2, columnspan=3)
        year['values'] = (10, 11, 12)
        year.state(["readonly"])

        ttk.Button(frame, text="Register", command=self.registerVolunteer).grid(column=3, row=3, sticky=W)
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def registerVolunteer(self, *args):
        volunteer_data = pd.read_csv('data/volunteers.csv')
        if self.name.get() and self.email.get():
            name = self.name.get()
            email = self.email.get()
            try:
                year = int(self.year.get())
                print(volunteer_data)
                volunteer_data.loc[len(volunteer_data.index)] = [len(volunteer_data.index),name, email, year]
                print(volunteer_data)
                volunteer_data.to_csv('data/volunteers.csv', index=False)
            except:
                messagebox.showinfo(message='Year is Invalid')

        else:
            messagebox.showinfo(message='Please Enter Valid Inputs')
