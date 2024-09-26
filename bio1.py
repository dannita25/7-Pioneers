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
label1 = Label (master, text ="Marian Croak",font=("sans-serif", 20, BOLD))
label1.pack(side = TOP, pady = 5)      
                
msg = Message(master, text='Inventor in the voice and data communication fields\n(1957-Present)\nMarian Croak has been in technology for 35 years and currently works at Google as vice president of site reliability engineering for ads, corporate engineering, and YouTube. Her crowning achievement was contributing to the invention of the Voice over IP (VoIP) protocol in the 1990s. Still in use today, VoIP allows voice communications and multimedia to be transmitted over Internet Protocol (IP) networks instead of over traditional telephone networks. Anyone who has taken part in a Zoom call recently will have come into contact with VoIP technology in some form.',  font = "70",fg="white", bg="black")
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