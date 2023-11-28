from tkinter import *
import PIL.Image
from PIL import ImageTk
import customtkinter
import requests

#The first window
class RAMSEYFrame1(customtkinter.CTk):
    customtkinter.set_appearance_mode("dark")
    
    #Constructor for Frame 1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        w = 1000
        h = 600
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = (screenWidth/2) - (w/2)
        y = (screenHeight/2) - (h/2)
    
        self.geometry("%dx%d+%d+%d" % (w,h,x,y))
        self.title("RAMSEY")
        self.resizable("False","False")
        self.wm_protocol("WM_DELETE_WINDOW",exit)
        
        background_image = PIL.Image.open(requests.get("https://cdn.openart.ai/stable_diffusion/05d2d2aa852fd048b29b4e0b13972653dd20c2b7_2000x2000.webp", stream=True).raw)
        resizeImage1 = customtkinter.CTkImage(dark_image = background_image, size = (1250, 800))
        background_label = customtkinter.CTkLabel(self, image=resizeImage1, text = "")
        background_label.place(x= 0,y= -150)
        
        anime_picture = PIL.Image.open(requests.get('https://64.media.tumblr.com/b670dd891997869721a4b2b1564aa6eb/tumblr_pklksruLv61u7vq8co1_r1_1280.png', stream =True).raw)
        resizeImage2 = customtkinter.CTkImage(dark_image = anime_picture, size = (350,350))
        picture = customtkinter.CTkLabel(self, image = resizeImage2, text = "")
        picture.place(x = 330, y = 25)
        
        anime_animated = PIL.Image.open(requests.get('https://i.pinimg.com/564x/31/83/0b/31830b86a06e318cb5e366ed32e044aa.jpg', stream =True).raw)
        resizeImage3 = customtkinter.CTkImage(dark_image = anime_animated, size = (100,100))
        picture = customtkinter.CTkLabel(self, image = resizeImage3, text = "",)
        picture.place(x = 330, y = 25)
        
        ramseyLabel = customtkinter.CTkLabel(self, text = "R.A.M.S.E.Y.", font = ('Script',60), height = 50, width = 110, text_color="white", fg_color='black')
        otherRamseyLabel = customtkinter.CTkLabel(self, text = "(Remarkable Aromas Make Sizzling Enjoyable Yumminess)", font = ('Script',40), height = 50, width = 120, text_color="white", fg_color='black')
        ramseyLabel.place(x = 380, y = 390)
        otherRamseyLabel.place(x = 190, y = 450)
    
        self.button = customtkinter.CTkButton(self, height = 70, width = 150, command = self.closeWindow, text = "Feelin' Hungry?", font = ('Comic Sans', 18))
        self.button.place(x = 420, y = 510)
        
        
    def closeWindow(self):
        self.destroy()
        ramseyFrame2 = RAMSEYFrame2()
        ramseyFrame2.mainloop()
        
