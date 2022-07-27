import tkinter
from tkinter import *


window = tkinter.Tk()

label = tkinter.Label(window, text="Lista de deportes")
label.grid(column=0, row=0)
lista = ["Voleibol", "Baloncesto", "Futbol", "Natacion"]
listBox = tkinter.Listbox(window)

for i in lista:
    listBox.insert(END, i)

listBox.grid(column=0,row=1,pady=5,padx=5, sticky=tkinter.W)
window.mainloop()
