from tkinter import *
from customtkinter import *
from Product import Product
from db import get_product_by_category, get_products_by_user
from item import ItemListPage
# from test import ItemListPage


class UserProductsPage(CTkFrame):
    def __init__(self, parent, switch_to_HomePage, user_id):
        super().__init__(parent, fg_color="white")
        img = PhotoImage(file='images/item_window.png')
        image_label = Label(self, image=img, bg='white')
        image_label.image = img
        image_label.place(x=-180, y=0)
        self.frame = CTkFrame(self, height=500, width=400, fg_color="white",bg_color="white")
        self.frame.place(x=520, y=0)

        ItemListPage(self.frame, get_products_by_user(user_id), True).pack()

        back_button = CTkButton(self, width=19, text="Back", fg_color='#57A1F8',bg_color="white",text_color="white",
                              border_width=0, hover=False, font=("TkDefaultFont", 20), command=lambda: switch_to_HomePage(user_id))
        back_button.place(x=50, y=400)
