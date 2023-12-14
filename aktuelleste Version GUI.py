import tkinter as tk
from tkinter import ttk

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
        tk.Button(kompressor_ipt_frame, text="Energieverbrauch", command=self.show_energy_IPT_options).pack(pady=5, padx=10, side=tk.LEFT)
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
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                padx=10,
                                                                                                                side=tk.LEFT)

    def show_energy_IPT_options(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        energy_options_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        energy_options_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["EnergyIPT"] = energy_options_frame  # Speichert den Frame im Dictionary

        # Button für die 24-Stunden-Energieoption
        tk.Button(energy_options_frame, text="24h", command=self.show_energy_IPT_24h).pack(pady=5, padx=10, side=tk.LEFT)

        # Button für die 7-Tage-Energieoption
        tk.Button(energy_options_frame, text="7 Tage", command=self.show_energy_IPT_7days).pack(pady=5, padx=10, side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(energy_options_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5, padx=10, side=tk.LEFT)

    def show_energy_IPT_24h(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Label(temperature_submenu_frame, text="Hier kommen noch Daten").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def show_energy_IPT_7days(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Label(temperature_submenu_frame, text="Hier kommen noch Daten").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)



    def show_energy_options_ostfalia(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        energy_options_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        energy_options_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["EnergyOstfalia"] = energy_options_frame  # Speichert den Frame im Dictionary

        # Button für die 24-Stunden-Energieoption
        tk.Button(energy_options_frame, text="24h", command=self.show_energy_Ostfalia_24h).pack(pady=5, padx=10,
                                                                                                side=tk.LEFT)

        # Button für die 7-Tage-Energieoption
        tk.Button(energy_options_frame, text="7 Tage", command=self.show_energy_Ostfalia_7days).pack(pady=5, padx=10,
                                                                                                     side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(energy_options_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                               padx=10,
                                                                                                               side=tk.LEFT)

    def show_energy_Ostfalia_24h(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Label(temperature_submenu_frame, text="Hier kommen noch Daten").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def show_energy_Ostfalia_7days(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Label(temperature_submenu_frame, text="Hier kommen noch Daten").pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def create_temperature_submenu(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="24h", command=self.show_temperature_24h).pack(pady=5, padx=10,
                                                                                                 side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="7 Tage", command=self.show_7days_options).pack(pady=5, padx=10,
                                                                                                  side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5, padx=10,
                                                                                                                 side=tk.LEFT)

    def show_temperature_24h(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="Daten für 24 Stunden anzeigen",
                  command=self.show_temperature_24h).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def show_7days_options(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="Daten für 7 Tage anzeigen", command=self.show_7days_options).pack(
            pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def create_temperature_submenu_ostfalia(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="24h", command=self.show_temperature_24h).pack(pady=5, padx=10,
                                                                                                 side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="7 Tage", command=self.create_temperature_submenu_ostfalia_7days).pack(pady=5,
                                                                                                           padx=10,
                                                                                                           side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def create_temperature_submenu_ostfalia_24h(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="Daten für 24 Stunden anzeigen",
                  command=self.show_temperature_24h).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def create_temperature_submenu_ostfalia_7days(self):
        self.close_all_menus()
        temperature_submenu_frame = tk.Frame(self)
        temperature_submenu_frame.pack(padx=10, pady=10)
        self.menu_frames["Temperature"] = temperature_submenu_frame
        self.temperature_submenu = temperature_submenu_frame

        tk.Button(temperature_submenu_frame, text="Daten für 7 Tage anzeigen",
                  command=self.create_temperature_submenu_ostfalia_7days).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(temperature_submenu_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(pady=5,
                                                                                                                 padx=10,
                                                                                                                 side=tk.LEFT)

    def show_messwerte(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
                pady=5,
                padx=10,
                side=tk.LEFT)

    def show_messwerte_ostfalia(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
            pady=5,
            padx=10,
            side=tk.LEFT)

    def show_systemdruck(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
            pady=5,
            padx=10,
            side=tk.LEFT)

    def show_systemdruck_ostfalia(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
            pady=5,
            padx=10,
            side=tk.LEFT)


    def show_historische_daten(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
            pady=5,
            padx=10,
            side=tk.LEFT)


    def show_historische_daten_ostfalia(self):
        self.close_all_menus()  # Schließt alle geöffneten Menüs
        status_sensoren_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        status_sensoren_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames["StatusSensoren"] = status_sensoren_frame  # Speichert den Frame im Dictionary

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Label(status_sensoren_frame, text="Aktuell keine Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(status_sensoren_frame, text="Zurück", command=lambda: self.close_all_menus()).pack(
            pady=5,
            padx=10,
            side=tk.LEFT)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
