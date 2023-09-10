import tkinter as tk
from tkinter import PhotoImage, messagebox
import Signup
from User import User
from db import *
from validators import SignUp_validation

class SignupPage(tk.Frame):
    def __init__(self, parent,switch_to_login, switch_to_HomePage ):
        super().__init__(parent,bg="white")
        self.switch_to_HomePage=switch_to_HomePage
        self.switch_to_loginn=switch_to_login
        self.img = tk.PhotoImage(file='images\signup.png')
        tk.Label(self, image=self.img, bg='white').place(x=50, y=50)
        self.frame = tk.Frame(self, width=350, height=550, bg="white")
        self.frame.place(x=480, y=10)
        self.heading = tk.Label(self.frame, text="Signup", fg="#57A1F8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        self.heading.place(x=100, y=5)

        y = 80
        self.name = self.create_entry("Name", y, on_enter=self.on_enter_name, on_leave=self.on_leave_name)
        y += 65
        self.user = self.create_entry("Username", y, on_enter=self.on_enter_user, on_leave=self.on_leave_user)
        y += 65
        self.email = self.create_entry("Email", y, on_enter=self.on_enter_email, on_leave=self.on_leave_email)
        y += 65
        self.num = self.create_entry("Phone number", y, on_enter=self.on_enter_num, on_leave=self.on_leave_num)
        y += 65
        self.password = self.create_entry("Password", y, on_enter=self.on_enter_pass, on_leave=self.on_leave_pass)
        y += 45

        tk.Button(self.frame, width=39, pady=7, text="Sign up", bg='#57A1F8', fg="white", border=0, command= self.sign_up_command).place(x=35, y=y)
        y += 56

        label = tk.Label(self.frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
        label.place(x=75, y=y)
        tk.Button(self.frame, width=6, text="Sign in", border=0, bg="white", cursor='hand2', fg="#57A1F8", command=  switch_to_login).place(x=220, y=y)

    def create_entry(self, placeholder, y, on_enter, on_leave):
        entry = tk.Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        entry.place(x=30, y=y)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        tk.Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=y + 27)
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
        
        if b1 and b2  and b3 and b4 and b5:
            user=User(self.user.get(),self.password.get(),self.name.get(),self.email.get(),self.num.get())
            user.user_id=add_user(user)
            self.switch_to_HomePage(user.user_id) 
        else:    
            messagebox.showinfo( 'error',"wrong data")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SignupPage(root,1)
#     app.pack(fill="both", expand=True)
#     root.mainloop()
