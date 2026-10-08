import tkinter as tk
from tkinter import messagebox
import config
from data_manager import get_users, save_users
from ui_helpers import make_button, make_entry

def create_page(parent, app):
    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="both", expand=True)

    box = tk.Frame(frame, bg=config.WHITE, highlightbackground=config.BORDER_COLOR, highlightthickness=1)
    box.place(relx=0.5, rely=0.5, anchor="center", width=440, height=555)

    tk.Label(box, text="Create Account", bg=config.WHITE, fg=config.TEXT_COLOR,
             font=(config.FONT, 23, "bold")).pack(pady=(30, 5))
    tk.Label(box, text="Join Zhu Library", bg=config.WHITE, fg=config.MUTED_TEXT,
             font=(config.FONT, 10)).pack(pady=(0, 18))

    fields = {}
    for label, key in [("Full Name", "name"), ("Username", "username"), ("Email", "email"), ("Password", "password")]:
        tk.Label(box, text=label, bg=config.WHITE, fg=config.TEXT_COLOR,
                 font=(config.FONT, 10, "bold")).pack(anchor="w", padx=48)
        entry = make_entry(box, show="*" if key == "password" else None)
        entry.pack(fill="x", padx=48, pady=(4, 10), ipady=6)
        fields[key] = entry

    def signup():
        name = fields["name"].get().strip()
        username = fields["username"].get().strip()
        email = fields["email"].get().strip()
        password = fields["password"].get()

        if not all([name, username, email, password]):
            messagebox.showwarning("Missing Information", "Please complete every field.")
            return

        users = get_users()
        if any(u.get("username", "").lower() == username.lower() for u in users):
            messagebox.showerror("Sign Up Failed", "That username is already in use.")
            return
        if any(u.get("email", "").lower() == email.lower() for u in users):
            messagebox.showerror("Sign Up Failed", "That email is already registered.")
            return

        new_user = {
            "id": f"U{len(users)+1:03d}",
            "name": name,
            "username": username,
            "email": email,
            "password": password,
            "role": "Member"
        }
        users.append(new_user)
        save_users(users)
        messagebox.showinfo("Account Created", "Your account has been created. You can now log in.")
        app.show_page("login")

    make_button(box, "Create Account", signup).pack(fill="x", padx=48, pady=(4, 5))
    make_button(box, "Back", lambda: app.show_page("main"), primary=False).pack(fill="x", padx=48)

    return frame
