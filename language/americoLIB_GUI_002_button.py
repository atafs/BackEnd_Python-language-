#!/usr/bin/python

#**************************
import tkinter as tk
from tkinter import messagebox

#GUI
top = tk.Tk()
top.height

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World", icon="warning")

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

#**************************
#SUCCESS
print ("\nENDING APPLICATION!!")