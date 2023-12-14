from unittest.mock import MagicMock

# Erstellen einer simulierten Datenbankverbindung
mock_db = MagicMock()

# Simulieren der Verbindungsherstellung
mock_db.connect.return_value = "Verbindung erfolgreich"

# Simulieren eines Cursors
cursor = MagicMock()
mock_db.cursor.return_value = cursor

# Simulieren der 'execute' Methode
cursor.execute.return_value = None

# Simulieren der 'fetchall' Methode für spezifische Daten
simulated_data = {
  "Kompressor_IPT": [
    {
      "ID": "12205254",
      "Zeitstempel": "2023-11-10 11:56:27.410",
      "Energie gesamt": "18988.191285"
    }
  ],
  "Kompressor_IPT_Entlueftung": [
    {
      "ID": "12203203",
      "Zeitstempel": "2023-11-10 11:56:27.390",
      "Energie gesamt": "36.17966"
    }
  ],
  "Kompressor_IPT_Kuehler": [
    {
      "ID": "12203200",
      "Zeitstempel": "2023-11-10 11:56:27.400",
      "Energie gesamt": "1008.193971"
    }
  ],
  "Kompressor_IPT_Sensoren": [
    {
      "Zeitstempel": "2023-11-10 11:56:27.380",
      "Druck": "7.04412",
      "Durchfluss": "132.202",
      "Temperatur1": "23.898",
      "Temperatur2": "1372"
    }
  ],
  "Kompressor_Ostfalia": [
    {
      "ID": "12205255",
      "Zeitstempel": "2023-11-10 11:56:27.310",
      "Energie gesamt": "11108.303394999999"
    }
  ]
}


cursor.fetchall.return_value = simulated_data

# Beispiel für die Verwendung
print(mock_db.connect())  # Gibt "Verbindung erfolgreich" zurück
cursor.execute("SELECT * FROM kompressoren")
print(cursor.fetchall())  # Gibt simulierte Daten zurück