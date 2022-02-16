import tkinter
from tkinter import ttk
from tkinter import messagebox

global appName
import pandas as pd


class assignForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        root.title('Di@tech-Volunteer Assignment')
        frame = ttk.Frame(parent, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)
        volunteerData=pd.read_csv('data/volunteers.csv')
        activitiesData=pd.read_csv('data/activities.csv')

        self.activity = tkinter.StringVar()
        activityDrop = ttk.Combobox(frame, textvariable=self.activity)
        activityDrop.grid(column=0, row=1, sticky=tkinter.W)
        activitiesName=list(activitiesData['name'])
        activitiesID=list(activitiesData['id'])
        activities=[]
        print(activitiesName)
        print(activitiesID)
        for i in range(len(activitiesID)):
            activityName=str(activitiesID[i])+"-"+activitiesName[i]
            activities.append(activityName)
        activityDrop['values'] = tuple(activities)
        activityDrop.state(["readonly"])

        self.volunteer = tkinter.StringVar()
        volunteerDrop = ttk.Combobox(frame, textvariable=self.volunteer)
        volunteerDrop.grid(column=1, row=1, sticky=tkinter.W)
        volunteerNames = list(volunteerData['name'])
        volunteerID = list(volunteerData['id'])
        volunteers = []
        for i in range(len(volunteerID)):
            volunteerName = str(volunteerID[i]) + "-" + volunteerNames[i]
            volunteers.append(volunteerName)
        volunteerDrop['values'] = tuple(volunteers)
        volunteerDrop.state(["readonly"])

    #     self.email = tkinter.StringVar()
        ttk.Label(frame, text="Activity:").grid(column=0, row=0, sticky=(tkinter.W,tkinter.E))
        ttk.Label(frame, text="Volunteer to Assign:").grid(column=1, row=0, sticky=(tkinter.W,tkinter.E))
    #     email_entry = ttk.Entry(frame, width=30, textvariable=self.email)
    #     email_entry.grid(column=1, row=1, columnspan=3)
    #
        # ttk.Label(frame, text="Year :").grid(column=0, row=2, sticky=tkinter.E)
    #     self.year = tkinter.StringVar()
    #     year = ttk.Combobox(frame, textvariable=self.year)
    #     year.grid(column=1, row=2, columnspan=3)
    #     year['values'] = (10, 11, 12)
    #     year.state(["readonly"])
    #
        ttk.Button(frame, text="Assign", command=self.assign).grid(column=2, row=3, sticky=tkinter.W)
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    def assign(self):
        assignData = pd.read_csv('data/volunteersAssign.csv')
        volunteer=self.volunteer.get()
        activity=self.activity.get()
        activity = int(activity.split('-')[0])
        if assignData.at[activity,'student1']=='None':
            assignData.at[activity, 'student1']=volunteer.split("-")[0]
        if assignData.at[activity,'student2']=='None':
            assignData.at[activity, 'student2']=volunteer.split("-")[0]
        if assignData.at[activity,'student3']=='None':
            assignData.at[activity, 'student3']=volunteer.split("-")[0]
        if assignData.at[activity,'student4']=='None':
            assignData.at[activity, 'student4']=volunteer.split("-")[0]
        if assignData.at[activity,'student5']=='None':
            assignData.at[activity, 'student5']=volunteer.split("-")[0]
        assignData.to_csv('data/volunteersAssign.csv',index=False)

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
