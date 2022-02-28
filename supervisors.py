from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global appName
import pandas as pd


class supervisorForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title("Di@tech-Supervisor Registration")
        frame = ttk.Frame(parent, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)

        self.name = StringVar()
        ttk.Label(frame, text="Name :").grid(column=0, row=0, sticky=E)
        name_entry = ttk.Entry(frame, width=30, textvariable=self.name)
        name_entry.grid(column=1, row=0, columnspan=3)

        self.email = StringVar()
        ttk.Label(frame, text="Email :").grid(column=0, row=1, sticky=E)
        email_entry = ttk.Entry(frame, width=30, textvariable=self.email)
        email_entry.grid(column=1, row=1, columnspan=3)

        self.spec = StringVar()
        ttk.Label(frame, text="Specialization :").grid(column=0, row=2, sticky=E)
        spec = ttk.Combobox(frame, textvariable=self.spec)
        spec.grid(column=1, row=2, columnspan=3, sticky=W)
        spec['values'] = ("Teacher", "Assistant", "Club Member")
        spec.state(["readonly"])
        # self.year = StringVar()
        # ttk.Label(frame, text="Year :").grid(column=0, row=2, sticky=E)
        # year_entry = ttk.Entry(frame, width=30, textvariable=self.year)
        # year_entry.grid(column=1, row=2, columnspan=3)

        ttk.Button(frame, text="Register", command=self.registerVolunteer).grid(column=3, row=3, sticky=W)
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def registerVolunteer(self, *args):
        volunteer_data = pd.read_csv('data/supervisors.csv')
        print(volunteer_data)
        if self.name.get() and self.email.get():
            name = self.name.get()
            email = self.email.get()
            spec = self.spec.get()
            volunteer_data.loc[len(volunteer_data.index)] = [len(volunteer_data.index), name, email, spec, 'None']
            print(volunteer_data)
            volunteer_data.to_csv('data/supervisors.csv', index=False)
            messagebox.showinfo(message='Registered Successfully')
        else:
            messagebox.showinfo(message='Please Enter Valid Inputs')

