from tkinter import *
import PIL.Image
from PIL import ImageTk
import customtkinter
import requests


class RAMSEY:
    global tkWindow,parameters,dropdowns
    global cuisines,cuisines2,areas
    global labels, options, vars, temp
    
    #To keep track of the option for area in "enableArea" method
    temp = ""
    
    
    #Areas for each borough
    areas = [None] * 5
    areas[0] = ["Upper East Side", "Upper West Side", "Midtown", "Greenwich", "East Village"]
    areas[1] = ["Long Island City", "Astoria", "Forest Hills", "Queens Village", "Kew Gardens"]
    areas[2] = ["Riverdale", "Morris Park", "Parkchester", "Pelham Bay", "Fordham"]
    areas[3] = ["Brooklyn Heights", "DUMBO", "Prospect Heights", "Coney Island", "Flatbush"]
    areas[4] = ["West Brighton", "St. George", "Fort Wadsworth", "Charleston", "Dongan Hills"]
    #End
    
    #Initializing all of the Tkinter Windows
    customtkinter.set_appearance_mode("dark")
    tkWindow = [None] * 3
    for i in range(3):
        tkWindow[i] = customtkinter.CTk()
        w = 1000
        h = 600
        screenWidth = tkWindow[i].winfo_screenwidth()
        screenHeight = tkWindow[i].winfo_screenheight()
        x = (screenWidth/2) - (w/2)
        y = (screenHeight/2) - (h/2)
    
        tkWindow[i].geometry("%dx%d+%d+%d" % (w,h,x,y))
        tkWindow[i].title("RAMSEY")
        tkWindow[i].resizable("False","False")
        tkWindow[i].wm_protocol("WM_DELETE_WINDOW",exit)
    
    parameters = [None] * 3
    parameters[0] = ["American","Indian","Chinese","Japanese","Greek","Mexican","French","Peruvian","Korean","Thai","Cuban", "Dominican", "Vietnamese", "Spain", "Brazilian", "Colombian", "Filippino", "Jamaican", "Russian", "Italian"]
    parameters[1] = ["Manhattan","Queens","Bronx","Brooklyn","Staten Island"]
    parameters[2] = ["None"]
    options = ["Cuisine", "Borough", "Area"]
    #End
    
    #Tkinter Window 1
    def closeWindow(*args):
        tkWindow[0].destroy()
        tkWindow[1].mainloop()
        
    button = customtkinter.CTkButton(tkWindow[0], height = 70, width = 150, command = closeWindow, text = "Ready to Eat?")
    button.place(x = 420, y = 450)
    
    ramseyLabel = customtkinter.CTkLabel(tkWindow[0], text = "R.A.M.S.E.Y.", font = ('Script',60), height = 70, width = 150)
    otherRamseyLabel = customtkinter.CTkLabel(tkWindow[0], text = "(Remarkable Aromas Make Sizzling Enjoyable Yumminess)", font = ('Script',40), height = 60, width = 150)
    ramseyLabel.place(x = 380, y = 300)
    otherRamseyLabel.place(x = 200, y = 370)
    
    image = PIL.Image.open(requests.get("https://www.shutterstock.com/image-photo/cuisine-different-countries-western-eastern-600nw-384573541.jpg", stream=True).raw)
    newImage = image.resize((600, 400))
    resizeImage = ImageTk.PhotoImage(newImage)
    picture = customtkinter.CTkLabel(tkWindow[0], image = resizeImage, text = "")
    picture.place(x = 300, y = 25)
    #End
    
    #Tkinter Window 2     
    vars = [None] * 3
    labels = [None] * 3
    dropdowns = [None] * 3
    increment = 230
    
    for i in range(3):
        vars[i] = StringVar()
        vars[i].set("Select")
        
        labels[i] = customtkinter.CTkLabel(tkWindow[1],fg_color = "transparent", height = 30, width = 100,text = options[i])
        dropdowns[i] = customtkinter.CTkOptionMenu(tkWindow[1],variable = vars[i],values = parameters[i],height = 30, width = 100)
        
        labels[i].place(x = increment, y = 75)
        dropdowns[i].place(x = increment, y = 100)
        increment += 200
    
    def enableArea(*args):
        global vars, temp

        #To reset the areas dropdown box if the user chooses a different borough, but not if they choose a different cuisine
        if temp != dropdowns[1].get() and dropdowns[1].get() != "Select" and dropdowns[2].cget("state") == "normal":
            vars[2].set("Select")
            
        if dropdowns[0].get() != "Select" and dropdowns[1].get() != "Select":    
            for i in range(5):
                if dropdowns[1].get() == parameters[1][i]:
                    dropdowns[2].configure(values = areas[i])
                    temp = parameters[1][i]
            dropdowns[2].configure(state = "normal")    
            
        
    
    vars[0].trace("w",enableArea)       
    vars[1].trace("w", enableArea)
    
    
    dropdowns[2].configure(state = "disabled")
    #End
   
    
    
   
if __name__ == "__main__":
   tkWindow[0].mainloop()