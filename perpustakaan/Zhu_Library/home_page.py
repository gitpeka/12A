import tkinter as tk
import config
from main_page import NEWS_TEXT, TIPS_TEXT
from sidebar import create_sidebar
from data_manager import get_books, get_borrowings

def create_page(parent, app):
    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="both", expand=True)
    create_sidebar(frame, app, "home")

    content = tk.Frame(frame, bg=config.BG_COLOR)
    content.pack(side="left", fill="both", expand=True)

    top = tk.Frame(content, bg=config.BG_COLOR)
    top.pack(fill="x", padx=35, pady=(28, 10))
    user_name = app.current_user.get("name", "Member") if app.current_user else "Member"
    tk.Label(top, text=f"Welcome, {user_name}", bg=config.BG_COLOR, fg=config.TEXT_COLOR,
             font=(config.FONT, 24, "bold")).pack(side="left")
    tk.Label(top, text="Your library dashboard", bg=config.BG_COLOR, fg=config.MUTED_TEXT,
             font=(config.FONT, 10)).pack(side="left", padx=15, pady=(10,0))

    books = get_books()
    borrowings = get_borrowings()
    stats = tk.Frame(content, bg=config.BG_COLOR)
    stats.pack(fill="x", padx=35, pady=15)
    for title, value in [("Books", len(books)), ("Borrowed", len([x for x in borrowings if x.get("status") == "Borrowed"])), ("Available", len([x for x in books if x.get("status") == "Available"]))]:
        card = tk.Frame(stats, bg=config.WHITE, highlightbackground=config.BORDER_COLOR, highlightthickness=1)
        card.pack(side="left", fill="x", expand=True, padx=(0, 12))
        tk.Label(card, text=title, bg=config.WHITE, fg=config.MUTED_TEXT, font=(config.FONT, 10)).pack(anchor="w", padx=18, pady=(15,2))
        tk.Label(card, text=str(value), bg=config.WHITE, fg=config.PRIMARY_RED, font=(config.FONT, 22, "bold")).pack(anchor="w", padx=18, pady=(0,15))

    body = tk.Frame(content, bg=config.BG_COLOR)
    body.pack(fill="both", expand=True, padx=35, pady=10)

    for heading, text in [("Library News", NEWS_TEXT), ("Tips & Tricks", TIPS_TEXT)]:
        card = tk.Frame(body, bg=config.WHITE, highlightbackground=config.BORDER_COLOR, highlightthickness=1)
        card.pack(fill="x", pady=8)
        tk.Label(card, text=heading, bg=config.WHITE, fg=config.PRIMARY_RED,
                 font=(config.FONT, 16, "bold")).pack(anchor="w", padx=20, pady=(18, 5))
        tk.Label(card, text=text, bg=config.WHITE, fg=config.TEXT_COLOR, justify="left",
                 font=(config.FONT, 10), wraplength=700).pack(anchor="w", padx=20, pady=(0,18))

    return frame
