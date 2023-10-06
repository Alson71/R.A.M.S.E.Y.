from tkinter import *


class RAMSEY:
    global tkWindow,boroughs,boroughDropdown,cuisineDropdown,boroughSpecificMenu 
    global cuisines
    
    tkWindow = Tk()
    tkWindow.geometry("1000x600")
    tkWindow.title("RAMSEY")
    tkWindow.resizable("False","False")
    
    
    boroughs = ["Manhattan","Queens","Staten Island","Bronx","Brooklyn"]
    
    
    var = StringVar()
    var.set("Borough")
    
    boroughDropdown = OptionMenu(tkWindow,var,*boroughs)
    boroughDropdown.place(x = 350,y = 100, height = 50, width = 100)
    
    
if __name__ == "__main__":
    tkWindow.mainloop()