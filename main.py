from unittest.mock import MagicMock
import random

# Funktion zur Generierung eines zufälligen Datensatzes
def generate_random_data():
    data = {
        "ID": str(random.randint(10000000, 99999999)),
        "Zeitstempel": MagicMock(),
        "Zeitstempel_Unix_ms": str(random.randint(1000000000000, 9999999999999)),
        "Strom_gesamt": str(random.uniform(0, 10)),
        "Spannung_gesamt": str(random.uniform(200, 500)),
        "Wirkleistung_gesamt": str(random.uniform(0, 20)),
        "Blindleistung_gesamt": str(random.uniform(0, 5)),
        "Energie_gesamt_kwh": str(random.uniform(10000, 20000)),
        "CosPhi_gesamt": str(random.uniform(0.2, 0.9)),
        "Frequenz_gesamt": str(random.uniform(48, 52)),
        "Temperatur1": str(random.uniform(20, 30)),
        "Temperatur2": str(random.uniform(100, 200)),
        "Druck": str(random.uniform(0.5, 1.5)),
        "Durchfluss": str(random.uniform(100, 200)),
    }
    return data

# Erzeuge 12 zufällige Datensätze
datensaetze = [generate_random_data() for _ in range(12)]

# Ausgabe der Datensätze
for i, datensatz in enumerate(datensaetze):
    print(f"Datensatz {i + 1}: {datensatz}")