# PROGRAM: tkinter APP
# Student Name      - DANNA SEQUEIROS HUILLCA
# Student Number    - EC1959192
# Date              - 25/04/2022


# This will import all the widgets

from tkinter import *
from tkinter.ttk import *
from ctypes.wintypes import WORD
from PIL import ImageTk, Image
from tkinter import BOTH, ttk
from tkinter.font import BOLD
import tkinter as tk
from cProfile import label

# creates a Tk() object
master = tk.Tk()
 
# sets the geometry of main root window
master.geometry("1500x700")
master.iconphoto(True, tk.PhotoImage(file='images\logo.png'))
master.title("Danna's App")
master.config(bg='black')


def new_window():
    master.destroy()
    import bio1

def new_window2():
    master.destroy()
    import bio2

def new_window3():
    master.destroy()
    import bio3
    
def new_window4():
    master.destroy()
    import bio4

def new_window5():
    master.destroy()
    import bio5

def new_window6():
    master.destroy()
    import bio6

def new_window7():
    master.destroy()
    import bio7


 
label =Label(master, text ="7 TECH PIONEERS", font=("sans-serif", 30, BOLD))
label.pack(side = TOP, pady = 10)

msg = Message(master, text="To celebrate Black History and to educate ourselves on technologists who have led, and continue to lead the way for future generations — we share 7 Pioneers of Tech. Among these names you might find familiar ones, whose life stories are even on famous movies. Sadly, many of these names have been overshadowed. In fact, many of these pioneers have impacted the field of technology in ways that affect you every day. We hope our brief highlights of each person inspires you to learn more about them and how their work changed the world.", font=("sans-serif", 15), fg="white", bg="black", width=1200)
msg.config(justify="center")
msg.pack(fill=BOTH)

photo = PhotoImage(file = r"images\marianp.png")
photo_2 = PhotoImage(file = r"images\clarencep.png")
photo_3 = PhotoImage(file = r"images\lisap.png")
photo_4 = PhotoImage(file = r"images\markp.png")
photo_5 = PhotoImage(file = r"images\gladysp.png")
photo_6 = PhotoImage(file = r"images\otisp.png")
photo_7 = PhotoImage(file = r"images\melbap.png")


# buttons widget which will open new windows on button clicks
Button(
    master, 
    text ='Marian Croak', 
    image = photo, 
    compound=BOTTOM,
    command=new_window
).pack(fill=X, expand=True, side=LEFT) 



Button(
    master, 
    text ='Clarence Ellis', 
    image = photo_2, 
    compound=BOTTOM,
    command=new_window2
).pack(fill=X, expand=True, side=LEFT)



Button(
    master, 
    text ='Lisa Gelobter', 
    image = photo_3, 
    compound=BOTTOM,
    command=new_window3
).pack(fill=X, expand=True, side=LEFT)

Button(
    master, 
    text ='Mark Dean', 
    image = photo_4, 
    compound=BOTTOM,
    command=new_window4,
).pack(side=LEFT) 

Button(
    master, 
    text ='Gladys Mae West', 
    image = photo_5, 
    compound=BOTTOM,
    command=new_window5
).pack(fill=X, expand=True, side=LEFT)

Button(
    master, 
    text ='Otis Boykin', 
    image = photo_6, 
    compound=BOTTOM,
    command=new_window6
).pack(fill=X, expand=True, side=LEFT)

Button(
    master, 
    text ='Melba Roy Mouton', 
    image = photo_7, 
    compound=BOTTOM,
    command=new_window7
).pack(fill=X, expand=True, side=LEFT)      
 

# mainloop, runs infinitely
master.mainloop()