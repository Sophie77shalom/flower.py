from tkinter import *
from tkinter.ttk import*

from time import strftime
root=Tk()
root.title("clock")
def time():
    string=strftime("%H:%M:%S %P")
    label.config(text=string)
    label.after(1000, time)

label=Label(root, font=("ds-digital",80), background="black", foreground="cyan")
label.pack(achor="centre")
time()

mainloop()