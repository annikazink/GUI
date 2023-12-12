import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")  # Größe des Hauptfensters
        self.title("Kompressor Daten")

        self.current_frame = None  # Aktuell angezeigtes Frame

        self.create_home_page()

    def create_home_page(self):
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        # Zerstöre das aktuelle Frame und ersetze es durch ein neues
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(expand=True)

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Buttons für jedes Gerät
        tk.Button(self, text="Gerät 1", command=lambda: master.switch_frame(GerätPage1)).pack(fill="x")
        tk.Button(self, text="Gerät 2", command=lambda: master.switch_frame(GerätPage2)).pack(fill="x")
        tk.Button(self, text="Gerät 3", command=lambda: master.switch_frame(GerätPage3)).pack(fill="x")

class GerätPage1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Erzeuge Buttons für verschiedene Aktionen für Gerät 1
        tk.Button(self, text="Energieverbrauch", command=self.show_message).pack(fill="x")
        tk.Button(self, text="Min., Max., und Durchschnitt", command=self.show_message).pack(fill="x")
        # Fügen Sie hier weitere Buttons hinzu...

        tk.Button(self, text="Zurück", command=master.create_home_page).pack(fill="x")

    def show_message(self):
        tk.messagebox.showinfo("Information", "Funktion noch nicht implementiert.")

# Klassen für GerätPage2 und GerätPage3 würden ähnlich implementiert werden...

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
