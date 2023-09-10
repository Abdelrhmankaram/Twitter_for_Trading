import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import Signup
from db import validate_login


class LoginPage(tk.Frame):
    def __init__(self, root, switch_to_Signup, switch_to_HomePage):
        self.switch_to_HomePage = switch_to_HomePage
        super().__init__(root, bg="white")
        self.user_id = None
        self.img = PhotoImage(file='images\login.png')
        tk.Label(self, image=self.img, bg='white').place(x=50, y=50)
        self.frame = tk.Frame(self, width=500, height=500, bg="white")
        self.frame.place(x=680, y=70)
        self.heading = tk.Label(self.frame, text="Login", fg="#57A1F8", bg="white", font=(
            "Microsoft YaHei UI Light", 28, "bold"))
        self.heading.place(x=110, y=5)
        self.user = tk.Entry(self.frame, width=25, fg="black", border=0,
                             bg="white", font=("Microsoft YaHei UI Light", 15))
        self.user.place(x=35, y=90)
        self.user.insert(0, "Username")
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        tk.Frame(self.frame, width=315, height=2,
                 bg="black").place(x=30, y=125)

        self.password = tk.Entry(self.frame, width=25, fg="black",
                                 border=0, bg="white", font=("Microsoft YaHei UI Light", 15))
        self.password.place(x=35, y=165)
        self.password.insert(0, "Password")
        self.password.bind('<FocusIn>', self.on_enter_pass)
        self.password.bind('<FocusOut>', self.on_leave_pass)
        tk.Frame(self.frame, width=315, height=2,
                 bg="black").place(x=30, y=200)

        tk.Button(self.frame, width=33,height=1, pady=7, text="Sign in", bg='#57A1F8',
                  fg="white", border=0, command=self.loginlogic,font=("TkDefaultFont", 12)).place(x=36, y=230)

        self.label = tk.Label(self.frame, text="Don't have an account?",
                              fg="black", bg="white", font=("Microsoft YaHei UI Light", 12))
        self.label.place(x=35, y=300)

        self.sign_up = tk.Button(self.frame, width=6, text="Sign up", border=0, font=("Microsoft YaHei UI Light", 12),
                                 bg="white", cursor='hand2', fg="#57A1F8", command=switch_to_Signup)
        self.sign_up.place(x=215, y=299)

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
        Signup_window = tk.Toplevel(self.root)
        Signup.Sign_up_def(Signup_window)
        self.root.withdraw()
