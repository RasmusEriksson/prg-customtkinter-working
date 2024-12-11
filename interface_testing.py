import customtkinter

button = NotImplemented

def button_function():

    print("Ze button has been pressed!")

app = customtkinter.CTk()
app.title("The coolest Name")
app.geometry("500x500")

button = customtkinter.CTkButton(app, text="Lets go!",command=button_function)
button.grid(row=0,column=0,padx=20,pady=20,sticky="ewsn",columnspan=2)

app.grid_columnconfigure((0,1), weight=1)
app.grid_rowconfigure(0,weight=1)



checkbox_1 = customtkinter.CTkCheckBox(app,text="Check Me Check Me plz!!")
checkbox_1.grid(row=1,column=0,padx=20,pady=(0,20),sticky="w")

checkbox_2 = customtkinter.CTkCheckBox(app,text="Me too Me too!!!!")
checkbox_2.grid(row=1,column=1,padx=20,pady=(0,20),sticky="w")


app.mainloop()