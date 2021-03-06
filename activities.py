from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global appName
import pandas as pd


class activitiesForm:
    def __init__(self, parent, root):
        try:
            for widget in parent.winfo_children():
                widget.destroy()
        except:
            pass
        self.parent=parent
        root.title('Di@tech-Activity Registration')
        frame = ttk.Frame(parent, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(5, weight=1)

        self.name = StringVar()
        ttk.Label(frame, text="Name :").grid(column=0, row=0,sticky=E)
        name_entry = ttk.Entry(frame, width=30, textvariable=self.name)
        name_entry.grid(column=1, row=0, columnspan=3)

        self.supervisor = StringVar()
        ttk.Label(frame, text="Supervisor-In-Charge :").grid(column=0, row=2, sticky=E)
        spec = ttk.Combobox(frame, textvariable=self.supervisor)
        spec.grid(column=1, row=2, columnspan=3, sticky=W)
        self.supervisor_data = pd.read_csv('data/supervisors.csv')
        self.supervisorName = self.supervisor_data['name'].tolist()
        self.supervisorID=self.supervisor_data['id'].tolist()
        self.supervisorCurrentActivity=self.supervisor_data['currentActivity'].tolist()
        self.supervisorData=[]
        for i in range(len(self.supervisorID)):
            name=str(self.supervisorName[i])
            id=str(self.supervisorID[i])
            print(i,self.supervisorID[i],self.supervisorName[i],self.supervisorCurrentActivity[i])
            currentActivity=self.supervisorCurrentActivity[i]
            if currentActivity == 'None':
                print(currentActivity)
                self.supervisorData.append(id+"-"+name)
        self.supervisorDataTuple = tuple(self.supervisorData)
        print(self.supervisorDataTuple)
        spec['values'] = self.supervisorDataTuple
        spec.state(["readonly"])

        self.time = StringVar()
        radioButtonArray=['Lunch', 'All Day', 'Day Before']
        r=3
        ttk.Label(frame, text="Time:").grid(column=0, row=3, sticky=E)
        for i in radioButtonArray:
            ttk.Radiobutton(frame, text=i, variable=self.time, value=i).grid(column=1, row=r,sticky=W)
            r+=1

        self.location = StringVar()
        ttk.Label(frame, text="Location :").grid(column=0, row=r+1, sticky=E)
        loc = ttk.Combobox(frame, textvariable=self.location)
        loc.grid(column=1, row=r+1, columnspan=3, sticky=W)
        loc['values'] = ('PE HALL', 'Presentation Hall', 'Quad', 'Hall Entrance', 'Lab')
        loc.state(["readonly"])
        # ttk.Label(frame, text="Year :").grid(column=0, row=2, sticky=E)
        # self.year = StringVar()
        # year = ttk.Combobox(frame, textvariable=self.year)
        # year.grid(column=1, row=2, columnspan=3)
        # year['values'] = (10, 11, 12)
        # year.state(["readonly"])

        ttk.Button(frame, text="Register", command=self.registerVolunteer).grid(column=3, row=r+2, sticky=W)
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def registerVolunteer(self, *args):
        activities_data = pd.read_csv('data/activities.csv')
        if self.name.get():
            name = self.name.get()
            supervisor = self.supervisor.get()
            supervisor=supervisor.split("-")[0]
            time = self.time.get()
            location=self.location.get()
            #
            try:
                self.actid=len(activities_data.index)
                activities_data.loc[len(activities_data.index)] = [self.actid,name, location, time, supervisor]
                print(self.supervisor_data)
                activities_data.to_csv('data/activities.csv', index=False)
                self.supervisor_data.iat[int(supervisor),4]=name
                self.supervisor_data.to_csv('data/supervisors.csv',index=False)
                print(self.supervisor_data)
                assignData=pd.read_csv("data/volunteersAssign.csv")
                assignData.loc[len(assignData.index)] = [self.actid,"None","None","None","None","None"]
                assignData.to_csv('data/volunteersAssign.csv', index=False)
            except:
                messagebox.showinfo(message='Invalid Inputs')
            messagebox.showinfo(message='Registered Successfully')