import customtkinter


class checkbox_frame(customtkinter.CTkFrame):
    def __init__(self,master,list):
        super().__init__(master)

        self.list = list
        self.boxes = []

        for i,value in enumerate(list):
            checkbox = customtkinter.CTkCheckBox(self,text=value)
            checkbox.grid(row=i,column=0,padx=10,pady=(0,10),sticky="w")
            self.boxes.append(checkbox)
        
    
    def get_checkboxes(self):
        checked_boxes = []
        for box in self.boxes:
            if box.get() == 1:
                checked_boxes.append(box.cget("text"))

        return checked_boxes
        



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("500x300")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = checkbox_frame(self,list=["button 1, woah!","button 2, crazy!","button 3, diabolical!"])
        self.frame.grid(row=0,column=0,pady=10,padx=10,sticky="nws")

        self.frame2 = checkbox_frame(self,list=["are you alive?","do you like cats?"])
        self.frame2.grid(row=0,column=1,pady=10,padx=10,sticky="nws")


        self.button = customtkinter.CTkButton(self, text="print checked boxes", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew",columnspan=2)

    def button_callback(self):
        print("checked boxes:",self.frame.get_checkboxes())
        print("checked boxes2:",self.frame2.get_checkboxes())

app = App()
app.mainloop()