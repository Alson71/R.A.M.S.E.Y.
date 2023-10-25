from tkinter import *
import customtkinter


class RAMSEY:
    global tkWindow,boroughs,boroughDropdown,cuisineDropdown,boroughSpecificMenu 
    global cuisines,cuisines2,brooklynAreas,manhattanAreas,queensAreas,bronxAreas,statenAreas
    
    customtkinter.set_appearance_mode("dark")
    tkWindow = customtkinter.CTk()
    tkWindow.geometry("1000x600")
    tkWindow.title("RAMSEY")
    tkWindow.resizable("False","False")
    
    
    boroughs = ["Manhattan","Queens","Staten Island","Bronx","Brooklyn"]
    cuisines = ["American","Indian","Chinese","Japanese","Greek","Mexican","French","Peruvian","Korean","Thai"]
    
    
    
    
    var = StringVar()
    var.set("Borough")
    
    boroughDropdown = customtkinter.CTkOptionMenu(tkWindow,variable = var,values = boroughs,height = 50, width = 100)
    boroughDropdown.place(x = 430,y = 100)
    
    
if __name__ == "__main__":
    tkWindow.mainloop()
