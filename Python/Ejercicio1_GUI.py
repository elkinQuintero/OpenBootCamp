import tkinter
from tkinter import *
from tkinter import ttk

from setuptools import Command

def seleccionar():
    opcion.config(text="{}".format(sportSelect.get()))
def reset():
    sportSelect.set(None)
    opcion.config(text="")

window = tkinter.Tk()

sportSelect = tkinter.StringVar()
sportSelect.set(None)
r1=ttk.Radiobutton(window, text="Futbol", value="Futbol", variable=sportSelect, command=seleccionar)
r2=ttk.Radiobutton(window, text="Baloncesto", value="Baloncesto", variable=sportSelect, command=seleccionar)
r3=ttk.Radiobutton(window, text="Voleibol", value="Voleibol", variable=sportSelect, command=seleccionar)
r4=ttk.Radiobutton(window, text="Natación", value="Natacion", variable=sportSelect, command=seleccionar)

r1.grid(column=0,row=0,pady=5,padx=5, sticky=tkinter.W)
r2.grid(column=0,row=1,pady=5,padx=5, sticky=tkinter.W)
r3.grid(column=0,row=2,pady=5,padx=5, sticky=tkinter.W)
r4.grid(column=0,row=3,pady=5,padx=5, sticky=tkinter.W)

opcion = ttk.Label(window)
opcion.grid(column=0,row=4,pady=5,padx=5, sticky=tkinter.W)
b1 = ttk.Button(window, text="Reiniciar", command=reset)
b1.grid(column=0,row=5,pady=5,padx=5, sticky=tkinter.W)

window.mainloop()

