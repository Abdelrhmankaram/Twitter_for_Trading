from tkinter import *
from Product import Product
from db import get_product_by_category, get_products_by_user
from item import ItemListPage
#from test import ItemListPage
class UserProductsPage(Frame):
    def __init__(self, parent, switch_to_HomePage,user_id):
        super().__init__(parent,bg="white")
        img = PhotoImage(file='images/item_window.png')
        image_label = Label(self, image=img, bg='white')
        image_label.image = img
        image_label.place(x=-220, y=0)
        self.frame = Frame(self, height=500, width=400, bg="white")
        self.frame.place(x=400, y=0)

        ItemListPage(self.frame,get_products_by_user(user_id),True).pack()
        
        back_button = Button(self,width=19, pady=7, text="Back", bg='#57A1F8', fg="white", border=0,command=lambda:switch_to_HomePage(user_id))
        back_button.place(x=50, y=400)
        
  