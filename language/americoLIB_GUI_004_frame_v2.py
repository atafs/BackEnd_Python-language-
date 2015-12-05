#!/usr/bin/python

#**************************
import tkinter as tk
from tkinter import messagebox

class Store:
    def __init__(self):
        self.variable = tk.IntVar()

    def add(self, value):
        var = self.variable
        var.set(var.get() + value)
        return var.get()

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        var = Store()
        self.label  = tk.Label(self, textvariable=var.variable)
        self.button = tk.Button(self, command=lambda: var.add(1), text='+1')
        self.label.pack()
        self.button.pack()


root = Main()
root.mainloop()

#**************************
#SUCCESS
print ("\nENDING APPLICATION!!")