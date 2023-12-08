#Verlauf Temperatur und Systemdruck

import tkinter as tk
import matplotlib.pyplot as plt
import random

# Funktionen für die Diagramme mit Dummy-Daten
def plot_temperature():
    # Dummy-Temperaturdaten generieren
    x = list(range(1, 11))
    y = [random.uniform(35, 40) for _ in range(10)]

    # Diagramm erstellen und Daten anzeigen
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='--', color='b')
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur')
    plt.title('Systemtemperatur über die Zeit')
    plt.grid(True)
    plt.show()

def plot_pressure():
    # Dummy-Druckdaten generieren
    x = list(range(1, 11))
    y = [random.uniform(100, 110) for _ in range(10)]

    # Diagramm erstellen und Daten anzeigen
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o', linestyle='--', color='r')
    plt.xlabel('Zeit')
    plt.ylabel('Druck')
    plt.title('Systemdruck über die Zeit')
    plt.grid(True)
    plt.show()

# Funktionen für die Auswahl der Diagramme
def show_temperature():
    new_frame.tkraise()
    plot_temperature()

def show_pressure():
    new_frame.tkraise()
    plot_pressure()

# Funktion, um das Programm zu beenden
def close_app():
    root.attributes('-fullscreen', False)
    root.destroy()

# GUI erstellen
root = tk.Tk()
root.title("Systemdaten")
root.geometry("300x150")  # Größe des Hauptfensters

# Vollbildmodus aktivieren
root.attributes('-fullscreen', True)

main_frame = tk.Frame(root)
main_frame.pack()

temp_button = tk.Button(main_frame, text="Systemtemperatur", command=show_temperature, height=2, width=20)
temp_button.pack(padx=20, pady=10)

pressure_button = tk.Button(main_frame, text="Systemdruck", command=show_pressure, height=2, width=20)
pressure_button.pack(padx=20, pady=10)

new_frame = tk.Frame(root)
new_frame.pack()

main_frame.tkraise()

# Schließ-X
close_button = tk.Button(root, text="X", command=close_app, bg="red", fg="white", font=("Arial", 12), width=2)
close_button.place(x=root.winfo_screenwidth()-30, y=0)

root.mainloop()

