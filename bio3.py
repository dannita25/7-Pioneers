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
label1 = Label (master, text ="Lisa Gelobter",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Computer Scientist\n(1971-Present)\nLisa Gelobter is a computer scientist and technology executive who has a long history of contributions to video technology on the web, including early contributions toward the now-ubiquitous Graphics Interchange Format (GIF). During her time at Adobe, Gelobter led the Shockwave and Flash Player product teams. Gelobter is currently the cofounder and CEO of Tequitable, a platform for employees to address issues of bias, discrimination, and harassment. She spent two years working at the White House as part of the newly formed United States Digital Service, where she helped design new digital services for people in education. She was also part of the founding team for the streaming service Hulu.',  font = "70",fg="white", bg="black")
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