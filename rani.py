        tk.Label(self.frame_login, text="Username :", font=("Arial", 10), bg=PINK).pack()
        self.username_entry = tk.Entry(self.frame_login, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.frame_login, text="Password (rahasia banget!):", font=("Arial", 10), bg=PINK).pack()
        self.password_entry = tk.Entry(self.frame_login, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(
            self.frame_login,
            text="🔑 MASUK",
            command=self.cek_login,
            font=("Arial", 10, "bold"),
            bg=CYAN,
            fg="black",
            padx=15,
            pady=5,
            relief=tk.RAISED
        ).pack(pady=15)

    def cek_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "ddrp" and password == "mantap":
            messagebox.showinfo("Yey!", "Login berhasil! Kamu keren! 🎉")
            self.buka_halaman_kelompok()
        else:
            messagebox.showerror("Yah!", "Salah password, coba lagi! 😅")
