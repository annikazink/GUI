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
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.menu_frames = {}
        self.temperature_submenu = None  # Referenz auf das Untermenü "Temperatur"
        self.temperature_submenu_7days = None  # Referenz auf das Untermenü "7 Tage"

        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

    def create_kompressor_ipt_page(self):
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        tk.Button(kompressor_ipt_frame, text="Status Sensoren", command=self.show_status_sensoren).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Energieverbrauch", command=self.show_energy_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Temperatur", command=self.create_temperature_submenu).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Messwerte", command=self.show_messwerte).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Systemdruck", command=self.show_systemdruck).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Historische Daten", command=self.show_historische_daten).pack(pady=5, padx=10, side=tk.LEFT)

    def create_kompressor_ostfalia_page(self):
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        tk.Button(kompressor_ostfalia_frame, text="Energieverbrauch", command=self.show_energy_options_ostfalia).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Messwerte", command=self.show_messwerte_ostfalia).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Historische Daten", command=self.show_historische_daten_ostfalia).pack(pady=5, padx=10, side=tk.LEFT)

    def close_all_menus(self):
        for frame in self.menu_frames.values():
            frame.destroy()
        self.menu_frames = {}

    def show_status_sensoren(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Status Sensoren" hier

    def show_energy_options(self):
        self.close_all_menus()
        energy_options_frame = tk.Frame(self)
        energy_options_frame.pack(padx=10, pady=10)
        self.menu_frames["Energy"] = energy_options_frame

        tk.Button(energy_options_frame, text="24h").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="7 Tage", command=self.show_7days_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="Zurück", command=lambda: self.close_menu("Energy")).pack(pady=5, padx=10, side=tk.LEFT)

    def show_energy_options_ostfalia(self):
        self.close_all_menus()
        energy_options_frame = tk.Frame(self)
        energy_options_frame.pack(padx=10, pady=10)
        self.menu_frames["Energy"] = energy_options_frame

        tk.Button(energy_options_frame, text="24h").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="7 Tage", command=self.show_7days_options_ostfalia).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(energy_options_frame, text="Zurück", command=lambda: self.close_menu("Energy")).pack(pady=5, padx=10, side=tk.LEFT)

    def create_temperature_submenu(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="24h", command=self.show_temperature_24h).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="7 Tage", command=self.show_7days_options).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_menu("Temperature")).pack(pady=5, padx=10, side=tk.LEFT)

    def create_temperature_submenu_ostfalia(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="24h", command=self.show_temperature_24h).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="7 Tage", command=self.show_7days_options_ostfalia).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_menu("Temperature")).pack(pady=5, padx=10, side=tk.LEFT)

    def show_messwerte(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Messwerte" hier

    def show_messwerte_ostfalia(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Messwerte" auf "Kompressor Ostfalia" hier

    def show_systemdruck(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Systemdruck" hier

    def show_systemdruck_ostfalia(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Systemdruck" auf "Kompressor Ostfalia" hier

    def show_historische_daten(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Historische Daten" hier

    def show_historische_daten_ostfalia(self):
        self.close_all_menus()
        # Implementiere die Funktion für "Historische Daten" auf "Kompressor Ostfalia" hier

    def show_7days_options(self):
        if self.temperature_submenu is not None:
            self.close_menu("Temperature")
            temperature_7days_submenu_frame = tk.Frame(self)
            temperature_7days_submenu_frame.pack(padx=10, pady=10)
            self.menu_frames["Temperature7Days"] = temperature_7days_submenu_frame
            self.temperature_submenu_7days = temperature_7days_submenu_frame

            tk.Button(temperature_7days_submenu_frame, text="Zurück", command=self.close_temperature_7days_submenu).pack(pady=5, padx=10, side=tk.LEFT)

    def show_7days_options_ostfalia(self):
        if self.temperature_submenu is not None:
            self.close_menu("Temperature")
            temperature_7days_submenu_frame = tk.Frame(self)
            temperature_7days_submenu_frame.pack(padx=10, pady=10)
            self.menu_frames["Temperature7Days"] = temperature_7days_submenu_frame
            self.temperature_submenu_7days = temperature_7days_submenu_frame

            tk.Button(temperature_7days_submenu_frame, text="Zurück", command=self.close_temperature_7days_submenu).pack(pady=5, padx=10, side=tk.LEFT)

    def close_temperature_7days_submenu(self):
        if self.temperature_submenu_7days is not None:
            self.temperature_submenu_7days.destroy()
            del self.menu_frames["Temperature7Days"]

    def show_temperature_24h(self):
        if self.temperature_submenu is not None:
            self.close_menu("Temperature")
            conn = sqlite3.connect("deine_datenbank.db")  # Passe den Datenbanknamen an
            query = """
                SELECT Zeitstempel, Temperatur1, Temperatur2
                FROM deine_tabelle
                WHERE Zeitstempel >= DATETIME('now', '-1 day')
                """
            df = pd.read_sql_query(query, conn)

            if not df.empty:
                df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'])
                df.set_index('Zeitstempel', inplace=True)
                df = df.resample('H').mean()

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

                plt.plot(df.index, df['Temperatur1'], label='Temperatur1')
                plt.plot(df.index, df['Temperatur2'], label='Temperatur2')
                plt.xlabel('Zeit')
                plt.ylabel('Temperatur')
                plt.title('Temperatur in den letzten 24 Stunden')
                plt.legend()
                plt.grid(True)
                plt.tight_layout()

                plt.show()

            conn.close()

    def close_menu(self, menu_name):
        if menu_name in self.menu_frames:
            self.menu_frames[menu_name].destroy()
            del self.menu_frames[menu_name]

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
