import random
from datetime import datetime, timedelta

def generiere_zufaellige_kompressor_daten(kompressor_id, startzeit, intervall_in_minuten=15):
    daten_liste = []
    aktuelle_zeit = startzeit

    intervall = timedelta(minutes=intervall_in_minuten)
    anzahl_datensaetze = int(7 * 24 * 60 / intervall_in_minuten)  # Anzahl der Datenpunkte für 7 Tage

    for _ in range(anzahl_datensaetze):
        daten = {
            "ID": kompressor_id,
            "Zeitstempel": aktuelle_zeit.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "Strom_gesamt": str(random.uniform(0.01, 0.05)),
            "Spannung_gesamt": str(random.uniform(380, 420)),
            "Wirkleistung_gesamt": str(random.uniform(5, 10)),
            "Blindleistung_gesamt": str(random.uniform(0, 2)),
            "Energie_gesamt_kwh": str(random.uniform(18000, 20000)),
            "CosPhi_gesamt": str(random.uniform(0.1, 1.0)),
            "Frequenz_gesamt": "50.0",
            "Temperatur1": str(random.uniform(20, 25)),
            "Temperatur2": str(random.uniform(130, 140)),
            "Druck": str(random.uniform(0.7, 0.8)),
            "Durchfluss": str(random.uniform(130, 140))
        }
        daten_liste.append({"Kompressor": kompressor_id, "Daten": daten})

        # Zeit für den nächsten Datensatz aktualisieren
        aktuelle_zeit -= intervall

    return daten_liste

# Startzeit festlegen (aktuelle Zeit)
startzeit = datetime.now()

# Daten für beide Kompressoren generieren
kompressor_daten_1 = generiere_zufaellige_kompressor_daten("Kompressor_1", startzeit)
kompressor_daten_2 = generiere_zufaellige_kompressor_daten("Kompressor_2", startzeit)

# Beispieldaten ausgeben
print(kompressor_daten_1[:2])  # Die ersten zwei Datensätze von Kompressor 1
