import tkinter as tk
from tkinter import ttk, messagebox
import config
from sidebar import create_sidebar
from data_manager import get_users, save_users
from ui_helpers import make_button, style_treeview

def create_page(parent, app):
    frame=tk.Frame(parent,bg=config.BG_COLOR); frame.pack(fill="both",expand=True)
    create_sidebar(frame,app,"users")
    content=tk.Frame(frame,bg=config.BG_COLOR); content.pack(side="left",fill="both",expand=True)
    tk.Label(content,text="Users Management",bg=config.BG_COLOR,fg=config.TEXT_COLOR,font=(config.FONT,24,"bold")).pack(anchor="w",padx=30,pady=(28,5))
    tk.Label(content,text="View and manage registered library users.",bg=config.BG_COLOR,fg=config.MUTED_TEXT,font=(config.FONT,10)).pack(anchor="w",padx=30,pady=(0,18))
    table_frame=tk.Frame(content,bg=config.WHITE); table_frame.pack(fill="both",expand=True,padx=30,pady=(0,20))
    style_treeview()
    cols=("id","name","username","email","role")
    tree=ttk.Treeview(table_frame,columns=cols,show="headings")
    for c,h,w in [("id","ID",70),("name","Full Name",180),("username","Username",140),("email","Email",230),("role","Role",100)]:
        tree.heading(c,text=h); tree.column(c,width=w)
    tree.pack(fill="both",expand=True,padx=10,pady=10)
    def refresh():
        for x in tree.get_children(): tree.delete(x)
        for u in get_users():
            tree.insert("", "end", values=(u.get("id"),u.get("name"),u.get("username"),u.get("email"),u.get("role")))
    def delete_user():
        sel=tree.selection()
        if not sel: return
        uid=tree.item(sel[0])["values"][0]
        if app.current_user and uid==app.current_user.get("id"):
            messagebox.showwarning("Not Allowed","You cannot delete the account currently in use.")
            return
        if messagebox.askyesno("Delete User","Delete this user account?"):
            save_users([u for u in get_users() if u["id"] != uid]); refresh()
    make_button(content,"Delete Selected",delete_user,primary=False).pack(anchor="e",padx=30,pady=(0,30))
    refresh()
    return frame
