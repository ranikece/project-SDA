for nama in anggota:
            tk.Label(center_frame, text=nama, font=("Arial", 11), bg=LILAC).pack(pady=2)

        tk.Button(
            center_frame,
            text="🚪 KELUAR",
            command=self.root.destroy,
            font=("Arial", 10, "bold"),
            bg="lightyellow",
            fg="black",
            padx=15,
            pady=5
        ).pack(pady=20)

# Jalankan aplikasi
if __name__ == "__main__":  # ← dua underscore ya
    root = tk.Tk()
    app = AplikasiLogin(root)
    root.mainloop()
