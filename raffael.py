import tkinter as tk
from tkinter import messagebox

# Warna
PINK = "#FFC0CB"
LILAC = "#C8A2C8"
CYAN = "#00FFFF"

# Ukuran layar mobile
screen_width = 360
screen_height = 640

class AplikasiLogin:
    def _init_(self, root):  # ← ini dua underscore ya
        self.root = root
        self.root.title("Login Lucu")
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg=PINK)
        self.root.resizable(False, False)

        self.buat_frame_login()

    def buat_frame_login(self):
        self.frame_login = tk.Frame(self.root, bg=PINK)
        self.frame_login.pack(expand=True)

        tk.Label(
            self.frame_login,
            text="🎪 LOGIN 🎪",
            font=("Comic Sans MS", 18, "bold"),
            bg=PINK,
            fg="purple"
        ).pack(pady=10)
