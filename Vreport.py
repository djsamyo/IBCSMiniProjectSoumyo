import tkinter
from tkinter import ttk
from tkinter import messagebox
import numpy as np

global appName
import pandas as pd


class vReportForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title('Di@tech-Volunteer-Wise Report')
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
        volunteerDrop['values'] = tuple(volunteers)
        volunteerDrop.state(["readonly"])
        volunteerDrop.bind('<<ComboboxSelected>>', self.getActivities)
        #     self.email = tkinter.StringVar()
        ttk.Label(self.frame, text="Choose the Volunteer:").grid(column=0, row=0, sticky=(tkinter.W, tkinter.E))
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
        assignData = pd.read_csv('data/volunteersAssign.csv')
        volunteer = self.volunteer.get()
        if volunteer:
            volunteerID = int(volunteer.split('-')[0])
            volunteerID = int(volunteerID)
            row1 = assignData.loc[assignData['student1'] == volunteerID]['activityID'].tolist()
            row2 = assignData.loc[assignData['student2'] == volunteerID]['activityID'].tolist()
            row3 = assignData.loc[assignData['student3'] == volunteerID]['activityID'].tolist()
            row4 = assignData.loc[assignData['student4'] == volunteerID]['activityID'].tolist()
            row5 = assignData.loc[assignData['student5'] == volunteerID]['activityID'].tolist()
            activities = sorted(np.unique(row5 + row4 + row2 + row3 + row1))
            activitiesText = "Activities:\n"
            nameData = activitiesData.loc[activities, 'name'].tolist()
            locationData = activitiesData.loc[activities, 'location'].tolist()
            timeData = activitiesData.loc[activities, 'time'].tolist()
            combinedList = zip(nameData, locationData, timeData)
            print(combinedList)
            l=1
            for i, j, k in combinedList:
                activitiesText = f"{activitiesText}{l}) {i}- Location:{j}, Time:{k} \n"
                l+=1
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
