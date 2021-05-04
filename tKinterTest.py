from tkinter import *

top = Tk()
groceryList = []

def results():
    print(groceryList)

def add():
    newItem = E1.get()
    groceryList.append(newItem)

#This is a label widget
L1 = Label(top, text = "Grocery List")
L1.grid(column= 0, row= 1)

#This is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#button widget
B2 = Button(text = "Add", bg = "cyan", command = add)
B2.grid(column = 1, row = 2)

#button widget
B1 = Button(text = "   Print List   ", bg = "#fce0de", command = results)
B1.grid(column = 0, row = 3)


top.mainloop()
