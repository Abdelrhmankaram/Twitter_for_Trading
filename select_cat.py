import tkinter as tk
from tkinter import PhotoImage



class CategoryPage(tk.Frame):
    def __init__(self, parent, switch_to_HomePage,switch_to_BrowseProductsPage,user_id):
        super().__init__(parent,bg="white")
        self.user_id=user_id
        self.user_id=user_id
        self.switch_to_BrowseProductsPage=switch_to_BrowseProductsPage
        self.img = PhotoImage(file='images\Category.png')
        tk.Label(self, image=self.img, bg='white').place(x=50, y=50)
        self.frame = tk.Frame(self, width=350, height=400, bg="white")
        self.frame.place(x=480, y=20)
        self.heading = tk.Label(self.frame, text="Choose Category", fg="#57A1F8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
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
        tk.Button(self.frame, width=19, pady=7, text="Back", bg='#57A1F8', fg="white", border=0, command= lambda:switch_to_HomePage(user_id)).place(x=175, y=y)

    def category_button(self, text, y):
        tk.Button(self.frame, width=39, pady=7, text=text, bg='#57A1F8', fg="white", border=0,command=lambda:self.switch_to_BrowseProductsPage(self.user_id,text)).place(x=35, y=y)
