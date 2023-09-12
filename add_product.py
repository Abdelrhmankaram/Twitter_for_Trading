import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage, messagebox
from Product import Product
from db import add_product
from validators import SignUp_validation
from validators import Number
from validators import Path
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os.path


class AddProductPage(ctk.CTkFrame):
    def __init__(self, parent, switch_to_HomePage, user_id):
        super().__init__(parent, fg_color="white")
        self.file_path = None
        self.parent = parent
        self.user_id = user_id
        self.img = PhotoImage(file='images\Add_product.png')
        tk.Label(self, image=self.img, bg='white').place(x=600, y=50)
        self.frame = ctk.CTkFrame(self, width=500, height=500, fg_color="white",bg_color="white")
        self.frame.place(x=60, y=0)

        heading = ctk.CTkLabel(self.frame, text="Fill The details", text_color="#57A1F8",
                           bg_color="white",fg_color="white",  font=("Century Gothic", 28))
        heading.place(x=40, y=15)

        y = 70
        self.name = self.create_entry(
            "Name", y, on_enter=self.on_enter_name, on_leave=self.on_leave_name)
        y += 70
        self.categories = ["Vehicles", "Electronics & Appliances",
                           "Properties", "Mobiles & Tablets", "Other"]
        self.selected_category = tk.StringVar(value=self.categories[0])

        self.create_category_radiobuttons(y)
        y += 120
        self.price = self.create_entry(
            "Price", y, on_enter=self.on_enter_price, on_leave=self.on_leave_price)
        y += 55
        self.path = ctk.CTkButton(self, width=19, text="Select image",font=("TkDefaultFont", 20),
                              fg_color='#57A1F8', bg_color="white",text_color="white", border_width=0, command=self.upload_file)
        self.path.place(x=110, y=y)
        y += 45
        self.description = self.create_entry(
            "Description", y, on_enter=self.on_enter_des, on_leave=self.on_leave_des)
        y += 55

        ctk.CTkButton(self.frame, width=39, text="Add Product", fg_color='#57A1F8',font=("TkDefaultFont", 20),
                  bg_color="white",text_color="white", border_width=0, command=self.add_product_command).place(x=25, y=y)
        y += 45
        ctk.CTkButton(self.frame, width=39, text="Back", fg_color='#57A1F8',font=("TkDefaultFont", 20), bg_color="white",text_color="white",
                  border_width=0, command=lambda: switch_to_HomePage(user_id)).place(x=25, y=y)

    def upload_file(self):
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        self.file_path = tk.filedialog.askopenfilename(filetypes=f_types)

    def create_entry(self, placeholder, y, on_enter, on_leave):
        entry = ctk.CTkEntry(self.frame, width=350, text_color="black",fg_color="white", border_width=0,
                         bg_color="white", font=("TkDefaultFont", 20))
        entry.place(x=30, y=y)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        ctk.CTkFrame(self.frame, width=295, height=2,
                 bg_color="black",fg_color="black").place(x=25, y=y + 27)
        return entry

    def on_enter_name(self, e):
        if self.name.get() == 'Name':
            self.name.delete(0, 'end')

    def on_leave_name(self, e):
        if self.name.get() == '':
            self.name.insert(0, 'Name')
        else:
            s = SignUp_validation.fix(self.name.get())
            if SignUp_validation.name_validate(s):
                self.name.delete(0, 'end')
                self.name.insert(0, s)
            else:
                messagebox.showinfo(
                    "Caution!", "name should only contain alphabet letters.", parent=self.parent)
                self.name.delete(0, 'end')
                self.name.insert(0, 'Name')

    def create_category_radiobuttons(self, y):
        for i, category in enumerate(self.categories):
            tk.Radiobutton(self, bg="white", text=category, variable=self.selected_category, value=category,
                           command=self.assign_category, font=("TkDefaultFont", 15)).place(x=110, y=y)
            y += 35

    def assign_category(self):
        selected_category = self.selected_category.get()
        print("Selected category:", selected_category)

    def assign(self, category):
        self.category_name = category

    def on_enter_price(self, e):
        if self.price.get() == 'Price':
            self.price.delete(0, 'end')

    def on_leave_price(self, e):
        if self.price.get() == '':
            self.price.insert(0, 'Price')
        else:
            if not Number.valid_num(self.price.get()):
                messagebox.showinfo(
                    "Caution!", "Invalid price", parent=self.parent)
                self.price.delete(0, 'end')
                self.price.insert(0, 'Price')

    def on_enter_path(self, e):
        if self.path.get() == 'Photo Path':
            self.path.delete(0, 'end')

    def on_leave_path(self, e):
        if self.path.get() == '':
            self.path.insert(0, 'Photo Path')
        else:
            s = SignUp_validation.fix(self.path.get())
            if not os.path.isfile(s):
                messagebox.showinfo(
                    "Caution!", "Photo Path is not valid", parent=self.parent)
                self.path.delete(0, 'end')
                self.path.insert(0, 'Photo Path')

    def on_enter_des(self, e):
        if self.description.get() == 'Description':
            self.description.delete(0, 'end')

    def on_leave_des(self, e):
        if self.description.get() == '':
            self.description.insert(0, 'Description')

    def reset(self):
        self.name.delete(0, 'end')
        self.price.delete(0, 'end')
        self.description.delete(0, 'end')
        self.name.insert(0, 'Name')
        self.price.insert(0, 'Price')
        self.file_path = None
        self.description.insert(0, "Description")

    def add_product_command(self):
        if (self.file_path is None):
            messagebox.showinfo(
                "Caution!", "select valid image", parent=self.parent)
            return
        product = Product(user_id=self.user_id, price=self.price.get(), product_name=self.name.get(
        ), category=self.selected_category.get(), picture=self.file_path, description=self.description.get(), status=1)
        add_product(product)
        messagebox.showinfo("Done", "Added successfully", parent=self.parent)
        self.reset()
