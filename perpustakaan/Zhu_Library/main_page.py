import tkinter as tk
import config
from ui_helpers import make_button

NEWS_TEXT = """LIBRARY NEWS

Welcome to Zhu Library.

• New books are added regularly.
• Keep your borrowed books in good condition.
• Check due dates before leaving the library.
• Use the management pages to keep the library organized."""

TIPS_TEXT = """TIPS & TRICKS

• Search by title, author, or category.
• Return books on time to keep them available.
• Use short, clear book records.
• Keep your account information secure."""

def create_page(parent, app):
    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="both", expand=True)

    left = tk.Frame(frame, bg=config.PRIMARY_RED, width=460)
    left.pack(side="left", fill="both")
    left.pack_propagate(False)

    tk.Label(left, text="ZHU LIBRARY", bg=config.PRIMARY_RED, fg=config.WHITE,
             font=(config.FONT, 28, "bold")).pack(anchor="w", padx=42, pady=(55, 8))
    tk.Label(left, text="A simple place for every story.", bg=config.PRIMARY_RED, fg="#FFEAEA",
             font=(config.FONT, 12)).pack(anchor="w", padx=42, pady=(0, 35))

    card = tk.Frame(left, bg=config.WHITE)
    card.pack(fill="x", padx=42, pady=10)

    tk.Label(card, text="Library News", bg=config.WHITE, fg=config.PRIMARY_RED,
             font=(config.FONT, 16, "bold")).pack(anchor="w", padx=18, pady=(18, 8))
    tk.Label(card, text=NEWS_TEXT, justify="left", wraplength=340, bg=config.WHITE,
             fg=config.TEXT_COLOR, font=(config.FONT, 10), padx=18, pady=10).pack(anchor="w")

    tk.Label(left, text=TIPS_TEXT, justify="left", wraplength=365, bg=config.PRIMARY_RED,
             fg="#FFEAEA", font=(config.FONT, 10), padx=42, pady=25).pack(anchor="w")

    right = tk.Frame(frame, bg=config.BG_COLOR)
    right.pack(side="left", fill="both", expand=True)

    center = tk.Frame(right, bg=config.BG_COLOR)
    center.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(center, text="Welcome to Zhu Library", bg=config.BG_COLOR, fg=config.TEXT_COLOR,
             font=(config.FONT, 25, "bold")).pack()
    tk.Label(center, text="Sign in to manage your library or create a new account.",
             bg=config.BG_COLOR, fg=config.MUTED_TEXT, font=(config.FONT, 11)).pack(pady=(8, 28))

    make_button(center, "Log In", lambda: app.show_page("login"), width=24).pack(pady=6)
    make_button(center, "Create an Account", lambda: app.show_page("signup"),
                primary=False, width=24).pack(pady=6)

    tk.Label(right, text="Zhu Library • Library Management System",
             bg=config.BG_COLOR, fg="#999999", font=(config.FONT, 9)).pack(side="bottom", pady=20)

    return frame
