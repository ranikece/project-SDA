def buka_halaman_kelompok(self):
        self.frame_login.destroy()

        self.frame_kelompok = tk.Frame(self.root, bg=LILAC)
        self.frame_kelompok.pack(fill="both", expand=True)

        center_frame = tk.Frame(self.frame_kelompok, bg=LILAC)
        center_frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(
            center_frame,
            text="TIM HEBAT",
            font=("Comic Sans MS", 16, "bold"),
            bg=LILAC,
            fg="darkblue"
        ).pack(pady=10)

        anggota = [
            "Dian Fitriani",
            "Dinar Aisa Artika",
            "Muhammad Raffael",
            "Putri Maharani"
        ]
