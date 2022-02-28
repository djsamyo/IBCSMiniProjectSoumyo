import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global appName
import pandas as pd


class attendanceForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        self.parent=parent
        root.title('Di@tech-Attendance')
        self.frame = ttk.Frame(parent, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        self.volunteer_data = pd.read_csv('data/volunteers.csv')
        self.volunteerName = self.volunteer_data['name'].tolist()
        self.volunteerID=self.volunteer_data['id'].tolist()

        self.activity_data = pd.read_csv('data/activities.csv')
        self.activity_dataID= self.activity_data['id'].tolist()
        self.activity_dataName= self.activity_data['name'].tolist()

        self.assignment_data=pd.read_csv('data/volunteersAssign.csv')
        activities=[]
        for i in self.assignment_data['activityID']:
            name=self.activity_dataName[self.activity_dataID.index(i)]
            activities.append(str(i)+"-"+name)
        self.activity=tkinter.StringVar()
        ttk.Label(self.frame, text="Choose the Activity:").grid(column=0, row=0, sticky=(tkinter.W, tkinter.E))
        activityDrop = ttk.Combobox(self.frame, textvariable=self.activity)
        activityDrop.grid(column=1, row=1, sticky=tkinter.W)
        activityDrop['values'] = tuple(activities)
        activityDrop.state(["readonly"])
        activityDrop.bind('<<ComboboxSelected>>', self.getActivities)

    #     for i in range(len(self.volunteerID)):
    #         name=str(self.volunteerName[i])
    #         id=str(self.volunteerID[i])
    #         print(i, self.volunteerID[i], self.volunteerName[i], self.supervisorCurrentActivity[i])
    #         currentActivity=self.supervisorCurrentActivity[i]
    #         if currentActivity == 'None':
    #             print(currentActivity)
    #             self.supervisorData.append(id+"-"+name)
    #     self.supervisorDataTuple = tuple(self.supervisorData)
    #     print(self.supervisorDataTuple)
    #     spec['values'] = self.supervisorDataTuple
    #     spec.state(["readonly"])
    #
    #     self.time = StringVar()
    #     radioButtonArray=['Lunch', 'All Day', 'Day Before']
    #     r=3
    #     ttk.Label(frame, text="Time:").grid(column=0, row=3, sticky=E)
    #     for i in radioButtonArray:
    #         ttk.Radiobutton(frame, text=i, variable=self.time, value=i).grid(column=1, row=r,sticky=W)
    #         r+=1
    #
    #     self.location = StringVar()
    #     ttk.Label(frame, text="Location :").grid(column=0, row=r+1, sticky=E)
    #     loc = ttk.Combobox(frame, textvariable=self.location)
    #     loc.grid(column=1, row=r+1, columnspan=3, sticky=W)
    #     loc['values'] = ('PE HALL', 'Presentation Hall', 'Quad', 'Hall Entrance', 'Lab')
    #     loc.state(["readonly"])
    #     # ttk.Label(frame, text="Year :").grid(column=0, row=2, sticky=E)
    #     # self.year = StringVar()
    #     # year = ttk.Combobox(frame, textvariable=self.year)
    #     # year.grid(column=1, row=2, columnspan=3)
    #     # year['values'] = (10, 11, 12)
    #     # year.state(["readonly"])
    #
    #     ttk.Button(frame, text="Register", command=self.registerVolunteer).grid(column=3, row=r+2, sticky=W)
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    #
    def getActivities(self,*args):
        r=0
        ttk.Label(self.frame, text="Choose the Activity:").grid(column=1, row=3, sticky=(tkinter.W, tkinter.E))
        self.checkFrame = ttk.Frame(self.frame, padding="3 3 12 12")
        self.checkFrame.grid(column=1, row=4, sticky=(N, W, E, S))

        activities_data = pd.read_csv('data/volunteersAssign.csv')
        volunteer_data=pd.read_csv('data/volunteers.csv')
        volunteer_data=volunteer_data['name'].tolist()
        activity=self.activity.get()
        activityID=int(activity.split("-")[0])
        volunteers=[]
        for i in range(1,6):
            volunteer=activities_data.iat[activityID,i]
            volunteerName=volunteer_data[volunteer]
            volunteers.append(volunteerName)
        r=1
        for i in volunteers:
            ttk.Checkbutton(self.checkFrame, text=i).grid(column=0, row=r, sticky=(tkinter.W, tkinter.E))
            r+=1
        ttk.Button(self.checkFrame, text="Register", command=self.takeAttendance).grid(column=3, row=r, sticky=W)

    def takeAttendance(self,*args):
        attendance=[]
        volunteers=[]
        for widget in self.checkFrame.winfo_children():
            if widget.state() == ("selected",):
                attendance.append("Present")
                volunteers.append(widget.cget("text"))
            elif widget.cget("text") != "Register":
                attendance.append("Absent")
                volunteers.append(widget.cget("text"))
        df = pd.DataFrame(attendance, index=volunteers, columns=['Attendance'])
        df.to_csv(f'attendance/{self.activity.get()}.csv')