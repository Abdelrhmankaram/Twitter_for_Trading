import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage, messagebox
import Signup
from User import User
from db import *
from validators import SignUp_validation
from PIL import ImageTk, Image


class SignupPage(ctk.CTkFrame):
    def __init__(self, parent, switch_to_login, switch_to_HomePage):
        super().__init__(parent, fg_color="white")
        self.switch_to_HomePage = switch_to_HomePage
        self.switch_to_loginn = switch_to_login
        self.img = ImageTk.PhotoImage(Image.open('images/signup.png'))
        tk.Label(self, image=self.img, bg='white').place(x=5, y=140)
        self.frame = ctk.CTkFrame(
            self, width=350, height=550, fg_color="white", bg_color="white")
        self.frame.place(x=480, y=10)
        self.heading = ctk.CTkLabel(self.frame, text="Signup", fg_color="white", bg_color="white", font=("Century Gothic", 28),text_color="#57A1F8")
        self.heading.place(x=130, y=5)

        y = 60
        self.name = self.create_entry(
            "Name", y, on_enter=self.on_enter_name, on_leave=self.on_leave_name)
        y += 65
        self.user = self.create_entry("Username", y, on_enter=self.on_enter_user, on_leave=self.on_leave_user)
        y += 65
        self.email = self.create_entry("Email", y, on_enter=self.on_enter_email, on_leave=self.on_leave_email)
        y += 65
        self.num = self.create_entry("Phone number", y, on_enter=self.on_enter_num, on_leave=self.on_leave_num)
        y += 65
        self.password = self.create_entry(
            "Password", y, on_enter=self.on_enter_pass, on_leave=self.on_leave_pass)
        y += 45

        ctk.CTkButton(self.frame, width=50,height=30, bg_color='white',
                      fg_color="#57A1F8", text_color="white", hover=False, font=("TkDefaultFont", 20), border_width=0, text="Sign up", command=self.sign_up_command).place(x=135, y=y)
        y += 56

        label = ctk.CTkLabel(self.frame, text="Already have an account?",
                             fg_color="white",text_color="black", bg_color="white", font=("TkDefaultFont", 12))
        label.place(x=75, y=y)
        ctk.CTkButton(self.frame, width=6, border_width=0,hover=False,
                                     bg_color="white",font=("TkDefaultFont", 12), cursor='hand2', fg_color="white", text_color="#57A1F8",text="Sign in", command=switch_to_login).place(x=220, y=y)

    def create_entry(self, placeholder, y, on_enter, on_leave):
        entry = ctk.CTkEntry(self.frame, width=350, fg_color="white",
                             bg_color="white",border_width=0,text_color="black", font=("Century Gothic", 20))
        entry.place(x=30, y=y)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        ctk.CTkFrame(self.frame, width=295, height=2,
                     bg_color="black").place(x=25, y=y + 27)
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
                messagebox.showinfo("Caution!", "name should only contain alphabet letters.", parent=self)
                self.name.delete(0, 'end')
                self.name.insert(0, 'Name')

    def on_enter_user(self, e):
        if self.user.get() == 'Username':
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'Username')

    def on_enter_email(self, e):
        if self.email.get() == 'Email':
            self.email.delete(0, 'end')

    def on_leave_email(self, e):
        if self.email.get() == '':
            self.email.insert(0, 'Email')
        else:
            if not SignUp_validation.email_check(self.email.get()):
                messagebox.showinfo("Caution!", "Invalid Email address", parent=self)
                self.email.delete(0, 'end')
                self.email.insert(0, 'Email')

    def on_enter_num(self, e):
        if self.num.get() == 'Phone number':
            self.num.delete(0, 'end')

    def on_leave_num(self, e):
        if self.num.get() == '':
            self.num.insert(0, 'Phone number')
        else:
            s = SignUp_validation.fix(self.num.get())
            if not SignUp_validation.phone_num_validate(s):
                messagebox.showinfo("Caution!", "Phone number should be 11 digits", parent=self)
                self.num.delete(0, 'end')
                self.num.insert(0, 'Phone number')

    def on_enter_pass(self, e):
        if self.password.get() == 'Password':
            self.password.delete(0, 'end')

    def on_leave_pass(self, e):
        if self.password.get() == '':
            self.password.insert(0, 'Password')

    def sign_up_command(self):
        
        b1 = self.name.get() != 'Name' and self.name.get() != '' and SignUp_validation.name_validate(SignUp_validation.fix(self.name.get()))
        b2 = self.user.get() != 'Username' and self.user.get() != '' and check_user_name_available(self.user.get()) 
        b3 = self.email.get() != 'Email' and self.email.get() != '' and SignUp_validation.email_check(self.email.get())
        b4 = self.num.get() != 'Phone number' and self.num.get() != '' and SignUp_validation.phone_num_validate(SignUp_validation.fix(self.num.get()))
        b5 = self.password.get() != 'Password' and self.password.get() != ''

        if b1 and b2 and b3 and b4 and b5:
            user = User(self.user.get(), self.password.get(),
                        self.name.get(), self.email.get(), self.num.get())
            user.user_id = add_user(user)
            self.switch_to_HomePage(user.user_id)
        else:
            messagebox.showinfo('error', "wrong data")
