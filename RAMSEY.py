from tkinter import *
from tkinter import messagebox
import PIL.Image
import customtkinter
import requests
from googlemaps import Client 
from tkinter.ttk import *
from time import sleep 
import threading
from io import BytesIO
import webbrowser
from datetime import date

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
            
            cumulativeCounter += len(stringArray[i]) + 1
            temp += len(stringArray[i]) + 1  
            if temp >= length:
                wrappedString += "\n"
                temp = len(stringArray[i]) + 1
            if enableSpecifiedLimit:
                    if cumulativeCounter > specifiedLimit:
                        wrappedString += stringArray[i]
                        break    
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
        self.areas[0] = ["Upper East Side", "Upper West Side", "Midtown", "Time Square", "East Village"]
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
        self.photo = [None] * 3
        
        self.name = ["","",""]
        self.website = ["","",""]
        self.hours = ["","",""]
        self.address = ["","",""]
        self.rating = ["","",""]
        self.phoneNumber = ["","",""]
    
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
        
        self.reviews = [["",""],["",""],["",""]]
        self.menuURL = ["","",""]
        
        self.today = date.today()
    
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
        self.vars[0].trace("w", lambda *args: self.fetch_top_places_threaded(*args))
        self.vars[1].trace("w", lambda *args: self.fetch_top_places_threaded(*args))
        self.vars[2].trace("w", lambda *args: self.fetch_top_places_threaded(*args))
        self.dropdowns[2].configure(state = "disabled")
       
        #Google Maps API Key
        self.api_key = 'AIzaSyAK1ms7Rl6vOVsZifEZPvCAgjT_ivmJGUY'  
        self.gmaps = Client(key=self.api_key)

            
            
    def fetch_top_places_threaded(self, *args):
        threading.Thread(target=self.fetch_top_places, args=args).start()
        
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
        #If all of the values stay the same
        if self.tempFields[0] == self.dropdowns[0].get() and self.tempFields[1] == self.dropdowns[1].get() and self.tempFields[2] == self.dropdowns[2].get():
            return
       
        
       #Removes the results on every new run of this method and makes sure that no results get overwritten
        for i in range(self.trackResults):
            self.placesLabels[i].place_forget()
            self.viewButtons[i].place_forget()
            self.result_labels[i].place_forget()
            if not self.ramseyFrame4[i] == None:
                self.ramseyFrame4[i].destroy()
            
         # Get the selected options      
        cuisine = self.dropdowns[0].get()
        borough = self.dropdowns[1].get()
        area = self.dropdowns[2].get()
    
        # Fetch top 3 places from Google Places API based on user selection and makes sure to track if one of the fields have been changed
        if cuisine != "Select" and borough != "Select" and area != "Select" and self.temp == borough:
            if self.tempFields[0] != self.dropdowns[0].get() or self.tempFields[1] or self.dropdowns[1].get() or self.tempFields[2] != self.dropdowns[2].get():
                
                #To prevent the user from causing errors while parsing data
                for l in range(3):
                    self.dropdowns[l].configure(state = "disabled")  
                    
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
                        self.photo[i] = customtkinter.CTkImage(dark_image = tempPhoto, size = (250,200))
                        self.placesLabels[i].configure(image = self.photo[i])
                        self.placesLabels[i].place(x = self.increment - 70, y = 150)
                             
                    place_details = self.gmaps.place(place_id=place['place_id'], fields=['website','formatted_phone_number','reviews','opening_hours','url'])
                    if 'result' in place_details and 'website' in place_details['result']:
                        self.website[i] = place_details['result']['website']
                    else: self.website[i] = ""
                    
                    if 'result' in place_details and 'formatted_phone_number'in place_details['result']:
                        self.phoneNumber[i] = place_details['result']['formatted_phone_number']
                    else: self.phoneNumber[i] = "Not Available"
                    
                    if 'result' in place_details and 'reviews' in place_details['result']:
                        reviews = place_details['result']['reviews'][:2]
                        count = 0
                        for review in reviews:
                             self.reviews[i][count] = review['text']
                             count += 1
                    else:
                        self.reviews[i][0] = ""
                        self.reviews[i][1] = "" 
                        
                    if 'result' in place_details and 'opening_hours' in place_details['result']:
                        weekday_text = place_details['result']['opening_hours'].get('weekday_text',[])
                        for temp in weekday_text:
                            hoursList = temp.split()
                            if self.getDate(hoursList[0]) == self.today.weekday():
                                self.hours[i] = temp
                                break
                    else:
                        self.hours[i] = "Not Available"
                        
                    if 'result' in place_details and ('url' in place_details['result'] and 'website' in place_details['result']):
                        request = requests.get(self.website[i] + "menu") #Checking if the website already has a built in menu
                        if request.status_code == 200:
                            self.menuURL[i] = self.website[i] + "menu"        
                        else: self.menuURL[i] = place_details['result']['url']   
                       
                    
                    self.name[i] = place['name']
                    self.address[i] = place['formatted_address']
                    self.rating[i] = place['rating']
                    
                    name = self.name[i]
                    if(len(self.name[i]) >= 17):
                        self.name[i] = RAMSEYFrame1.textWrapping(name,17,True,34)
                
                    
                    
                    self.result_labels[i].configure(text=self.name[i])
                    
                    #Putting all of the data into the button method to be used if the user tries to open a result
                    self.viewButtons[i].configure(command=lambda i=i, name=self.name[i], website=self.website[i], hours=self.hours[i],
    address=self.address[i], rating=self.rating[i], phoneNumber=self.phoneNumber[i],
    review1=self.reviews[i][0], review2=self.reviews[i][1], photo=self.photo[i],
    menuURL=self.menuURL[i]: self.openResult(i, name, website, hours, address, rating, phoneNumber, review1, review2, photo, menuURL))
                    
                    
                    self.viewButtons[i].place(x = self.increment, y = 450)
                    self.viewButtons[i].configure(state = "disabled")
                    
                    self.result_labels[i].place(x=self.increment, y=385)
                    self.increment += 280
            
        #Withdraw is called multiple times because sometimes the window doesn't close properly
        if self.dropdowns[0].get() != "Select" and self.dropdowns[1].get() != "Select":                     
            for i in range(3):
                self.dropdowns[i].configure(state = "normal")
                self.viewButtons[i].configure(state = "normal")
                self.tempFields[i] = self.dropdowns[i].get()
    
    def openResult(self,arg,name,website,hours,address,rating,phoneNumber,reviews,reviews1,photo,menuURL):
        self.withdraw()
        if self.ramseyFrame4[arg] == None:
            self.openTopLevel(0,arg,name,website,hours,address,rating,phoneNumber,reviews,reviews1,photo,menuURL)
        else:
            self.ramseyFrame3 = RAMSEYFrame3(self)
             
        self.after(11000,lambda: self.openTopLevel(1,arg,name,website,hours,address,rating,phoneNumber,reviews,reviews1,photo,menuURL))
        
    
    def openTopLevel(self, arg, arg2,name,website,hours,address,rating,phoneNumber,reviews,reviews1,photo,menuURL): # "0" is for Ramsey Frame 3 and "1" is for Ramsey Frame 4
        if arg == 0 and self.ramseyFrame3 == None or not self.ramseyFrame3.winfo_exists():
            self.ramseyFrame3 = RAMSEYFrame3(self)
            if self.ramseyFrame4[arg2] == None or not self.ramseyFrame4[arg2].winfo_exists(): 
                self.ramseyFrame4[arg2] = RAMSEYFrame4(self,self,name,website,hours,address,rating,phoneNumber,reviews,reviews1,photo,menuURL)
                self.ramseyFrame4[arg2].withdraw()
                
        elif arg == 1:
            self.ramseyFrame3.destroy()
            self.ramseyFrame4[arg2].deiconify()
            
    
    #To be used to iterate the hours list and find the correct date     
    def getDate(self,day):
        if day == "Monday:":
            return 0  
        elif day == "Tuesday:":
            return 1 
        elif day == "Wednesday:":
            return 2 
        elif day == "Thursday:":
            return 3 
        elif day == "Friday:":
            return 4 
        elif day == "Saturday:":
            return 5 
        else:
            return 6 
    
        
        
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
        
        for i in range(300):  
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
        
