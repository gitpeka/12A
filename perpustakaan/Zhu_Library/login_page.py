import tkinter as tk
from tkinter import messagebox
import config
from data_manager import get_users
from ui_helpers import make_button, make_entry

def create_page(parent, app):
    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="both", expand=True)

    box = tk.Frame(frame, bg=config.WHITE, highlightbackground=config.BORDER_COLOR, highlightthickness=1)
    box.place(relx=0.5, rely=0.5, anchor="center", width=410, height=430)

    tk.Label(box, text="Welcome Back", bg=config.WHITE, fg=config.TEXT_COLOR,
             font=(config.FONT, 23, "bold")).pack(pady=(38, 5))
    tk.Label(box, text="Log in to Zhu Library", bg=config.WHITE, fg=config.MUTED_TEXT,
             font=(config.FONT, 10)).pack(pady=(0, 25))

    tk.Label(box, text="Username or Email", bg=config.WHITE, fg=config.TEXT_COLOR,
             font=(config.FONT, 10, "bold")).pack(anchor="w", padx=48)
    user_entry = make_entry(box)
    user_entry.pack(fill="x", padx=48, pady=(5, 15), ipady=7)

    tk.Label(box, text="Password", bg=config.WHITE, fg=config.TEXT_COLOR,
             font=(config.FONT, 10, "bold")).pack(anchor="w", padx=48)
    pass_entry = make_entry(box, show="*")
    pass_entry.pack(fill="x", padx=48, pady=(5, 20), ipady=7)

    def login():
        identifier = user_entry.get().strip()
        password = pass_entry.get()
        for user in get_users():
            if (user.get("username", "").lower() == identifier.lower() or
                user.get("email", "").lower() == identifier.lower()) and user.get("password") == password:
                app.current_user = user
                app.show_page("home")
                return
        messagebox.showerror("Login Failed", "Incorrect username/email or password.")

    make_button(box, "Log In", login).pack(fill="x", padx=48)
    make_button(box, "Back", lambda: app.show_page("main"), primary=False).pack(fill="x", padx=48, pady=8)

    return frame
