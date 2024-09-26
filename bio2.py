from tkinter import*
from tkinter.ttk import *
from ctypes.wintypes import WORD
from PIL import ImageTk, Image
from tkinter import BOTH, ttk
from tkinter.font import BOLD
import tkinter as tk


master = Tk() 
master.title("Biography")
master.geometry("500x500")
master.iconphoto(True, tk.PhotoImage(file='images\logo.png'))
master.config(bg='black')
label1 = Label (master, text ="Clarence Ellis",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Computer Scientist\n(1943-2014)\nClarence “Skip” Ellis was one of few African-Americans to walk the halls of the now-legendary Xerox PARC in the 1970s and 1980s, where he was part of the team that developed early display software, object-oriented programming languages, and OfficeTalk, an early groupware system that paved the way for today’s collaboration software. “Using the Alto and Dorado machines, and the Cedar database and programming environment, we have devised a system that allows the flexible manipulation of electronic forms on the display screen of users and helps to coordinate and control the flow of forms between user workstations,” said the original OfficeTalk notes from 1982, coauthored by Ellis. ',  font = "70",fg="white", bg="black")
msg.config(justify="center")
msg.pack()


def first_window():
    master.destroy()
    import tech_main

Button(
    master, 
    text ='BACK TO MAIN WINDOW', 
    command=first_window
).pack(side=BOTTOM, pady=5) 

master.mainloop()