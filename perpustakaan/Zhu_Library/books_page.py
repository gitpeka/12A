import tkinter as tk
from tkinter import ttk, messagebox
import config
from sidebar import create_sidebar
from data_manager import get_books, save_books
from ui_helpers import make_button, make_entry, style_treeview

def create_page(parent, app):
    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="both", expand=True)
    create_sidebar(frame, app, "books")

    content = tk.Frame(frame, bg=config.BG_COLOR)
    content.pack(side="left", fill="both", expand=True)
    tk.Label(content, text="Book Management", bg=config.BG_COLOR, fg=config.TEXT_COLOR,
             font=(config.FONT, 24, "bold")).pack(anchor="w", padx=30, pady=(28,5))
    tk.Label(content, text="Add, edit, remove, and view library books.", bg=config.BG_COLOR,
             fg=config.MUTED_TEXT, font=(config.FONT, 10)).pack(anchor="w", padx=30)

    toolbar = tk.Frame(content, bg=config.BG_COLOR)
    toolbar.pack(fill="x", padx=30, pady=18)
    search = make_entry(toolbar)
    search.pack(side="left", fill="x", expand=True, ipady=7)
    search.insert(0, "")
    make_button(toolbar, "Search", lambda: refresh()).pack(side="left", padx=8)
    make_button(toolbar, "Add Book", lambda: add_book()).pack(side="left")

    table_frame = tk.Frame(content, bg=config.WHITE)
    table_frame.pack(fill="both", expand=True, padx=30, pady=(0,30))
    style_treeview()
    cols = ("id","title","author","year","category","status")
    tree = ttk.Treeview(table_frame, columns=cols, show="headings")
    headings = {"id":"ID","title":"Title","author":"Author","year":"Year","category":"Category","status":"Status"}
    widths = {"id":70,"title":220,"author":180,"year":70,"category":130,"status":100}
    for c in cols:
        tree.heading(c, text=headings[c])
        tree.column(c, width=widths[c], anchor="w")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh():
        for item in tree.get_children(): tree.delete(item)
        query = search.get().strip().lower()
        for b in get_books():
            if query and query not in " ".join(str(b.get(k,"")) for k in cols).lower(): continue
            tree.insert("", "end", values=tuple(b.get(c,"") for c in cols))

    def add_book():
        win = tk.Toplevel(frame); win.title("Add Book"); win.geometry("400x450"); win.configure(bg=config.BG_COLOR); win.grab_set()
        entries = {}
        for label, key in [("Title","title"),("Author","author"),("Year","year"),("Category","category")]:
            tk.Label(win,text=label,bg=config.BG_COLOR,fg=config.TEXT_COLOR,font=(config.FONT,10,"bold")).pack(anchor="w",padx=35,pady=(18,3))
            e=make_entry(win); e.pack(fill="x",padx=35,ipady=6); entries[key]=e
        def save():
            if not entries["title"].get().strip() or not entries["author"].get().strip():
                messagebox.showwarning("Missing Information","Title and author are required.",parent=win); return
            books=get_books()
            books.append({"id":f"B{len(books)+1:03d}","title":entries["title"].get().strip(),"author":entries["author"].get().strip(),"year":entries["year"].get().strip(),"category":entries["category"].get().strip(),"status":"Available"})
            save_books(books); win.destroy(); refresh()
        make_button(win,"Save Book",save).pack(pady=25)
    def delete_book():
        sel=tree.selection()
        if not sel: return
        bid=tree.item(sel[0])["values"][0]
        books=[b for b in get_books() if b["id"] != bid]
        save_books(books); refresh()
    make_button(content,"Delete Selected",delete_book,primary=False).pack(anchor="e",padx=30,pady=(0,15))
    refresh()
    return frame
