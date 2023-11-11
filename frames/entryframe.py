import customtkinter
from tkinter import *

class EntryFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        
        self.build()

    def build(self):
        self.title = customtkinter.CTkLabel(
            self, 
            text = "Title", 
            fg_color = "green",
        )
        self.title.pack(side=TOP, fill=X)

        self.title = customtkinter.CTkLabel(
            self, 
            text = "Lorem Ipsum", 
            fg_color = "grey",
            anchor = NW
        )
        self.title.pack(side=BOTTOM, fill=BOTH, expand=True)
        
    def setEntry(self, data):
        pass