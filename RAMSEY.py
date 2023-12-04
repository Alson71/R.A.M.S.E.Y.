from tkinter import *
import PIL.Image
import customtkinter
import requests
from googlemaps import Client 
from tkinter.ttk import *
from time import sleep 
import threading
from io import BytesIO

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
    
    #General text wrapping solution
    @staticmethod
    def textWrapping(randomString, length, enableSpecifiedLimit, specifiedLimit): #Specified limit is used to check if the text is too long (put 'False' and '0' for those fields if there is no specific limit needed)
        wrappedString = ""
        stringArray = randomString.split()
        temp = 0
        cumulativeCounter = 0
        for i in range(len(stringArray)):
            if enableSpecifiedLimit:
                if cumulativeCounter > specifiedLimit: 
                    break
            
            cumulativeCounter += len(stringArray[i]) + 1
            temp += len(stringArray[i]) + 1  
            if temp >= length:
                wrappedString += "\n"
                temp = len(stringArray[i]) + 1 
            wrappedString += stringArray[i] + " "
        return wrappedString
        
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
        self.trackResults = 0
    
        self.vars = [None] * 3
        self.labels = [None] * 3
        self.dropdowns = [None] * 3
        self.increment = 160
        self.result_labels = [None] * 3
        self.tempFields = [None] * 3
        self.viewButtons = [None] * 3
        self.placesLabels = [None] * 3
        
        self.ramseyFrame3 = None
        self.ramseyFrame4 = [None] * 3
        
    
        for i in range(3):
            self.vars[i] = StringVar()
            self.vars[i].set("Select")
        
            self.labels[i] = customtkinter.CTkLabel(self,fg_color = "transparent", height = 35, width = 105,text = self.options[i])
            self.dropdowns[i] = customtkinter.CTkOptionMenu(self,variable = self.vars[i],values = self.parameters[i],height = 35, width = 105)
            
            self.viewButtons[i] = customtkinter.CTkButton(self, text = "View", height = 30, width = 100, command = lambda:  self.openResult(i))
            self.placesLabels[i] = customtkinter.CTkLabel(self, text = "")
            
            self.tempFields[i] = ""
            self.labels[i].place(x = self.increment, y = 55)
            self.dropdowns[i].place(x = self.increment, y = 80)
            self.result_labels[i] = customtkinter.CTkLabel(self, bg_color="transparent", height=40, width=100, text="")
            self.increment += 280

        self.vars[0].trace("w",self.enableArea)       
        self.vars[1].trace("w", self.enableArea)
        self.vars[0].trace("w",self.fetch_top_places)
        self.vars[1].trace("w",self.fetch_top_places)
        self.vars[2].trace("w",self.fetch_top_places)
        self.dropdowns[2].configure(state = "disabled")

       
        #Google Maps API Key
        self.api_key = 'AIzaSyAK1ms7Rl6vOVsZifEZPvCAgjT_ivmJGUY'  
        self.gmaps = Client(key=self.api_key)

            
            
   
    def enableArea(self, *args):
        if self.temp != self.dropdowns[1].get() and self.dropdowns[1].get() != "Select" and self.dropdowns[2].cget("state") == "normal":
                self.vars[2].set("Select")
                       
        if self.dropdowns[0].get() != "Select" and self.dropdowns[1].get() != "Select":    
            for i in range(5):
                if self.dropdowns[1].get() == self.parameters[1][i]:
                    self.dropdowns[2].configure(values = self.areas[i])
                    self.temp = self.parameters[1][i]
            self.dropdowns[2].configure(state = "normal")
                  
    # Method to fetch top 3 places based on user selection
    def fetch_top_places(self,*args):
        #If all the values in the dropdown boxes stay the same even when clicking on a dropdown box
        if self.tempFields[0] == self.dropdowns[0].get() and self.tempFields[1] == self.dropdowns[1].get() and self.tempFields[2] == self.dropdowns[2].get():
            return
        
       #Removes the results on every new run of this method and makes sure that no results get overwritten
        for i in range(self.trackResults):
            self.placesLabels[i].place_forget()
            self.viewButtons[i].place_forget()
            self.result_labels[i].place_forget()
            self.ramseyFrame4[i].destroy()
            
         # Get the selected options      
        cuisine = self.dropdowns[0].get()
        borough = self.dropdowns[1].get()
        area = self.dropdowns[2].get()
    
        # Fetch top 3 places from Google Places API based on user selection and makes sure to track if one of the fields have been changed
        if cuisine != "Select" and borough != "Select" and area != "Select" and self.temp == borough:
            if self.tempFields[0] != self.dropdowns[0].get() or self.tempFields[1] or self.dropdowns[1].get() or self.tempFields[2] != self.dropdowns[2].get():
                
                places_result = self.gmaps.places(query=f"{cuisine} restaurant in {area}, {borough}")

            # Get the top 3 places from the API response
                top_places = places_result['results'][:3]

            # Display the top 3 places in the GUI
                self.increment = 160
                for i, place in enumerate(top_places):
                    self.trackResults = i + 1
                    if 'photos' in place:
                        photo_reference = place['photos'][0]['photo_reference']  
                        tempPhoto = PIL.Image.open(requests.get(f"https://maps.googleapis.com/maps/api/place/photo?photoreference={photo_reference}&key={self.api_key}&maxwidth={400}&maxheight={400}", stream = True).raw)
                        placesPhoto = customtkinter.CTkImage(dark_image = tempPhoto, size = (250,200))
                        self.placesLabels[i].configure(image = placesPhoto)
                        self.placesLabels[i].place(x = self.increment - 70, y = 150)
     
                    place_name = place['name']
                    name = place_name
                    if(len(place_name) >= 17):
                        place_name = RAMSEYFrame1.textWrapping(name,17,True,34)
                    
                    self.ramseyFrame4[i] = RAMSEYFrame4(self,self)
                    self.ramseyFrame4[i].withdraw()
                    
                    self.result_labels[i].configure(text=place_name)
                    self.viewButtons[i].place(x = self.increment, y = 450)
                    self.result_labels[i].place(x=self.increment, y=385)
                    self.increment += 280
                           
        for i in range(3):
            self.tempFields[i] = self.dropdowns[i].get()
    
    def openResult(self, arg):
        self.withdraw()
        self.openTopLevel(0,0)
        self.after(11000,lambda: self.openTopLevel(1,arg))
        
    
    def openTopLevel(self, arg, arg2): # "0" is for Ramsey Frame 3 and "1" is for Ramsey Frame 4
        if arg == 0 and self.ramseyFrame3 == None or not self.ramseyFrame3.winfo_exists():
            self.ramseyFrame3 = RAMSEYFrame3(self)
        elif arg == 1:
            self.ramseyFrame3.destroy()
            self.ramseyFrame4[arg2].deiconify()
       
    
        
        