#Frame that will show the result of any restaurant    
class RAMSEYFrame4(customtkinter.CTkToplevel):

    def __init__(self,master,ramseyFrame2,name,websiteURL,hours,address,rating,phoneNumber,review1,review2,photo,menuURL,*args,**kwargs):
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
        
          
        
        self.backButton = customtkinter.CTkButton(self, width = 100, height = 30, text = "Back", command = self.backToMenu)
        self.backButton.place(x = 50, y = 25)
        
        self.websiteButton = customtkinter.CTkButton(self,width = 100, height = 30, text = "Website", command = lambda: self.openWebsite(websiteURL))
        self.websiteButton.place(x = 325, y = 200)
        self.menuButton = customtkinter.CTkButton(self,width = 100, height = 30, text = "Menu", command = lambda: webbrowser.open_new(menuURL))
        self.menuButton.place(x = 535, y = 200)
        
        self.addressLabel = customtkinter.CTkLabel(self, width = 100, height = 50, font = ('Script',45), text = "Address:", fg_color = "black")
        self.addressLabel.place(x = 70, y = 315)
        
        text = address
        if len(address) >= 18:    
            text = RAMSEYFrame1.textWrapping(address,18,False,0)
            
        self.address = customtkinter.CTkLabel(self, text = text,width = 100, height = 50, font = ('Comic Sans', 20))
        self.address.place(x = 60, y = 375)
        
        self.hours = customtkinter.CTkLabel(self, text = str(hours), width = 100, height = 50, font = ('Comic Sans', 20))
        self.hours.place(x = 340, y = 230)
        
        self.ratingLabel = customtkinter.CTkLabel(self, width = 100, height = 50, font = ('Script',45), text = "Rating:", fg_color = "black")
        self.ratingLabel.place(x = 420, y = 315)
        
        self.rating = customtkinter.CTkLabel(self, text = str(rating) + " out of 5.0",width = 100, height = 50, font = ('Comic Sans', 20))
        if len(str(rating)) == 1:
            self.rating.place(x = 420, y = 400)
        else:
            self.rating.place(x = 410, y = 400)
        
        self.reviewLabel = customtkinter.CTkLabel(self, width = 100, height = 50, font = ('Script',45), text = "Reviews:", fg_color = "black")
        self.reviewLabel.place(x = 750, y = 315)
        
        
        self.phoneNumber = customtkinter.CTkLabel(self, text = "Phone Number: " + str(phoneNumber), width = 100, height = 30, font = ('Comic Sans', 20))
        self.phoneNumber.place(x = 340, y = 280)
        
        #Formatting the reviews and limiting them to only 75 characters
        text = review1
        if(len(review1) >= 37):
            text = RAMSEYFrame1.textWrapping(review1,37, True, 125)
            text = "1. " + text + "..."
        self.review = customtkinter.CTkLabel(self, text = text,width = 100, height = 50, font = ('Comic Sans', 20))
        self.review.place(x = 655, y = 365)
        
        text = review2
        if(len(review2) >= 37):
            text = RAMSEYFrame1.textWrapping(review2,37, True, 125)
            text = "2. " + text + "..."
        self.review1 = customtkinter.CTkLabel(self, text = text,width = 100, height = 50, font = ('Comic Sans', 20))
        self.review1.place(x = 655, y = 480)
        
        
        self.titleOfRes = customtkinter.CTkLabel(self, height = 50, width = 110, font = ('Comic Sans',40), fg_color = "blue", text_color = "turquoise")
        text = name
        self.array = name.split()
        
        #Text wrapping that accounts for all types of text lengths of the restaurant name
        if(len(name) >= 10): 
            text = RAMSEYFrame1.textWrapping(name,10,True,21)
            lessThanSix = True
            
            #Positioning the entire line based off the length of the word for each individual line
            for i in range(len(self.array)):
                if len(self.array[i]) > 6:
                    lessThanSix = False
                    
            if not lessThanSix:   
                self.titleOfRes.place(x = 400, y = 10) 
            else:
                self.titleOfRes.place(x = 425, y = 10)
        elif len(name) < 6:
            self.titleOfRes.place(x = 425, y = 10)
        
        elif len(name) > 6 and len(self.array) == 1: #Adjust the label accordingly if it's only one word and more than 6 letters long
            increment = (len(name) - 6) * 12
            self.titleOfRes.place(x = 425 - increment, y = 10)    
        else:
            text = RAMSEYFrame1.textWrapping(name,6,False,0)
            self.titleOfRes.place(x = 425, y = 10)
            
        self.titleOfRes.configure(text = text)
        
        
        self.place = customtkinter.CTkLabel(self,image = photo, text = "")
        self.place.place(x = 700, y = 50)
        
    def openWebsite(self, websiteURL):
        if websiteURL == "":
            messagebox.showinfo("Website", "No website has been found!")     
        else:
            webbrowser.open_new(websiteURL)
        
    def backToMenu(self):
        self.withdraw()
        self.master.deiconify()
   
          
if __name__ == "__main__":
   ramseyFrame1 = RAMSEYFrame1()
   ramseyFrame1.mainloop()