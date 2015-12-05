#!/usr/bin/python

#**************************
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self,master):
        self.var = tk.IntVar()
        frame = tk.Frame(master)
        frame.grid()
        f2 = tk.Frame(master,width=200,height=100)
        f2.grid(row=0,column=1)
        button = tk.Checkbutton(frame,text='show',variable=self.var,command=self.fx)
        button.grid(row=0,column=0)
        msg2="""I feel bound to give them full satisfaction on this point"""
        self.v= tk.Message(f2,text=msg2)
    
    def fx(self):
        if self.var.get():
            self.v.grid(column=1,row=0,sticky=N)
        else:
            self.v.grid_remove()

top = tk.Tk()
app = App(top)            
top.mainloop()

#**************************
#SUCCESS
print ("\nENDING APPLICATION!!")