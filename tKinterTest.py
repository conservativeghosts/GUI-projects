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
        top.geometry('250x200+250+200')
        L4W2 = Label(top, text = "Your Rolls:")
        L4W2.place(x=5, y=0)
        
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.place(x=30, y=15)
        
        B2W2 = Button(text = "main menu", bg = "yellow", command = mainMenu)
        B2W2.place(x=5, y=45)
    
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
    def searchDie():

        clearWindow()

        L1D = Label(top, text = "what number are you looking for?")
        L1D.grid(column = 0, row = 0)

        E1D = Entry(top, bd = 5)
        E1D.grid(column = 0, row = 1)

        B1D = Button(text = "search", bg = "green", command = pain)
        B1D.grid(column = 1, row = 1)
        
        E1D.delete(0, END)
        numLook = E1D.get()
        """ okay here's the thing I know what's wrong and how to fix it ieally,
I just don't have any idea how to fix it in practice.
Basically, because "numLook" isn't universally defined and it is defed in a funcition
that it is called in, basically no workie. I have numLook defed in a different function
becuse that function is were you get the entry data required, but becuse it is there and
not under pain when I call the variable the pain function breaks becuse it doesn't have a
value, IDk how to fix this. :(
"""

    def pain():
        result = binDie(myRolls, int(numLook))
                
        if result != -1:
            L2D = Label(top, text = "your number is at index postition {}".format(result))

        else:
            L3D = Label(top, text = "the number you are looking for is not here")

            
    def binDie(myRolls, x):
        low = 0
        high = len(myRolls)-1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if myRolls[mid] < x:
                low = mid + 1
            elif myRolls[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
        
    def searchPlay():
        clearWindow()

        L1P = Label(top, text = "what number are you looking for?")
        L1P.grid(column = 0, row = 0)

        E1P = Entry(top, bd = 5)
        E1P.grid(column = 0, row = 1)

        B1P = Button(text = "search", bg = "green", command = pain2)
        B1P.grid(column = 1, row = 1)
        
        E1P.delete(0, END)
        numLook2 = E1P.get()
    def pain2():
        result = binPlay(playList, int(numLook2))
                
        if result != -1:
            L2P = Label(top, text = "your song is at index position {}".format(result))

        else:
            L3P = Label(top, text = "the song you are looking for is not here")

    def binPlay (playList, x):
        low = 0
        high = len(playList)-1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if playList[mid] < x:
                low = mid + 1
            elif playList[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
        
    clearWindow()

    L2W3 = Label(top, text = "before you can run this function please make sure you have ran the first two.")
    L2W3.grid(column = 0, row = 0)
        
    L1W3 = Label(top, text = "Searching for things...")
    L1W3.grid(column = 0, row = 1)

    L2W3 = Label(top, text = "Which list would you like to search?")
    L2W3.grid(column = 0, row = 2)

    B1W3 = Button(text = "Playlist", bg = "green", command = searchPlay)
    B1W3.grid(column = 0, row = 3)

    B2W3 = Button(text = "Die rolls", bg = "orange", command = searchDie)
    B2W3.grid(column = 1, row = 3)

    B3W3 = Button(text = "Main Menu", bg = "yellow", command = mainMenu)
    B3W3.grid(column = 1, row = 0)
            

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
