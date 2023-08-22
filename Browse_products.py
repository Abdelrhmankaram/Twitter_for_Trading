from tkinter import *
from Product import Product
from db import get_product_by_category
from item import ItemListPage
class BrowseProductsPage(Frame):
    def __init__(self, parent, switch_to_CategoryPage,user_id,category):
        super().__init__(parent,bg="white")
        self.category=category
        img = PhotoImage(file='images/item_window.png')
        image_label = Label(self, image=img, bg='white')
        image_label.image = img
        image_label.place(x=-220, y=0)
        self.frame = Frame(self, height=500, width=400, bg="white")
        self.frame.place(x=400, y=0)

        ItemListPage(self.frame,get_product_by_category(self.category),False).pack()
        back_button = Button(self,width=19, pady=7, text="Back", bg='#57A1F8', fg="white", border=0,command=lambda:switch_to_CategoryPage(user_id))
        back_button.place(x=50, y=400)
        
       