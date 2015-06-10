#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:57:17 2015

@author: Pendan
"""

import telnetlib
import os
import Tkinter
import subprocess


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)


        button = Tkinter.Button(self,text=u"Get Server Version",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="gray")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u" ")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        HOST = self.entryVariable.get()

        proc = subprocess.Popen(["curl -s -I '"+HOST+"'"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        for item in out.split("\n"):
            if "Server:" in item:
             self.labelVariable.set(item.strip())
             self.entry.focus_set()
             self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( " " )
        HOST = self.entryVariable.get()

        proc = subprocess.Popen(["curl -s -I '"+HOST+"'"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        for item in out.split("\n"):
            if "Server:" in item:
             self.labelVariable.set(item.strip())
             self.entry.focus_set()
             self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('ServerPy')
    app.mainloop()

    


