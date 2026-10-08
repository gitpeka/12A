import json
import os
from config import DATA_DIR, USERS_FILE, BOOKS_FILE, BORROWINGS_FILE

DEFAULT_BOOKS = [
    {"id": "B001", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": "1925", "category": "Classic", "status": "Available"},
    {"id": "B002", "title": "1984", "author": "George Orwell", "year": "1949", "category": "Dystopian", "status": "Available"},
    {"id": "B003", "title": "Pride and Prejudice", "author": "Jane Austen", "year": "1813", "category": "Romance", "status": "Available"},
]

def ensure_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_FILE):
        save_json(USERS_FILE, [])
    if not os.path.exists(BOOKS_FILE):
        save_json(BOOKS_FILE, DEFAULT_BOOKS)
    if not os.path.exists(BORROWINGS_FILE):
        save_json(BORROWINGS_FILE, [])

def load_json(path, default):
    ensure_data()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default

def save_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_users():
    return load_json(USERS_FILE, [])

def save_users(data):
    save_json(USERS_FILE, data)

def get_books():
    return load_json(BOOKS_FILE, DEFAULT_BOOKS)

def save_books(data):
    save_json(BOOKS_FILE, data)

def get_borrowings():
    return load_json(BORROWINGS_FILE, [])

def save_borrowings(data):
    save_json(BORROWINGS_FILE, data)
