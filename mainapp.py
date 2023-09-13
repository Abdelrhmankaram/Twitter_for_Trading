import customtkinter as ctk
from Browse_products import BrowseProductsPage
from Signup import SignupPage
from Login import LoginPage
from add_product import AddProductPage
from select_cat import CategoryPage
from home_page import HomePage
from user_product import UserProductsPage
from PIL import Image, ImageTk
import ctypes

myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Twitter")
        self.geometry("950x500+300+200")
        self.config(background="white")
        self.icon = Image.open("images\wittericon.ico")
        self.icon = ImageTk.PhotoImage(self.icon)
 
        # Set the taskbar icon
        self.iconphoto(True, self.icon)
        self.iconbitmap('images\wittericon.ico')
        self.resizable(False, False)
        self.current_page = None

        self.switch_to_login()

    def switch_to_login(self):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = LoginPage(
            self, self.switch_to_Signup, self.switch_to_HomePage)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_Signup(self):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = SignupPage(
            self, self.switch_to_login, self.switch_to_HomePage)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_HomePage(self, user_id):
        if self.current_page is not None:
            self.current_page.destroy()
        self.current_page = HomePage(self, self.switch_to_login, self.switch_to_CategoryPage,
                                     self.switch_to_AddProductPage, user_id, self.switch_to_UserProductsPage)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_CategoryPage(self, user_id):
        if self.current_page is not None:
            self.current_page.destroy()
        self.current_page = CategoryPage(
            self, self.switch_to_HomePage, self.switch_to_BrowseProductsPage, user_id)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_AddProductPage(self, user_id):
        if self.current_page is not None:
            self.current_page.destroy() 
        self.current_page = AddProductPage(
            self, self.switch_to_HomePage, user_id)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_BrowseProductsPage(self, user_id, category):
        self.current_page.destroy()
        self.current_page = BrowseProductsPage(
            self, self.switch_to_CategoryPage, user_id, category)
        self.current_page.pack(fill="both", expand=True)

    def switch_to_UserProductsPage(self, user_id):
        self.current_page.destroy()
        self.current_page = UserProductsPage(
            self, self.switch_to_HomePage, user_id)
        self.current_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    app=App();
    
    app.mainloop()
