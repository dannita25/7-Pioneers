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
label1 = Label (master, text ="Melba Roy Mouton",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Mathematician and Computer programmer\n(1929-1990)\nLike Katherine Johnson, Melba Roy Mouton was another great Black leader in tech for her important work as a “human computer” at NASA. She eventually made her way to being Head of Computer Programming at NASA, and then took on a role as Program Production Section Chief at Goddard Space Flight Center. Her work helped produce the orbital element timetables which allowed millions to see the satellite from Earth as it passed overhead. She received an Apollo Achievement Award and an Exceptional Performance Award while at NASA.',  font = "70",fg="white", bg="black")
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