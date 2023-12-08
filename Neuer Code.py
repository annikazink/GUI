import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.current_frame = None  # Aktuell angezeigtes Frame

        self.home_page()

    def home_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self)
        self.current_frame.pack()

        tk.Button(self.current_frame, text="Kompressor IPT", command=self.kompressor_ipt_page).pack()
        tk.Button(self.current_frame, text="Kompressor Ostfalia", command=self.kompressor_ostfalia_page).pack()

    def kompressor_ipt_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self)
        self.current_frame.pack()

        tk.Button(self.current_frame, text="Status Sensoren").pack()
        tk.Button(self.current_frame, text="Energieverbrauch").pack()
        tk.Button(self.current_frame, text="Temperaturen").pack()
        tk.Button(self.current_frame, text="Messwerte").pack()
        tk.Button(self.current_frame, text="Systemdruck").pack()
        tk.Button(self.current_frame, text="Historische Daten").pack()

        tk.Button(self.current_frame, text="Zurück", command=self.home_page).pack()

    def kompressor_ostfalia_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self)
        self.current_frame.pack()

        tk.Button(self.current_frame, text="Energieverbräuche").pack()
        tk.Button(self.current_frame, text="Messwerte").pack()
        tk.Button(self.current_frame, text="Historische Daten").pack()

        tk.Button(self.current_frame, text="Zurück", command=self.home_page).pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