#Loading Screen (3rd Frame)       
class RAMSEYFrame3(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        
        self.animationIndex = 0
        self.animations = ["Working hard for your results", "Working hard for your results.", "Working hard for your results..", "Working hard for your results..."]
        
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

        loadingImage = PIL.Image.open(requests.get('https://cdn.openart.ai/uploads/image_Qz5b9Umf_1677711675034_512.webp', stream =True).raw)
        resizeImage = customtkinter.CTkImage(dark_image = loadingImage, size = (200,200))
        picture = customtkinter.CTkLabel(self, image = resizeImage, text = "")
        picture.place(x = 400, y = 125)
        
       
        
        self.loadingReminder = customtkinter.CTkLabel(self, text = '', font = ('Comic Sans', 30), fg_color= 'black', width = 200, height = 50)
        self.loadingReminder.place(x= 300, y=350)
        self.bar = customtkinter.CTkProgressBar(self, orientation = 'horizontal', mode = 'indeterminate', width = 500, height = 50)
        self.bar.place(x = 250, y = 450)
       
        self.update()
        threading.Thread(target=self.loadingAnimation).start()
        


    def loadingAnimation(self):
        
        for i in range(400):  
           self.update_idletasks()
           self.bar.step()
           if i % 20 == 0:
               self.animationIndex += 1
               self.loadingReminder.configure(text = self.animations[self.animationIndex % len(self.animations)])
           sleep(0.01)
        
        self.bar.destroy()
        self.loadingReminder.configure(text = "Results Loaded!") 
        self.loadingReminder.place(x = 395, y = 350)
            
        threading.Thread(target=self.loadingScreenGif).start()
            
            
            
    def loadingScreenGif(self):
        gif_url = "https://www.icegif.com/wp-content/uploads/smiley-face-icegif-3.gif"  
        response = requests.get(gif_url)
        
        if response.status_code == 200:
            gif = PIL.Image.open(BytesIO(response.content))
            gif_list = []
            try:
                while True:
                    gif.seek(len(gif_list))
                    gif_list.append(customtkinter.CTkImage(dark_image = gif.copy(), size = (167, 120)))
            except EOFError:
                pass
            
            animated_label = customtkinter.CTkLabel(self, text = "")
            animated_label.place(x = 425, y = 425)
            
            def update_label(index):
                frame = gif_list[index]
                animated_label.configure(image=frame)
                self.after(100, update_label, (index + 1) % len(gif_list))
    # Start displaying frames
            update_label(0)      
        
#Class that will show the result of any restaurant    
class RAMSEYFrame4(customtkinter.CTkToplevel):

    def __init__(self,master,ramseyFrame2,*args,**kwargs):
        super().__init__(master,*args,**kwargs)

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
        
        self.backButton = customtkinter.CTkButton(self, width = 100, height = 30, text = "Back", command = self.backToMenu)
        self.backButton.place(x = 50, y = 25)    
        
    def backToMenu(self):
        self.withdraw()
        self.master.deiconify()
   
          
if __name__ == "__main__":
   ramseyFrame1 = RAMSEYFrame1()
   ramseyFrame1.mainloop()
