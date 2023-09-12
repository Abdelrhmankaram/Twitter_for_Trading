import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

from db import delete_product, get_phone

class CustomItem(ctk.CTkFrame):
    def __init__(self, parent, product_object,flag):
        super().__init__(parent,fg_color="white",bg_color="white")
        self.configure(bg_color="white", height=170, width=500, cursor='hand2')
        self.product_id=product_object.product_id
        self.pic = Image.open(product_object.picture)
        self.pic = self.pic.resize((160, 120))
        self.img = ImageTk.PhotoImage(self.pic)
        self.img_label = tk.Label(self, image=self.img, width=120, height=120, bg="white")
        self.img_label.place(x=0, y=0)
        self.name_label = tk.Label(self, text=product_object.product_name, font=("Arial", 20), bg="white", fg="red")
        self.name_label.place(x=130, y=10)
        if flag:
            self.delete_button = tk.Button(self, text="Delete", width=10, pady=7, bg='#57A1F8', fg="white", border=0,command=self.delete_item)
            self.delete_button.place(x=320, y=30)
            
        self.description_label = tk.Label(self, text=product_object.description, font=("Arial", 10), bg="white")
        self.description_label.place(x=130, y=50)
        self.phone_label = tk.Label(self, text=get_phone(product_object.user_id), font=("Arial", 10), bg="white")
        self.phone_label.place(x=130, y=70)
    
        self.price_label = tk.Label(self, text=str(product_object.price)+"$", font=("Arial", 20), bg="white", fg="green")
        x = self.winfo_width() - len(str(product_object.price)) * 14
        self.price_label.place(x=300, y=77)

        self.bind("<Button>", lambda e: print("hello"))
        #elf.img_label.bind("<Button>", lambda e: print("hello"))
    def delete_item(self):
        self.destroy()
        delete_product(self.product_id)

class ItemListPage(ctk.CTkFrame):
    def __init__(self, parent, items,flag):
        super().__init__(parent,fg_color="white",bg_color="white")
        self.items = items
        self.flag=flag
        self.canvas = tk.Canvas(self, bg='white', height=600, width=500)  # Set canvas size
        self.scroll_y = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scroll_y.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.frame = ctk.CTkFrame(self.canvas, bg_color='white',fg_color="white")
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw', width=500)  # Set frame width

        self.populate_frame()

    def populate_frame(self):
        y_position = 10
        for item in self.items:
            custom_item = CustomItem(self.frame, item,self.flag)
            custom_item.pack(pady=5)
            y_position += custom_item.winfo_height() + 5
        
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

