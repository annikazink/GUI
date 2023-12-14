import tkinter as tk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)

        self.menu_frames = {}
        self.current_menu_frame = None  # Aktuell geöffnetes Menü
        self.temperature_submenu = None  # Referenz auf das Untermenü "Temperatur"
        self.temperature_submenu_7days = None  # Referenz auf das Untermenü "7 Tage"

        self.create_kompressor_ipt_page()
        self.create_kompressor_ostfalia_page()

    def create_kompressor_ipt_page(self):
        kompressor_ipt_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ipt_frame, text="Kompressor IPT")

        tk.Button(kompressor_ipt_frame, text="Kompressor", command=self.show_KompressorIPT_Kompressor).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Entluefter", command=self.show_KompressorIPT_Entluefter).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Kuehler", command=self.show_KompressorIPT_Kuehler).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Gesamt", command=self.show_KompressorIPT_Gesamt).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ipt_frame, text="Historische Daten", command=self.show_KompressorIPT_HistorischeDaten).pack(pady=5, padx=10, side=tk.LEFT)

    def create_kompressor_ostfalia_page(self):
        kompressor_ostfalia_frame = tk.Frame(self.notebook)
        self.notebook.add(kompressor_ostfalia_frame, text="Kompressor Ostfalia")

        tk.Button(kompressor_ostfalia_frame, text="Energieverbrauch",
                  command=self.show_KompressorOstfalia_Energieverbrauch).pack(pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Messwerte", command=self.show_KompressorOstfalia_Messwerte).pack(
            pady=5, padx=10, side=tk.LEFT)
        tk.Button(kompressor_ostfalia_frame, text="Historische Daten", command=self.show_KompressorOstfalia_HistorischeDaten).pack(
            pady=5, padx=10, side=tk.LEFT)

    def close_current_menu(self):
        if self.current_menu_frame:
            self.current_menu_frame.destroy()
            self.current_menu_frame = None

    def show_KompressorIPT_Kompressor(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        kompressordatenIPT_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        kompressordatenIPT_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames[
            "KompressordatenIPT"] = kompressordatenIPT_frame  # Aktualisiert den Frame-Schlüssel im Dictionary
        self.current_menu_frame = kompressordatenIPT_frame  # Aktualisiert das aktuell geöffnete Menü

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Button(kompressordatenIPT_frame, text="Energie", command=self.plot_KompressorIPT_Kompressor_Energie).pack(pady=5,
                                                                                                 padx=10,
                                                                                                 side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(kompressordatenIPT_frame, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                                 padx=10,
                                                                                                 side=tk.LEFT)

    def show_KompressorIPT_Entluefter(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        entluefterIPT_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        entluefterIPT_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        EntluefterIPT = entluefterIPT_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = entluefterIPT_frame  # Aktualisiert das aktuell geöffnete Menü

        # Label, das anzeigt, dass aktuell keine Daten verfügbar sind
        tk.Button(EntluefterIPT, text="Energie", command=self.plot_KompressorIPT_Entluefter_Energie).pack(pady=5,
                                                                                      padx=10,
                                                                                      side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(EntluefterIPT, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                     padx=10,
                                                                                     side=tk.LEFT)

    def show_KompressorIPT_Kuehler(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        kuehlerIPT_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        kuehlerIPT_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        KuehlerIPT = kuehlerIPT_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = kuehlerIPT_frame  # Aktualisiert das aktuell geöffnete Menü

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(KuehlerIPT, text="Energie", command=self.plot_KompressorIPT_Kuehler_Energie).pack(pady=5,
                                                                                   padx=10,
                                                                                   side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(KuehlerIPT, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                  padx=10,
                                                                                  side=tk.LEFT)

    def show_KompressorIPT_Gesamt(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        gesamtIPT_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        gesamtIPT_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        GesamtIPT = gesamtIPT_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = gesamtIPT_frame  # Aktualisiert das aktuell geöffnete Menü

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(GesamtIPT, text="Druck", command=self.plot_KompressorIPT_Gesamt_Druck).pack(pady=5,
                                                                                  padx=10,
                                                                                  side=tk.LEFT)

        tk.Button(GesamtIPT, text="Durchfluss", command=self.plot_KompressorIPT_Gesamt_Durchfluss).pack(pady=5,
                                                                                              padx=10,
                                                                                              side=tk.LEFT)

        tk.Button(GesamtIPT, text="Temperatur", command=self.plot_KompressorIPT_Gesamt_Temperatur).pack(pady=5,
                                                                                                        padx=10,
                                                                                                        side=tk.LEFT)

        tk.Button(GesamtIPT, text="Energie", command=self.plot_KompressorIPT_Gesamt_Energie).pack(pady=5,
                                                                                                        padx=10,
                                                                                                        side=tk.LEFT)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(GesamtIPT, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                   padx=10,
                                                                                   side=tk.LEFT)

    def show_KompressorIPT_HistorischeDaten(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        historischeDatenIPT_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        historischeDatenIPT_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        HistorischeDatenIPT = historischeDatenIPT_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = historischeDatenIPT_frame  # Aktualisiert das aktuell geöffnete Menü

        # Label, das anzeigt, dass aktuell keine historischen Daten verfügbar sind
        tk.Label(HistorischeDatenIPT, text="Aktuell keine historischen Daten verfügbar.").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(HistorischeDatenIPT, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                           padx=10,
                                                                                           side=tk.LEFT)

    def show_KompressorOstfalia_Energieverbrauch(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        energieverbrauchOstfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        energieverbrauchOstfalia_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        EnergieverbrauchOstfalia = energieverbrauchOstfalia_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = energieverbrauchOstfalia_frame  # Aktualisiert das aktuell geöffnete Menü

        # Label, das den Energieverbrauch anzeigt
        tk.Label(EnergieverbrauchOstfalia, text="Energieverbrauch: [Hier Energieverbrauch einfügen]").pack(pady=5,
                                                                                                           padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(EnergieverbrauchOstfalia, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                                  padx=10,
                                                                                                  side=tk.LEFT)

    def show_KompressorOstfalia_Messwerte(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        messwerteOstfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        messwerteOstfalia_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        MesswerteOstfalia = messwerteOstfalia_frame  # Aktualisiert die Variable auf den neuen Frame
        self.current_menu_frame = messwerteOstfalia_frame  # Aktualisiert das aktuell geöffnete Menü

        # Label, das die Messwerte anzeigt
        tk.Label(MesswerteOstfalia, text="Messwerte: [Hier Messwerte einfügen]").pack(pady=5, padx=10)

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(MesswerteOstfalia, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                         padx=10,
                                                                                         side=tk.LEFT)

    def show_KompressorOstfalia_HistorischeDaten(self):
        self.close_current_menu()  # Schließt das aktuell geöffnete Menü
        historischeDatenOstfalia_frame = tk.Frame(self)  # Erstellt einen neuen Frame
        historischeDatenOstfalia_frame.pack(padx=10, pady=10)  # Platziert den Frame im Hauptfenster
        self.menu_frames[
            "HistorischeDatenOstfalia"] = historischeDatenOstfalia_frame  # Aktualisiert den Frame-Schlüssel im Dictionary
        self.current_menu_frame = historischeDatenOstfalia_frame  # Aktualisiert das aktuell geöffnete Menü

        # Hier kannst du deine historischen Daten anzeigen, z.B. in einem Text-Widget
        historische_daten_label = tk.Label(historischeDatenOstfalia_frame, text="Historische Daten anzeigen:")
        historische_daten_label.pack(pady=5, padx=10)

        historische_daten_text = tk.Text(historischeDatenOstfalia_frame, width=40, height=10)
        historische_daten_text.pack(pady=5, padx=10)

        historische_daten_text.insert(tk.END, "Hier werden die historischen Daten angezeigt.")

        # Button, um zum Hauptmenü zurückzukehren
        tk.Button(historischeDatenOstfalia_frame, text="Zurück", command=self.close_current_menu).pack(pady=5,
                                                                                                       padx=10,
                                                                                                       side=tk.LEFT)

    def plot_KompressorIPT_Kompressor_Energie(self):
        pass

    def plot_KompressorIPT_Entluefter_Energie(self):
        pass

    def plot_KompressorIPT_Kuehler_Energie(self):
        pass

    def plot_KompressorIPT_Gesamt_Druck(self):
        pass

    def plot_KompressorIPT_Gesamt_Durchfluss(self):
        pass

    def plot_KompressorIPT_Gesamt_Temperatur(self):
        pass

    def plot_KompressorIPT_Gesamt_Energie(self):
        pass

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()