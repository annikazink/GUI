import tkinter as tk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

    def create_kompressor_ipt_page(self):
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        tk.Button(kompressor_ipt_frame, text="Status Sensoren").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Energieverbrauch").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Temperaturen").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Messwerte").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Systemdruck").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Historische Daten").pack(pady=5, padx=10, side=tk.LEFT)

    def create_kompressor_ostfalia_page(self):
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        tk.Button(kompressor_ostfalia_frame, text="Energieverbräuche").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Messwerte").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Historische Daten").pack(pady=5, padx=10, side=tk.LEFT)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