#The second window   
class RAMSEYFrame2(customtkinter.CTk):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        
        w = 1000
        h = 600
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = (screenWidth/2) - (w/2)
        y = (screenHeight/2) - (h/2)
    
        self.geometry("%dx%d+%d+%d" % (w,h,x,y))
        self.title("RAMSEY")
        self.resizable("False","False")
        self.wm_protocol("WM_DELETE_WINDOW",exit)
        
        background_image = PIL.Image.open(requests.get("https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/10/1-Main-Feature-Photo.jpg", stream=True).raw)
        resizeImage1 = customtkinter.CTkImage(dark_image = background_image, size = (1250, 800))
        background_label = customtkinter.CTkLabel(self, image=resizeImage1, text = "")
        background_label.place(x= -90,y= -80)
        
    
        self.areas = [None] * 5
        self.areas[0] = ["Upper East Side", "Upper West Side", "Midtown", "Greenwich", "East Village"]
        self.areas[1] = ["Long Island City", "Astoria", "Forest Hills", "Queens Village", "Kew Gardens"]
        self.areas[2] = ["Riverdale", "Morris Park", "Parkchester", "Pelham Bay", "Fordham"]
        self.areas[3] = ["Brooklyn Heights", "DUMBO", "Prospect Heights", "Coney Island", "Flatbush"]
        self.areas[4] = ["West Brighton", "St. George", "Fort Wadsworth", "Charleston", "Dongan Hills"]

        self.parameters = [None] * 3
        self.parameters[0] = ["American","Indian","Chinese","Japanese","Greek","Mexican","French","Peruvian","Korean","Thai","Cuban", "Dominican", "Vietnamese", "Spain", "Brazilian", "Colombian", "Filippino", "Jamaican", "Russian", "Italian"]
        self.parameters[1] = ["Manhattan","Queens","Bronx","Brooklyn","Staten Island"]
        self.parameters[2] = ["None"]
        
        self.options = ["Cuisine", "Borough", "Area"]

        self.temp = ""
    
        self.vars = [None] * 3
        self.labels = [None] * 3
        self.dropdowns = [None] * 3
        self.increment = 160
    
        for i in range(3):
            self.vars[i] = StringVar()
            self.vars[i].set("Select")
        
            self.labels[i] = customtkinter.CTkLabel(self,fg_color = "transparent", height = 35, width = 105,text = self.options[i])
            self.dropdowns[i] = customtkinter.CTkOptionMenu(self,variable = self.vars[i],values = self.parameters[i],height = 35, width = 105)
        
            self.labels[i].place(x = self.increment, y = 55)
            self.dropdowns[i].place(x = self.increment, y = 80)
            self.increment += 280

        self.vars[0].trace("w",self.enableArea)       
        self.vars[1].trace("w", self.enableArea)
        self.vars[1].trace("w", self.enableButton)
        self.vars[2].trace("w", self.enableButton)
        self.dropdowns[2].configure(state = "disabled")
        
    def enableArea(self, *args):
        if self.temp != self.dropdowns[1].get() and self.dropdowns[1].get() != "Select" and self.dropdowns[2].cget("state") == "normal":
                self.vars[2].set("Select")
                       
        if self.dropdowns[0].get() != "Select" and self.dropdowns[1].get() != "Select":    
            for i in range(5):
                if self.dropdowns[1].get() == self.parameters[1][i]:
                    self.dropdowns[2].configure(values = self.areas[i])
                    self.temp = self.parameters[1][i]
            self.dropdowns[2].configure(state = "normal")
            
    def enableButton(self, *args):
        if self.dropdowns[0].get() != "Select" and self.dropdowns[1].get() != "Select" and self.dropdowns[2].get() != "Select":
            self.button = customtkinter.CTkButton(self, height = 75, width = 200, command = self.showLoading, text = "Search", font = ('Comic Sans', 26))
            self.button.place(x = 380, y = 450) 
            
            ready_to_eat_picture = PIL.Image.open(requests.get('https://media.comicbook.com/2019/09/evangelion-gendo-1187959.jpeg', stream =True).raw)
            resizeImage = customtkinter.CTkImage(dark_image = ready_to_eat_picture , size = (400,250))
            picture = customtkinter.CTkLabel(self, image = resizeImage, text = "")
            picture.place(x = 280, y = 180)
            
            readyLabel = customtkinter.CTkLabel(self, text = "Ready to Eat?", font = ('Comic Sans',35), height = 40, width = 100, text_color="white", fg_color='black')
            readyLabel.place(x = 390, y = 390)
            
                
    def showLoading(self):
        self.destroy()
        loadingFrame = RAMSEYFrame3()
        loadingFrame.mainloop()
        
#Loading Screen (3rd Frame)       
class RAMSEYFrame3(customtkinter.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        
        w = 1000
        h = 600
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = (screenWidth/2) - (w/2)
        y = (screenHeight/2) - (h/2)
    
        self.geometry("%dx%d+%d+%d" % (w,h,x,y))
        self.title("RAMSEY")
        self.resizable("False","False")
        self.wm_protocol("WM_DELETE_WINDOW",exit)
        
        
       
if __name__ == "__main__":
   ramseyFrame1 = RAMSEYFrame1()
   ramseyFrame1.mainloop()