from tkinter import*
from tkinter.ttk import *
from ctypes.wintypes import WORD
from PIL import ImageTk, Image
from tkinter import BOTH, ttk
from tkinter.font import BOLD
import tkinter as tk


master = Tk() 
master.title("Biography")
master.geometry("600x500")
master.iconphoto(True, tk.PhotoImage(file='images\logo.png'))
master.config(bg='black')
label1 = Label (master, text ="Mark Dean",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 10)      
                
msg = Message(master, text='Computer Scientist and Inventor\n(1957-Present)\nBorn in Tennessee in 1957, Mark Dean is a computer scientist, professor, and inventor who was central to the creation of the personal computer. During his long career at IBM, between 1979 and 2013, Dean worked on the team responsible for bus control systems, including what became the Industry Standard Architecture (ISA) that allowed early computers to communicate with external devices. Dean also holds other key patents related to early models of the IBM PC, released in 1981. He became the first Black IBM Fellow when he was appointed to the position in 1995. Today Dean is an emeritus professor in the Min H. Kao Department of Electrical Engineering and Computer Science at the University of Tennessee.',  font = "70",fg="white", bg="black")
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