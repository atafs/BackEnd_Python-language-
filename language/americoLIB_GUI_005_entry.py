#!/usr/bin/python

#**************************
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
L1 = tk.Label(top, text="User Name")
L1.pack( side = tk.LEFT)
E1 = tk.Entry(top, bd =5)

E1.pack(side = tk.RIGHT)

top.mainloop()

#**************************
#SUCCESS
print ("\nENDING APPLICATION!!")