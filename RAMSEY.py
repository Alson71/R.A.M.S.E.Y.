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
        #newImage1 = customtkinter.CTkImage(dark_image = background_image, size = (screenWidth, screenHeight))
        resizeImage1 = ImageTk.PhotoImage(background_image)
        background_label = customtkinter.CTkLabel(self, image=resizeImage1, text = "")
        background_label.place(x= 0,y= -150)
        
        anime_picture = PIL.Image.open(requests.get('https://64.media.tumblr.com/b670dd891997869721a4b2b1564aa6eb/tumblr_pklksruLv61u7vq8co1_r1_1280.png', stream =True).raw)
        resizeImage2 = customtkinter.CTkImage(dark_image = anime_picture, size = (350,350))
        picture = customtkinter.CTkLabel(self, image = resizeImage2, text = "")
        picture.place(x = 330, y = 25)
        
        anime_animated = PIL.Image.open(requests.get('https://i.pinimg.com/564x/e3/90/a4/e390a4626bab79e09d85b87f98f3c2d9.jpg', stream =True).raw)
        resizeImage3 = customtkinter.CTkImage(dark_image = anime_animated, size = (100,100))
        picture = customtkinter.CTkLabel(self, image = resizeImage3, text = "")
        picture.place(x = 330, y = 25)
        
        ramseyLabel = customtkinter.CTkLabel(self, text = "R.A.M.S.E.Y.", font = ('Script',60), height = 50, width = 110, text_color="white", fg_color='black')
        otherRamseyLabel = customtkinter.CTkLabel(self, text = "(Remarkable Aromas Make Sizzling Enjoyable Yumminess)", font = ('Script',40), height = 50, width = 120, text_color="white", fg_color='black')
        ramseyLabel.place(x = 380, y = 390)
        otherRamseyLabel.place(x = 190, y = 450)
    
        self.button = customtkinter.CTkButton(self, height = 70, width = 150, command = self.closeWindow, text = "Ready to Eat?")
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
        #newImage1 = background_image.resize((screenWidth, screenHeight))
        resizeImage1 = ImageTk.PhotoImage(background_image)
        background_label = customtkinter.CTkLabel(self, image=resizeImage1, text = "")
        background_label.place(x= -140,y= -140)
        
    
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
        self.increment = 230
    
        for i in range(3):
            self.vars[i] = StringVar()
            self.vars[i].set("Select")
        
            self.labels[i] = customtkinter.CTkLabel(self,fg_color = "transparent", height = 30, width = 100,text = self.options[i])
            self.dropdowns[i] = customtkinter.CTkOptionMenu(self,variable = self.vars[i],values = self.parameters[i],height = 30, width = 100)
        
            self.labels[i].place(x = self.increment, y = 75)
            self.dropdowns[i].place(x = self.increment, y = 100)
            self.increment += 200

        self.vars[0].trace("w",self.enableArea)       
        self.vars[1].trace("w", self.enableArea)
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
            
      
   
if __name__ == "__main__":
   ramseyFrame1 = RAMSEYFrame1()
   ramseyFrame1.mainloop()