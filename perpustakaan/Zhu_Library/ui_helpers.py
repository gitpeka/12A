import tkinter as tk
from tkinter import ttk
import config

def style_treeview():
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure(
        "Treeview",
        background=config.WHITE,
        foreground=config.TEXT_COLOR,
        rowheight=32,
        fieldbackground=config.WHITE,
        font=(config.FONT, 10)
    )
    style.configure(
        "Treeview.Heading",
        background=config.PRIMARY_RED,
        foreground=config.WHITE,
        font=(config.FONT, 10, "bold")
    )
    style.map("Treeview", background=[("selected", "#F3B5B5")], foreground=[("selected", config.TEXT_COLOR)])

def make_button(parent, text, command, primary=True, width=None):
    bg = config.PRIMARY_RED if primary else config.WHITE
    fg = config.WHITE if primary else config.PRIMARY_RED
    active = config.DARK_RED if primary else config.LIGHT_RED
    kwargs = {
        "text": text,
        "command": command,
        "font": (config.FONT, 10, "bold"),
        "bg": bg,
        "fg": fg,
        "activebackground": active,
        "activeforeground": fg if primary else config.PRIMARY_RED,
        "relief": "flat",
        "bd": 0,
        "padx": 16,
        "pady": 9,
        "cursor": "hand2",
    }
    if width:
        kwargs["width"] = width
    return tk.Button(parent, **kwargs)

def make_entry(parent, show=None):
    e = tk.Entry(
        parent,
        font=(config.FONT, 11),
        bg=config.WHITE,
        fg=config.TEXT_COLOR,
        relief="solid",
        bd=1,
        insertbackground=config.TEXT_COLOR
    )
    if show:
        e.configure(show=show)
    return e
