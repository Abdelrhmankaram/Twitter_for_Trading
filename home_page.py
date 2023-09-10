import tkinter as tk
from tkinter import PhotoImage

class HomePage(tk.Frame):
    def __init__(self, parent, switch_to_signin,switch_to_CategoryPage,switch_to_AddProductPage,user_id,switch_to_UserProductsPage):
        super().__init__(parent,bg="white")
        self.user_id=user_id
        self.parent = parent
        self.parent.title("Twitter")
        self.img = PhotoImage(file='images\options_window.png')
        tk.Label(self, image=self.img, bg='white').place(x=50, y=50)
        self.frame = tk.Frame(self, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)
        heading = tk.Label(self.frame, text="Options", fg="#57A1F8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=110, y=5)

        y = 80
        tk.Button(self.frame, width=39, pady=7, text="Browse products", bg='#57A1F8', fg="white", border=0,command=lambda:switch_to_CategoryPage(self.user_id)).place(x=35, y=y)
        y += 60
        tk.Button(self.frame, width=39, pady=7, text="Sell new product", bg='#57A1F8', fg="white", border=0,command=lambda:switch_to_AddProductPage(self.user_id)).place(x=35, y=y)
        y += 60
        tk.Button(self.frame, width=39, pady=7, text="View your products", bg='#57A1F8', fg="white", border=0,command=lambda:switch_to_UserProductsPage(self.user_id)).place(x=35, y=y)
        y += 90
        tk.Button(self.frame, width=19, pady=7, text="Log out", bg='#57A1F8', fg="white", border=0, command=switch_to_signin).place(x=175, y=y)