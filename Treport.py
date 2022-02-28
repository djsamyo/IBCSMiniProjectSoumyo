import tkinter
from tkinter import ttk
from tkinter import messagebox
import numpy as np

global appName
import pandas as pd


class tReportForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title('Di@tech-Time-Wise Report')
        self.frame = ttk.Frame(parent, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)
        volunteerData = pd.read_csv('data/volunteers.csv')

        self.volunteer = tkinter.StringVar()
        volunteerDrop = ttk.Combobox(self.frame, textvariable=self.volunteer)
        volunteerDrop.grid(column=1, row=1, sticky=tkinter.W)
        volunteerNames = list(volunteerData['name'])
        volunteerID = list(volunteerData['id'])
        volunteers = []
        for i in range(len(volunteerID)):
            volunteerName = str(volunteerID[i]) + "-" + volunteerNames[i]
            volunteers.append(volunteerName)
        volunteerDrop['values'] = ('Lunch', 'All Day', 'Day Before')
        volunteerDrop.state(["readonly"])
        volunteerDrop.bind('<<ComboboxSelected>>', self.getActivities)
        #     self.email = tkinter.StringVar()
        ttk.Label(self.frame, text="Choose the Time:").grid(column=0, row=0, sticky=(tkinter.W, tkinter.E))
        self.activities = tkinter.StringVar()
        ttk.Label(self.frame, textvariable=self.activities).grid(column=1, row=2, sticky=tkinter.W)
        #     email_entry = ttk.Entry(self.frame, width=30, textvariable=self.email)
        #     email_entry.grid(column=1, row=1, columnspan=3)
        # ttk.Button(self.frame, text="Get Activities", command=self.assign).grid(column=2, row=3, sticky=tkinter.W)
        # for child in self.frame.winfo_children():
        #     child.grid_configure(padx=5, pady=5)

    def getActivities(self, *args):
        print("ok")
        activitiesData = pd.read_csv('data/activities.csv')
        volunteerAssignData = pd.read_csv('data/volunteersAssign.csv')
        volunteers = pd.read_csv('data/volunteers.csv')
        supervisors=pd.read_csv('data/supervisors.csv')
        time = self.volunteer.get()
        if time:
            row = activitiesData.loc[activitiesData['time'] == time]
            activitiesText = "Activities:\n"
            names = row['name'].tolist()
            location = row['location'].tolist()
            supervisorID = row['supervisorID'].tolist()
            activityID = row['id'].tolist()
            m = 1
            for i, j, k, l in zip(names, location, supervisorID, activityID):
                activitiesText = f"{activitiesText} {m}){i},Location-{j},Supervisor-{supervisors.iloc[k,1]}\n Volunteers:\n"
                for n in volunteerAssignData.iloc[l, 1:]:
                    activitiesText = f"{activitiesText} {volunteers.iloc[n, 1]}\n"
            self.activities.set(activitiesText)
