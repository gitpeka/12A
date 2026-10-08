import tkinter as tk
from tkinter import ttk, messagebox
import config
from sidebar import create_sidebar
from data_manager import get_books, save_books, get_borrowings, save_borrowings
from data_manager import get_users
from ui_helpers import make_button, make_entry, style_treeview

def create_page(parent, app):
    frame=tk.Frame(parent,bg=config.BG_COLOR); frame.pack(fill="both",expand=True)
    create_sidebar(frame,app,"borrowings")
    content=tk.Frame(frame,bg=config.BG_COLOR); content.pack(side="left",fill="both",expand=True)
    tk.Label(content,text="Borrowing Management",bg=config.BG_COLOR,fg=config.TEXT_COLOR,font=(config.FONT,24,"bold")).pack(anchor="w",padx=30,pady=(28,5))
    tk.Label(content,text="Track book loans and returns.",bg=config.BG_COLOR,fg=config.MUTED_TEXT,font=(config.FONT,10)).pack(anchor="w",padx=30)

    toolbar=tk.Frame(content,bg=config.BG_COLOR); toolbar.pack(fill="x",padx=30,pady=18)
    make_button(toolbar,"Borrow Book",lambda: borrow()).pack(side="left")
    make_button(toolbar,"Return Selected",lambda: return_book(),primary=False).pack(side="left",padx=8)

    table_frame=tk.Frame(content,bg=config.WHITE); table_frame.pack(fill="both",expand=True,padx=30,pady=(0,30))
    style_treeview()
    cols=("id","user","book","date","status")
    tree=ttk.Treeview(table_frame,columns=cols,show="headings")
    for c,h,w in [("id","ID",70),("user","User",180),("book","Book",240),("date","Borrowed On",130),("status","Status",110)]:
        tree.heading(c,text=h); tree.column(c,width=w)
    tree.pack(fill="both",expand=True,padx=10,pady=10)

    def refresh():
        for x in tree.get_children(): tree.delete(x)
        for r in get_borrowings():
            tree.insert("", "end", values=(r.get("id"),r.get("username"),r.get("book_title"),r.get("date"),r.get("status")))
    def borrow():
        books=[b for b in get_books() if b.get("status")=="Available"]
        users=get_users()
        if not books:
            messagebox.showwarning("No Books","There are no available books.")
            return
        win=tk.Toplevel(frame); win.title("Borrow Book"); win.geometry("420x400"); win.configure(bg=config.BG_COLOR); win.grab_set()
        tk.Label(win,text="Select User",bg=config.BG_COLOR,fg=config.TEXT_COLOR,font=(config.FONT,10,"bold")).pack(anchor="w",padx=35,pady=(25,4))
        user_var=tk.StringVar(value=users[0]["username"] if users else "")
        uc=ttk.Combobox(win,textvariable=user_var,values=[u["username"] for u in users],state="readonly"); uc.pack(fill="x",padx=35)
        tk.Label(win,text="Select Book",bg=config.BG_COLOR,fg=config.TEXT_COLOR,font=(config.FONT,10,"bold")).pack(anchor="w",padx=35,pady=(20,4))
        book_var=tk.StringVar(value=books[0]["title"])
        bc=ttk.Combobox(win,textvariable=book_var,values=[b["title"] for b in books],state="readonly"); bc.pack(fill="x",padx=35)
        def save():
            import datetime
            selected=next((b for b in books if b["title"]==book_var.get()),None)
            if not selected: return
            records=get_borrowings()
            records.append({"id":f"BR{len(records)+1:03d}","username":user_var.get(),"book_id":selected["id"],"book_title":selected["title"],"date":datetime.date.today().isoformat(),"status":"Borrowed"})
            selected["status"]="Borrowed"; save_books(get_books()); save_borrowings(records); win.destroy(); refresh()
        make_button(win,"Confirm Borrow",save).pack(pady=30)
    def return_book():
        sel=tree.selection()
        if not sel: return
        rid=tree.item(sel[0])["values"][0]
        records=get_borrowings()
        record=next((r for r in records if r["id"]==rid),None)
        if not record or record["status"]!="Borrowed": return
        record["status"]="Returned"
        books=get_books()
        for b in books:
            if b["id"]==record["book_id"]: b["status"]="Available"
        save_borrowings(records); save_books(books); refresh()
    refresh()
    return frame
