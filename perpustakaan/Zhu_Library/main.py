import tkinter as tk
from tkinter import messagebox
import config
from data_manager import ensure_data
import main_page
import login_page
import signup_page
import home_page
import books_page
import borrowings_page
import users_page

class ZhuLibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        ensure_data()
        self.title(config.APP_NAME)
        self.geometry("1200x720")
        self.minsize(1000, 650)
        self.configure(bg=config.BG_COLOR)
        self.current_user = None
        self.current_frame = None

        self.pages = {
            "main": main_page.create_page,
            "login": login_page.create_page,
            "signup": signup_page.create_page,
            "home": home_page.create_page,
            "books": books_page.create_page,
            "borrowings": borrowings_page.create_page,
            "users": users_page.create_page,
        }
        self.show_page("main")

    def show_page(self, page_name):
        if page_name not in self.pages:
            return
        if page_name == "home" and not self.current_user:
            page_name = "login"
        if page_name in ("books","borrowings","users") and not self.current_user:
            page_name = "login"

        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = self.pages[page_name](self, self)
        self.current_frame.pack(fill="both", expand=True)

    def logout(self):
        self.current_user = None
        self.show_page("main")

if __name__ == "__main__":
    app = ZhuLibraryApp()
    app.mainloop()
