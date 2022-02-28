import tkinter
from tkinter import ttk
from tkinter import messagebox
import numpy as np

global appName
import pandas as pd


class aReportForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title('Di@tech-Activity-Wise Report')
        self.frame = ttk.Frame(parent, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)

        activitiesData = pd.read_csv('data/activities.csv')

        self.activity = tkinter.StringVar()
        activityDrop = ttk.Combobox(self.frame, textvariable=self.activity)
        activityDrop.grid(column=1, row=1, sticky=tkinter.W)
        activityNames = list(activitiesData['name'])
        activityID = list(activitiesData['id'])
        activities = []
        for i in range(len(activityID)):
            volunteerName = str(activityID[i]) + "-" + activityNames[i]
            activities.append(volunteerName)
        activityDrop['values'] = tuple(activities)
        activityDrop.state(["readonly"])
        activityDrop.bind('<<ComboboxSelected>>', self.getActivities)
        #     self.email = tkinter.StringVar()
        ttk.Label(self.frame, text="Choose the Activity:").grid(column=0, row=0, sticky=(tkinter.W, tkinter.E))
        self.activities = tkinter.StringVar()
        ttk.Label(self.frame, textvariable=self.activities).grid(column=1, row=2, sticky=tkinter.W)
        #     email_entry = ttk.Entry(self.frame, width=30, textvariable=self.email)
        #     email_entry.grid(column=1, row=1, columnspan=3)
        # ttk.Button(self.frame, text="Get Activities", command=self.assign).grid(column=2, row=3, sticky=tkinter.W)
        # for child in self.frame.winfo_children():
        #     child.grid_configure(padx=5, pady=5)

    def getActivities(self, *args):
        print("ok")
        volunteerData = pd.read_csv('data/volunteers.csv')
        assignData = pd.read_csv('data/volunteersAssign.csv')
        activity = int(self.activity.get().split('-')[0])
        activitiesText="Volunteers for this Activity Are: \n"
        for i in assignData.iloc[activity,1:].tolist():
            activitiesText = str(activitiesText+volunteerData.at[i,'name'] + "\n")
            self.activities.set(activitiesText)
            # def registerVolunteer(self, *args):
    #     volunteer_data = pd.read_csv('data/volunteers.csv')
    #     if self.name.get() and self.email.get():
    #         name = self.name.get()
    #         email = self.email.get()
    #         try:
    #             year = int(self.year.get())
    #             print(volunteer_data)
    #             volunteer_data.loc[len(volunteer_data.index)] = [len(volunteer_data.index),name, email, year]
    #             print(volunteer_data)
    #             volunteer_data.to_csv('data/volunteers.csv', index=False)
    #         except:
    #             messagebox.showinfo(message='Year is Invalid')
    #         messagebox.showinfo(message='Registered Successfully')
    #     else:
    #         messagebox.showinfo(message='Please Enter Valid Inputs')
