ZHU LIBRARY
===========

A red-and-white library management app built with Python Tkinter.

REQUIREMENTS
------------
- Python 3.9+ recommended
- Tkinter (normally included with standard Python installations)
- No third-party packages are required

RUN
---
Open a terminal in this folder and run:

    python main.py

DATA
----
The app automatically creates a "data" folder containing:
- users.json
- books.json
- borrowings.json

Accounts created through Sign Up are stored in users.json.
Books and borrowing records are also persisted in JSON.

FILES
-----
main.py              Main application and page routing
config.py            Universal colors, fonts, paths, and settings
data_manager.py      JSON storage and data helpers
ui_helpers.py        Reusable UI components
main_page.py         Public landing page
login_page.py        Login page
signup_page.py       Signup page
home_page.py         Logged-in homepage
sidebar.py           Shared vertical navigation
books_page.py        Book management
borrowings_page.py   Borrowing management
users_page.py        User management

SECURITY NOTE
-------------
This is a local educational/demo application. Passwords are stored as plain
text in JSON, so this design should NOT be used for a real production system.
For a real deployment, passwords should be securely hashed and authenticated
against a proper database.
