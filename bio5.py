from tkinter import*
from tkinter.ttk import *
from ctypes.wintypes import WORD
from PIL import ImageTk, Image
from tkinter import BOTH, ttk
from tkinter.font import BOLD
import tkinter as tk


master = Tk() 
master.title("Biography")
master.geometry("500x400")
master.iconphoto(True, tk.PhotoImage(file='images\logo.png'))
master.config(bg='black')
label1 = Label (master, text ="Gladys Mae West",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Mathematician\n(1930-Present)\nGladys Mae West is an American mathematician who contributed to the creation of Global Positioning Systems (GPS) during her time at what is now the Naval Surface Warfare Center, part of the US Air Force. Through the 1970s and 1980s, West helped program an IBM 7030 “Stretch” computer to build a highly accurate geodetic model of Earth, which would later form a key part of an early version of GPS. ',  font = "70",fg="white", bg="black")
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