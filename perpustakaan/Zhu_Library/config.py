import os
# Zhu Library - universal configuration

APP_NAME = "Zhu Library"

# Universal colors
BG_COLOR = "#FFF8F8"
WHITE = "#FFFFFF"
PRIMARY_RED = "#B71C1C"
DARK_RED = "#7F0000"
LIGHT_RED = "#FDECEC"
ACCENT_RED = "#E53935"
TEXT_COLOR = "#252525"
MUTED_TEXT = "#666666"
BORDER_COLOR = "#E5BDBD"

FONT = "Segoe UI"
TITLE_SIZE = 28
HEADING_SIZE = 20
BODY_SIZE = 11

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
BORROWINGS_FILE = os.path.join(DATA_DIR, "borrowings.json")
