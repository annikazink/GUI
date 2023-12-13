import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.attributes("-fullscreen", True)  # Starte im Vollbildmodus

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        # Füge den Schließen-Button hinzu
        close_button = tk.Button(
            self, text="X", command=self.quit, font=("Arial", 12), width=2, height=1
        )
        close_button.place(relx=1, rely=0, anchor=tk.NE)

        self.create_kompressor_ipt_buttons(kompressor_ipt_frame)
        self.create_kompressor_ostfalia_buttons(kompressor_ostfalia_frame)

        # Frame für Sensorstatus in der Mitte des Bildschirms
        self.sensor_status_frame = tk.Frame(self)
        self.sensor_status_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Labels für die Sensorwerte
        self.sensor_labels = {
            "Druck": tk.Label(self.sensor_status_frame, text="", font=("Arial", 12)),
            "Durchfluss": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
            "Temperatur 1": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
            "Temperatur 2": tk.Label(
                self.sensor_status_frame, text="", font=("Arial", 12)
            ),
        }

        # Platzierung der Sensorlabels
        for idx, (key, label) in enumerate(self.sensor_labels.items()):
            label.pack(padx=10, pady=5, anchor=tk.W)

    def create_kompressor_ipt_buttons(self, frame):
        def show_sensor_status():
            # Hier sollen die Daten aus der Datenbank abgerufen werden
            # Beispiel: Annahme, dass die Daten in einer Liste sind
            sensor_data = {
                "Druck": "100 PSI",
                "Durchfluss": "50 L/min",
                "Temperatur 1": "25°C",
                "Temperatur 2": "30°C",
            }

            # Zeige die Sensordaten in Labels an
            for key, value in sensor_data.items():
                self.sensor_labels[key]["text"] = f"{key}: {value}"

        def reset_sensor_status():
            # Setze die Labels zurück
            for key in self.sensor_labels:
                self.sensor_labels[key]["text"] = ""

        tk.Button(
            frame,
            text="Energieverbrauch",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(
            frame,
            text="Temperaturen",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(
            frame,
            text="Messwerte",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(
            frame,
            text="Systemdruck",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(
            frame,
            text="Historische Daten",
            font=("Arial", 12),
            width=20,
            height=3,
            command=reset_sensor_status,
        ).grid(row=0, column=4, padx=10, pady=5)

        # Button "Status Sensoren" neben den anderen Buttons platzieren
        tk.Button(
            frame,
            text="Status Sensoren",
            font=("Arial", 12),
            width=20,
            height=3,
            command=show_sensor_status,
        ).grid(row=0, column=5, padx=10, pady=5)

    def create_kompressor_ostfalia_buttons(self, frame):
        tk.Button(
            frame, text="Energieverbräuche", font=("Arial", 12), width=20, height=3
        ).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Messwerte", font=("Arial", 12), width=20, height=3).grid(
            row=0, column=1, padx=10, pady=5
        )
        tk.Button(
            frame, text="Historische Daten", font=("Arial", 12), width=20, height=3
        ).grid(row=0, column=2, padx=10, pady=5)

import tkinter as tk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.menu_frames = {}

        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

    def create_kompressor_ipt_page(self):
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        tk.Button(kompressor_ipt_frame, text="Status Sensoren").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Energieverbrauch", command=self.show_energy_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Temperatur", command=self.show_temperature_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Messwerte").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Systemdruck").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Historische Daten").pack(pady=5, padx=10, side=tk.LEFT)

    def create_kompressor_ostfalia_page(self):
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        tk.Button(kompressor_ostfalia_frame, text="Energieverbräuche", command=self.show_energy_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Messwerte").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Temperatur", command=self.show_temperature_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Historische Daten").pack(pady=5, padx=10, side=tk.LEFT)

    def close_all_menus(self):
        for frame in self.menu_frames.values():
            frame.destroy()
        self.menu_frames = {}

    def show_temperature_options(self):
        self.close_all_menus()
        temperature_options_frame = tk.Frame(self)
        temperature_options_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_options_frame

        tk.Button(temperature_options_frame, text="7 Tage").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_options_frame, text="24h").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_options_frame, text="Zurück", command=lambda: self.close_menu("Temperature")).pack(pady=5, padx=10, side=tk.LEFT)

    def show_energy_options(self):
        self.close_all_menus()
        energy_options_frame = tk.Frame(self)
        energy_options_frame.pack(padx=10, pady=10)
        self.menu_frames["Energy"] = energy_options_frame

        tk.Button(energy_options_frame, text="7 Tage").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="24h").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="Zurück", command=lambda: self.close_menu("Energy")).pack(pady=5, padx=10, side=tk.LEFT)

    def close_menu(self, menu_name):
        if menu_name in self.menu_frames:
            self.menu_frames[menu_name].destroy()
            del self.menu_frames[menu_name]


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
