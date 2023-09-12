import customtkinter as ctk
from tkinter import PhotoImage
from tkinter import messagebox
import Signup
from db import validate_login


class LoginPage(ctk.CTkFrame):
    def __init__(self, root, switch_to_Signup, switch_to_HomePage):
        self.switch_to_HomePage = switch_to_HomePage
        super().__init__(root, fg_color="white")
        self.user_id = None
        self.img = PhotoImage(file='images\login.png')
        ctk.CTkLabel(self, image=self.img, bg_color='white',
                     text="").place(x=10, y=110)
        self.frame = ctk.CTkFrame(
            self, width=350, height=350, fg_color="white")
        self.frame.place(x=480, y=70)
        self.heading = ctk.CTkLabel(self.frame, text="Login", text_color="#57A1F8", fg_color="white", bg_color="white", font=(
            "Century Gothic", 28))
        self.heading.place(x=150, y=10)
        self.user = ctk.CTkEntry(self.frame, width=350, fg_color="white", border_width=0,
                                 bg_color="white", font=("Century Gothic", 20))
        x = 50
        y = 80
        self.user.place(x=x-2, y=y)
        y += 40
        self.user.insert(0, "Username")
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        ctk.CTkFrame(self.frame, width=310, height=1.5,
                     bg_color="black", fg_color="black").place(x=x, y=y)

        self.password = ctk.CTkEntry(self.frame, width=350, fg_color="white", border_width=0,
                                     bg_color="white", font=("Century Gothic", 20))
        y += 30
        self.password.place(x=x-2, y=y)
        y += 40
        self.password.insert(0, "Password")
        self.password.bind('<FocusIn>', self.on_enter_pass)
        self.password.bind('<FocusOut>', self.on_leave_pass)
        ctk.CTkFrame(self.frame, width=310, height=1.5,
                     bg_color="black", fg_color="black").place(x=x, y=y)

        ctk.CTkButton(self.frame, width=39,  text="Sign in", bg_color='white',
                      fg_color="#57A1F8", text_color="white", font=("TkDefaultFont", 20), border_width=0,
                      command=self.loginlogic, hover=False).place(x=x+100, y=225)

        self.label = ctk.CTkLabel(self.frame, text="Don't have an account?",
                                  fg_color="white", text_color="black", bg_color="white", font=("TkDefaultFont", 12))
        self.label.place(x=100, y=270)

        self.sign_up = ctk.CTkButton(self.frame, width=6, text="Sign up", border_width=0,hover=False,
                                     bg_color="white",font=("TkDefaultFont", 12), cursor='hand2', fg_color="white", text_color="#57A1F8", command=switch_to_Signup)
        self.sign_up.place(x=225, y=271)

    def loginlogic(self):
        if self.checkuser() is not None:
            self.switch_to_HomePage(self.user_id[0])
        else:
            messagebox.showinfo('error', "wrong username or password")

    def checkuser(self):

        self.password.get()
        self.user_id = validate_login(self.user.get(), self.password.get())
        return self.user_id

    def on_enter_user(self, e):
        if self.user.get() == "Username":
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'Username')

    def on_enter_pass(self, e):
        if self.password.get() == "Password":
            self.password.delete(0, 'end')

    def on_leave_pass(self, e):
        if self.password.get() == '':
            self.password.insert(0, 'Password')

    def sign_up_command(self):
        Signup_window = ctk.Toplevel(self.root)
        Signup.Sign_up_def(Signup_window)
        self.root.withdraw()
