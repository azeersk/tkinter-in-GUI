from tkinter import *
from tkinter.ttk import *
azeer = Tk()
Label(azeer, text = "enter your name").grid(row = 0,column = 0)
Label(azeer, text = "enter your age").grid(row = 1, column = 0)
#text input
a = Entry(azeer,width = 50).grid(row = 0, column = 1)
r = Entry(azeer,width = 50 ).grid(row = 1, column = 1)
#buttons
def on_click():
    print(F"my name is {a},and my age is {r}")

Button(azeer, text = "click me", command = on_click).grid(row = 2, column = 1)
Checkbutton(azeer,text = "keep me logind").grid(columnspan = 2)
ar = Combobox(azeer)
ar["values"] = (1,2,3,4,5,"Text")
ar.current(2)
ar.grid(row = 3, column = 3)
Radiobutton(azeer, text = "python ", value = 1).grid(row = 3, column = 1)

azeer.mainloop()
