import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="white")
        self.heading = tk.Label(self, text="Signup", fg="#57A1F8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        self.heading.place(x=50, y=50)  # Adjusted coordinates

app = tk.Tk()
app.current_page = LoginPage(app)
app.current_page.pack(fill="both", expand=True)
app.mainloop()
