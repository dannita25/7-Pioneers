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
label1 = Label (master, text ="Otis Boykin",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Electrical engineer and Inventor\n(1920-1982)\nOtis Boykin was another prolific inventor, eventually holding 26 patents. After graduating from Fisk College in 1941, he began working with the Majestic Radio and TV Corporation and eventually P.J. Nilsen Research Laboratories. Among his inventions were a wire precision resistor used in televisions, radios, IBM computers, and even in military missiles. He also invented a control unit for the pacemaker. Boykin helped improve and make everyday electronics more efficient and affordable.',  
font = "70",fg="white", bg="black")
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