import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage



class CategoryPage(ctk.CTkFrame):
    def __init__(self, parent, switch_to_HomePage,switch_to_BrowseProductsPage,user_id):
        super().__init__(parent,fg_color="white")
        self.user_id=user_id
        self.user_id=user_id
        self.switch_to_BrowseProductsPage=switch_to_BrowseProductsPage
        self.img = PhotoImage(file='images\Category.png')
        tk.Label(self, image=self.img, bg='white').place(x=50, y=150)
        self.frame = ctk.CTkFrame(self, width=350, height=400, fg_color="white",bg_color="white")
        self.frame.place(x=480, y=20)
        self.heading = ctk.CTkLabel(self.frame, text="Choose Category", text_color="#57A1F8", bg_color="white",fg_color="white",  font=("Century Gothic", 28))
        self.heading.place(x=40, y=5)

        y = 70
        self.category_button("Vehicles", y)
        y += 60
        self.category_button("Electronics & Appliances", y)
        y += 60
        self.category_button("Properties", y)
        y += 60
        self.category_button("Mobiles & Tablets", y)
        y += 60
        self.category_button("Other", y)
        y += 60
        ctk.CTkButton(self.frame, width=19,  text="Back", fg_color='#57A1F8', bg_color="white",text_color="white", border_width=0,font=("TkDefaultFont", 20),hover=False, command= lambda:switch_to_HomePage(user_id)).place(x=235, y=y)

    def category_button(self, text, y):
        ctk.CTkButton(self.frame, width=39, text=text, fg_color='#57A1F8', bg_color="white",text_color="white", font=("TkDefaultFont", 20),border_width=0,hover=False,command=lambda:self.switch_to_BrowseProductsPage(self.user_id,text)).place(x=35, y=y)
