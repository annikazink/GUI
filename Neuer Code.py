import tkinter as tk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.attributes('-fullscreen', True)  # Starte im Vollbildmodus

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        # Füge den Schließen-Button hinzu
        close_button = tk.Button(self, text="X", command=self.quit, font=("Arial", 12), width=2, height=1)
        close_button.place(relx=1, rely=0, anchor=tk.NE)

        self.create_kompressor_ipt_buttons(kompressor_ipt_frame)
        self.create_kompressor_ostfalia_buttons(kompressor_ostfalia_frame)

    def create_kompressor_ipt_buttons(self, frame):
        tk.Button(frame, text="Status Sensoren", font=("Arial", 12), width=20, height=3).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Energieverbrauch", font=("Arial", 12), width=20, height=3).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="Temperaturen", font=("Arial", 12), width=20, height=3).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(frame, text="Systemdruck", font=("Arial", 12), width=20, height=3).grid(row=0, column=4, padx=10, pady=5)
        tk.Button(frame, text="Historische Daten", font=("Arial", 12), width=20, height=3).grid(row=0, column=5, padx=10, pady=5)

    def create_kompressor_ostfalia_buttons(self, frame):
        tk.Button(frame, text="Energieverbräuche", font=("Arial", 12), width=20, height=3).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="Historische Daten", font=("Arial", 12), width=20, height=3).grid(row=0, column=2, padx=10, pady=5)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
