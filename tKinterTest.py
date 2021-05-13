from tkinter import *
import random 

top = Tk()
playList = []
myRolls = []
rollTimes = 0
dieType = 0

def results():
    print(playList)

def export():
    with open("test.txt", "w") as f:
        for item in playList:
            f.write("%s\n" % item)
def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 2, row = 1)

    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 2, row = 2)

    B2Main = Button(text = "Week 2", bg = "white", command = week2)
    B2Main.grid(column = 2, row = 3)

    B3Main = Button(text = "Week 3", bg = "white", command = week3)
    B3Main.grid(column = 2, row = 4)

def week1():
    def add():
        newItem = E1.get()
        playList.append(newItem)
        E1.delete(0, END)

    clearWindow()

    #This is a label widget
    L1 = Label(top, text = "Playlist Maker")
    L1.grid(column = 0, row = 1)

    #This is an entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #button widgets
    B1 = Button(text = "   Print Playlist   ", bg = "#c6edee", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = "Add", bg = "#feebe5", command = add)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "  export list  ", bg = "#ceb0af" ,command = export)
    B3.grid(column = 0, row = 5)

    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 3, row = 1)

def week2():
    def rollDice():
        #update variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        #clear window after pulling entry data
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #diplay dice rolls and present an exit button
        L4W2 = Label(top, text = "Your Rolls")
        L4W2.grid(column = 0, row = 1)
        
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text = "main menu", bg = "yellow", command = mainMenu)
        B2W2.grid(column = 0, row = 3)
    
    clearWindow()
    
    L1W2 = Label(top, text = "Dice Rollaer Program")
    L1W2.grid(column = 0, row = 1)
    
    L2W2 = Label(top, text = "How many sides")
    L2W2.grid(column = 0, row = 2)

    L3W2= Label(top, text = "How many rolls")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)
    
    B1W2 = Button(text = "roll", bg = "yellow", command = rollDice)
    B1W2.grid(column = 2, row = 4)
#to add: roll funciton and exit button

def week3():
    print("we're not here yet")

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
