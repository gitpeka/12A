import tkinter as tk
import config
from ui_helpers import make_button

def create_sidebar(parent, app, active):
    side = tk.Frame(parent, bg=config.PRIMARY_RED, width=210)
    side.pack(side="left", fill="y")
    side.pack_propagate(False)

    tk.Label(side, text="ZHU\nLIBRARY", bg=config.PRIMARY_RED, fg=config.WHITE,
             font=(config.FONT, 20, "bold"), justify="left").pack(anchor="w", padx=25, pady=(30, 40))

    items = [
        ("Home", "home"),
        ("Book Management", "books"),
        ("Borrowing Management", "borrowings"),
        ("Users Management", "users"),
    ]
    for label, page in items:
        bg = config.DARK_RED if page == active else config.PRIMARY_RED
        btn = tk.Button(side, text=label, command=lambda p=page: app.show_page(p),
                        bg=bg, fg=config.WHITE, activebackground=config.DARK_RED,
                        activeforeground=config.WHITE, relief="flat", bd=0,
                        font=(config.FONT, 10, "bold"), anchor="w",
                        padx=25, pady=13, cursor="hand2")
        btn.pack(fill="x")

    tk.Label(side, text="Library Management System", bg=config.PRIMARY_RED, fg="#FFDADA",
             font=(config.FONT, 8), wraplength=160, justify="left").pack(side="bottom", anchor="w", padx=25, pady=75)

    logout = tk.Button(side, text="Log Out", command=app.logout,
                       bg=config.WHITE, fg=config.PRIMARY_RED,
                       activebackground=config.LIGHT_RED, activeforeground=config.PRIMARY_RED,
                       relief="flat", bd=0, font=(config.FONT, 9, "bold"),
                       cursor="hand2", padx=10, pady=8)
    logout.pack(side="bottom", fill="x", padx=25, pady=25)

    return side
