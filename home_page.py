import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, switch_to_signin,switch_to_CategoryPage,switch_to_AddProductPage,user_id,switch_to_UserProductsPage):
        super().__init__(parent,fg_color="white")
        self.user_id=user_id
        self.parent = parent
        self.parent.title("Twitter")
        self.img = PhotoImage(file='images\options_window.png')
        tk.Label(self, image=self.img, bg='white',fg="white").place(x=50, y=50)
        self.frame = ctk.CTkFrame(self, width=350, height=350, bg_color="white",fg_color="white")
        self.frame.place(x=480, y=70)
        heading = ctk.CTkLabel(self.frame, text="Options", fg_color="white",text_color="#57A1F8", bg_color="white", font=("Century Gothic", 28))
        heading.place(x=110, y=5)
        x=60;
        y = 80
        ctk.CTkButton(self.frame, width=200, text="Browse products",text_color="white", bg_color='white', fg_color="#57A1F8",font=("TkDefaultFont", 20), border_width=0,command=lambda:switch_to_CategoryPage(self.user_id)).place(x=x, y=y)
        y += 60
        ctk.CTkButton(self.frame, width=200, text="Sell new product", fg_color='#57A1F8', bg_color="white",text_color="white", border_width=0,
        font=("TkDefaultFont", 20),command=lambda:switch_to_AddProductPage(self.user_id)).place(x=x, y=y)
        y += 60
        ctk.CTkButton(self.frame, width=200, text="View your products", fg_color='#57A1F8', bg_color="white",font=("TkDefaultFont", 20),text_color="white", border_width=0,command=lambda:switch_to_UserProductsPage(self.user_id)).place(x=x, y=y)
        y += 90
        ctk.CTkButton(self.frame, width=19, text="Log out", fg_color='#57A1F8', bg_color="white",text_color="white", font=("TkDefaultFont", 20),border_width=0, command=switch_to_signin).place(x=x+200, y=y)