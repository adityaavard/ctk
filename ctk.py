#import
import customtkinter
from tkinter import *

#custom color theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

#main window
ctk = customtkinter.CTk()
ctk.geometry("720x480")
ctk.title("customtkinter window")

#text testing
textlabel = customtkinter.CTkLabel(ctk, text="test")
textlabel.pack()

#mainloop
ctk.mainloop()

#print failure message
print("faliure")

